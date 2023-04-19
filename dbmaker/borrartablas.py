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

        cursorlocal.execute('DROP TABLE IF EXISTS web_usuarios')
        cursorlocal.execute('DROP TABLE IF EXISTS web_logs_usuarios')
        cursorlocal.execute('DROP TABLE IF EXISTS web_logs_vigilantes')
        cursorlocal.execute('DROP TABLE IF EXISTS web_logs_visitantes')
        cursorlocal.execute('DROP TABLE IF EXISTS web_horariospermitidos')
        cursorlocal.execute('DROP TABLE IF EXISTS dias_acumulados')
        cursorlocal.execute('DROP TABLE IF EXISTS web_dispositivos')
        cursorlocal.execute('DROP TABLE IF EXISTS web_huellas')
        cursorlocal.execute('DROP TABLE IF EXISTS web_tagsrfid')
        cursorlocal.execute('DROP TABLE IF EXISTS solicitud_aperturas')
        cursorlocal.execute('DROP TABLE IF EXISTS accesos_abiertos')
        cursorlocal.execute('DROP TABLE IF EXISTS control_horarios_visitantes')
        cursorlocal.execute('DROP TABLE IF EXISTS web_unidades')
        connlocal.commit()

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
    
