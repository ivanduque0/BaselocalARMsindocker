import psycopg2
import os
import time
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env.manager')
load_dotenv(dotenv_path=dotenv_path)
connlocal = None
cursorlocal=None
total=0

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

        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_usuarios (cedula integer, nombre varchar(150), telegram_id varchar(150), contrato_id varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_interacciones (nombre varchar(150), fecha date, hora time without time zone, razon varchar(150), contrato varchar(150), cedula_id integer)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_horariospermitidos (entrada time without time zone, salida time without time zone, cedula_id integer, dia varchar(180))')
        #cursorlocal.execute('CREATE TABLE IF NOT EXISTS led (onoff integer, acceso integer)')
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
    
