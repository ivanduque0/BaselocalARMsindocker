import psycopg2
import os
import time
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)
connlocal = None
cursorlocal=None
total=0

SERVIDOR_LOCAL=os.environ.get('URL_SERVIDOR')

######################################
#############ACCESOS###################
#######################################
acceso1=os.environ.get('URL_ACCESO1')
acceso2=os.environ.get('URL_ACCESO2')
acceso3=os.environ.get('URL_ACCESO3')
acceso4=os.environ.get('URL_ACCESO4')

descripcion_acceso1=os.environ.get('RAZON_BOT1')
descripcion_acceso2=os.environ.get('RAZON_BOT2')
descripcion_acceso3=os.environ.get('RAZON_BOT3')
descripcion_acceso4=os.environ.get('RAZON_BOT4')

captahuella1=os.environ.get('URL_CAPTAHUELLA1')
captahuella2=os.environ.get('URL_CAPTAHUELLA2')
captahuella3=os.environ.get('URL_CAPTAHUELLA3')
captahuella4=os.environ.get('URL_CAPTAHUELLA4')

descripcion_captahuella1=os.environ.get('RAZON_CAPTAHUELLA1')
descripcion_captahuella2=os.environ.get('RAZON_CAPTAHUELLA2')
descripcion_captahuella3=os.environ.get('RAZON_CAPTAHUELLA3')
descripcion_captahuella4=os.environ.get('RAZON_CAPTAHUELLA4')

dispositivos=[acceso1, acceso2, acceso3, acceso4,captahuella1, captahuella2, captahuella3, captahuella4, SERVIDOR_LOCAL      
      
             ]

dispositivos_dict ={acceso1:descripcion_acceso1, 
                    acceso2:descripcion_acceso2, 
                    acceso3:descripcion_acceso3, 
                    acceso4:descripcion_acceso4, 
                    captahuella1:descripcion_captahuella1, 
                    captahuella2:descripcion_captahuella2, 
                    captahuella3:descripcion_captahuella3, 
                    captahuella4:descripcion_captahuella4, 
                    SERVIDOR_LOCAL:'SERVIDOR LOCAL',
                    
                    }

while True:
    
    t1=time.perf_counter()
    while total<=5:
        t2=time.perf_counter()
        total=t2-t1
    total=0
    try:
        
        #con esto se apunta a la base de datos local
        connlocal = psycopg2.connect(
            database=os.environ.get("DATABASE"), 
            user=os.environ.get("USERDB"), 
            password=os.environ.get("PASSWORD"), 
            host=os.environ.get("HOST"), 
            port=os.environ.get("PORT")
        )
        cursorlocal = connlocal.cursor()

        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_usuarios (cedula varchar(150), nombre varchar(150), telegram_id varchar(150), contrato_id varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_interacciones (nombre varchar(150), fecha date, hora time without time zone, razon varchar(150), contrato varchar(150), cedula_id varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_horariospermitidos (entrada time without time zone, salida time without time zone, cedula_id varchar(150), dia varchar(180))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS dias_acumulados (fecha varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_dispositivos (dispositivo varchar(150), descripcion varchar(150), estado varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_huellas (id_suprema integer, cedula varchar(150), template text)')
        #cursorlocal.execute('CREATE TABLE IF NOT EXISTS led (onoff integer, acceso integer)')
        connlocal.commit()
        
        cursorlocal.execute('SELECT*FROM web_dispositivos')
        tabladispositivos= cursorlocal.fetchall()
        
        if len(tabladispositivos) < 1:
            for dispositivo in dispositivos:
                if dispositivo:
                    descripcion = dispositivos_dict[dispositivo]
                    if dispositivo == SERVIDOR_LOCAL:
                        estado = '1'
                    else:
                        estado = '0'
                    cursorlocal.execute('INSERT INTO web_dispositivos values(%s, %s, %s)',(dispositivo, descripcion, estado))
                    connlocal.commit()
        
        # cursorlocal.execute('SELECT*FROM led')
        # tablaled= cursorlocal.fetchall()
        # if len(tablaled) < 1:
        #     cursorlocal.execute('INSERT INTO led values(0,1)')
        #     connlocal.commit()
        #     cursorlocal.execute('INSERT INTO led values(0,2)')
        #     connlocal.commit()
        #     cursorlocal.execute('INSERT INTO led values(0,3)')
        #     connlocal.commit()
        #     cursorlocal.execute('INSERT INTO led values(0,4)')
        #     connlocal.commit()

    except (Exception, psycopg2.Error) as error:
        print("fallo en hacer las consultas")
        if connlocal:
            cursorlocal.close()
            connlocal.close()

    finally:
        print("se ha cerrado la conexion a la base de datos")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
        break
    
