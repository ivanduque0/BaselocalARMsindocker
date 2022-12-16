import psycopg2
import os
import subprocess
import time
import pytz
from datetime import datetime
from ping3 import ping
import urllib.request
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)
CONTRATO=os.environ.get("CONTRATO")
maximo_dias_acumular=int(os.environ.get("DIAS_ACUMULAR"))
connuri=os.environ.get("POSTGRES_URI")
connlocal = None
connheroku = None
cursorheroku=None
cursorlocal=None
listausuariosheroku=[]
listausuarioslocal=[]
listahuellasheroku=[]
listahuellaslocal=[]
listaempleadosseguricel=[]
total=0
fechahoy=None
fechaayer=None
diasacumulados=[]
etapa=0
total_ping = 0
nroCaptahuellasConHuella=0
nroCaptahuellasSinHuella=0
captahuella_actual=0
TIEMPO_PING=int(os.environ.get('TIEMPO_PING'))

######################################
#############ACCESOS###################
#######################################
acceso1=os.environ.get('URL_ACCESO1')
acceso2=os.environ.get('URL_ACCESO2')
acceso3=os.environ.get('URL_ACCESO3')
acceso4=os.environ.get('URL_ACCESO4')
acceso5=os.environ.get('URL_ACCESO5')
acceso6=os.environ.get('URL_ACCESO6')
acceso7=os.environ.get('URL_ACCESO7')
acceso8=os.environ.get('URL_ACCESO8')
acceso9=os.environ.get('URL_ACCESO9')
acceso10=os.environ.get('URL_ACCESO10')
acceso11=os.environ.get('URL_ACCESO11')
acceso12=os.environ.get('URL_ACCESO12')
acceso13=os.environ.get('URL_ACCESO13')
acceso14=os.environ.get('URL_ACCESO14')
acceso15=os.environ.get('URL_ACCESO15')
acceso16=os.environ.get('URL_ACCESO16')
acceso17=os.environ.get('URL_ACCESO17')
acceso18=os.environ.get('URL_ACCESO18')
acceso19=os.environ.get('URL_ACCESO19')
acceso20=os.environ.get('URL_ACCESO20')

descripcion_acceso1=os.environ.get('RAZON_ACCESO1')
descripcion_acceso2=os.environ.get('RAZON_ACCESO2')
descripcion_acceso3=os.environ.get('RAZON_ACCESO3')
descripcion_acceso4=os.environ.get('RAZON_ACCESO4')
descripcion_acceso5=os.environ.get('RAZON_ACCESO5')
descripcion_acceso6=os.environ.get('RAZON_ACCESO6')
descripcion_acceso7=os.environ.get('RAZON_ACCESO7')
descripcion_acceso8=os.environ.get('RAZON_ACCESO8')
descripcion_acceso9=os.environ.get('RAZON_ACCESO9')
descripcion_acceso10=os.environ.get('RAZON_ACCESO10')
descripcion_acceso11=os.environ.get('RAZON_ACCESO11')
descripcion_acceso12=os.environ.get('RAZON_ACCESO12')
descripcion_acceso13=os.environ.get('RAZON_ACCESO13')
descripcion_acceso14=os.environ.get('RAZON_ACCESO14')
descripcion_acceso15=os.environ.get('RAZON_ACCESO15')
descripcion_acceso16=os.environ.get('RAZON_ACCESO16')
descripcion_acceso17=os.environ.get('RAZON_ACCESO17')
descripcion_acceso18=os.environ.get('RAZON_ACCESO18')
descripcion_acceso19=os.environ.get('RAZON_ACCESO19')
descripcion_acceso20=os.environ.get('RAZON_ACCESO20')

######################################
#############CAPTAHUELLAS#############
#######################################

captahuella1=os.environ.get('URL_CAPTAHUELLA1')
captahuella2=os.environ.get('URL_CAPTAHUELLA2')
captahuella3=os.environ.get('URL_CAPTAHUELLA3')
captahuella4=os.environ.get('URL_CAPTAHUELLA4')
captahuella5=os.environ.get('URL_CAPTAHUELLA5')
captahuella6=os.environ.get('URL_CAPTAHUELLA6')
captahuella7=os.environ.get('URL_CAPTAHUELLA7')
captahuella8=os.environ.get('URL_CAPTAHUELLA8')
captahuella9=os.environ.get('URL_CAPTAHUELLA9')
captahuella10=os.environ.get('URL_CAPTAHUELLA10')
captahuella11=os.environ.get('URL_CAPTAHUELLA11')
captahuella12=os.environ.get('URL_CAPTAHUELLA12')
captahuella13=os.environ.get('URL_CAPTAHUELLA13')
captahuella14=os.environ.get('URL_CAPTAHUELLA14')
captahuella15=os.environ.get('URL_CAPTAHUELLA15')
captahuella16=os.environ.get('URL_CAPTAHUELLA16')
captahuella17=os.environ.get('URL_CAPTAHUELLA17')
captahuella18=os.environ.get('URL_CAPTAHUELLA18')
captahuella19=os.environ.get('URL_CAPTAHUELLA19')
captahuella20=os.environ.get('URL_CAPTAHUELLA20')

######################################
################RFID###################
#######################################

rfid1=os.environ.get('URL_RFID1')
rfid2=os.environ.get('URL_RFID2')
rfid3=os.environ.get('URL_RFID3')
rfid4=os.environ.get('URL_RFID4')
rfid5=os.environ.get('URL_RFID5')
rfid6=os.environ.get('URL_RFID6')
rfid7=os.environ.get('URL_RFID7')
rfid8=os.environ.get('URL_RFID8')
rfid9=os.environ.get('URL_RFID9')
rfid10=os.environ.get('URL_RFID10')
rfid11=os.environ.get('URL_RFID11')
rfid12=os.environ.get('URL_RFID12')
rfid13=os.environ.get('URL_RFID13')
rfid14=os.environ.get('URL_RFID14')
rfid15=os.environ.get('URL_RFID15')
rfid16=os.environ.get('URL_RFID16')
rfid17=os.environ.get('URL_RFID17')
rfid18=os.environ.get('URL_RFID18')
rfid19=os.environ.get('URL_RFID19')
rfid20=os.environ.get('URL_RFID20')

dispositivos=[
            acceso1, acceso2, acceso3, acceso4,
            acceso5, acceso6, acceso7, acceso8,
            acceso9, acceso10, acceso11, acceso12,
            acceso13, acceso14, acceso15, acceso16,
            acceso17, acceso18, acceso19, acceso20,
            captahuella1, captahuella2, captahuella3, captahuella4,
            captahuella5, captahuella6, captahuella7, captahuella8,
            captahuella9, captahuella10, captahuella11, captahuella12,
            captahuella13, captahuella14, captahuella15, captahuella16,
            captahuella17, captahuella18, captahuella19, captahuella20, 
            rfid1, rfid2, rfid3, rfid4, rfid5,
            rfid6, rfid7, rfid8, rfid9, rfid10,
            rfid11, rfid12, rfid13, rfid14, rfid15,
            rfid16, rfid17, rfid18, rfid19, rfid20,
            ]

captahuellas=[captahuella1, captahuella2, captahuella3, captahuella4, captahuella5,
              captahuella6, captahuella7, captahuella8, captahuella9, captahuella10,
              captahuella11, captahuella12, captahuella13, captahuella14, captahuella15,
              captahuella16, captahuella17, captahuella18, captahuella19, captahuella20, 
              ]

intentos=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
        
        if not connuri:
            conn_info = subprocess.run(["heroku", "config:get", "DATABASE_URL", "-a", 'tesis-reconocimiento-facial'], stdout = subprocess.PIPE)
            connuri = conn_info.stdout.decode('utf-8').strip()
        
        connheroku = psycopg2.connect(connuri)
        cursorheroku = connheroku.cursor()
        t1_ping=time.perf_counter()
        while True:
            t2_ping=time.perf_counter()
            total_ping=t2_ping-t1_ping

            if total_ping > TIEMPO_PING:
                for dispositivo in dispositivos:
                    intentos_tabla=dispositivos.index(dispositivo)
                    if dispositivo:
                        longitud_url=len(dispositivo)
                        ping_dispositivo = ping(dispositivo[7:longitud_url])
                        if ping_dispositivo:
                            cursorlocal.execute('UPDATE web_dispositivos SET estado=1 WHERE dispositivo=%s', (dispositivo,))
                            connlocal.commit()
                            intentos[intentos_tabla]=0
                        else:
                            intentos[intentos_tabla]=intentos[intentos_tabla]+1
                            if intentos[intentos_tabla] >= 4:
                                cursorlocal.execute('UPDATE web_dispositivos SET estado=0 WHERE dispositivo=%s', (dispositivo,))
                                connlocal.commit()
                t1_ping=time.perf_counter()

            if etapa==0:
                tz = pytz.timezone('America/Caracas')
                caracas_now = datetime.now(tz)
                fechahoy=str(caracas_now)[:10]

                if fechahoy != fechaayer:
                    fechaayer=fechahoy
                    tupla_fecha_hoy=(fechahoy,)
                    cursorlocal.execute('SELECT fecha FROM dias_acumulados')
                    dias_acumulados= cursorlocal.fetchall()
                    nro_dias_acumulados=len(dias_acumulados)

                    if nro_dias_acumulados >= maximo_dias_acumular:
                        cursorlocal.execute('DELETE FROM web_interacciones *')
                        cursorlocal.execute('DELETE FROM dias_acumulados *')
                        connlocal.commit()
                        
                    if not tupla_fecha_hoy in dias_acumulados:
                        cursorlocal.execute('''INSERT INTO dias_acumulados (fecha)
                        VALUES (%s);''', (fechahoy,))
                        connlocal.commit()

                cursorlocal.execute('SELECT * FROM web_interacciones where contrato=%s and fecha=%s', (CONTRATO,fechahoy))
                interacciones_local= cursorlocal.fetchall()
                cursorheroku.execute('SELECT nombre, fecha, hora, razon, contrato, cedula FROM web_interacciones where contrato=%s and fecha=%s', (CONTRATO,fechahoy))
                interacciones_heroku= cursorheroku.fetchall()

                nro_int_local = len(interacciones_local)
                nro_int_heroku = len(interacciones_heroku)

                if nro_int_local != nro_int_heroku:

                    for interaccion in interacciones_local:
                        try:
                            interacciones_heroku.index(interaccion)
                        except ValueError:
                            nombre=interaccion[0]
                            fecha=interaccion[1]
                            hora=interaccion[2]
                            razon=interaccion[3]
                            cedula=interaccion[5]
                            cursorheroku.execute('''INSERT INTO web_interacciones (nombre, fecha, hora, razon, contrato, cedula)
                            VALUES (%s, %s, %s, %s, %s, %s);''', (nombre, fecha, hora, razon, CONTRATO, cedula))
                            connheroku.commit()
                    
                    nombre=None
                    fecha=None
                    hora=None
                    razon=None
                    cedula=None
                etapa=1

            if etapa==1:

                cursorlocal.execute('SELECT * FROM web_usuarios')
                usuarios_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT cedula FROM web_usuarios where contrato_id=%s or contrato_id=%s', (CONTRATO,'SEGURICEL'))
                usuarios_heroku= cursorheroku.fetchall()


                for usuario in usuarios_local:
                    cedula=usuario[0]
                    try:
                        listausuarioslocal.index(cedula)
                    except ValueError:
                        listausuarioslocal.append(cedula)
                
                for usuario in listausuarioslocal:
                    cursorheroku.execute('SELECT entrada, salida, cedula, dia FROM web_horariospermitidos WHERE cedula=%s and (contrato_id=%s or contrato_id=%s)',(usuario,CONTRATO,'SEGURICEL'))
                    diasheroku= cursorheroku.fetchall()
                    
                    cursorlocal.execute('SELECT * FROM web_horariospermitidos WHERE cedula_id=%s',(usuario,))
                    diaslocal= cursorlocal.fetchall()

                    if len(diasheroku) > 0 and len(diasheroku) > len(diaslocal):
                        for diasherokuiterar in diasheroku:
                            try:
                                diaslocal.index(diasherokuiterar)
                            except ValueError:
                                entrada=diasherokuiterar[0]
                                salida=diasherokuiterar[1]
                                cedula=diasherokuiterar[2]
                                dia=diasherokuiterar[3]
                                cursorlocal.execute('''INSERT INTO web_horariospermitidos (entrada, salida, cedula_id, dia)
                                VALUES (%s, %s, %s, %s);''', (entrada, salida, cedula, dia))
                                connlocal.commit()

                    if len(diaslocal) > len(diasheroku):
                        for diaslocaliterar in diaslocal:
                            try:
                                diasheroku.index(diaslocaliterar)
                            except ValueError:
                                entrada=diaslocaliterar[0]
                                salida=diaslocaliterar[1]
                                cedula=diaslocaliterar[2]
                                dia=diaslocaliterar[3]
                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE entrada=%s AND salida=%s AND cedula_id=%s AND dia=%s',(entrada, salida, cedula, dia))
                                connlocal.commit()
                diaslocal=[]
                diasheroku=[]
                listausuariosheroku=[]
                listausuarioslocal=[]
                etapa=2

            if etapa==2:

                cursorlocal.execute('SELECT cedula, telegram_id FROM web_usuarios')
                usuarios_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT cedula, telegram_id FROM web_usuarios where contrato_id=%s or contrato_id=%s', (CONTRATO,'SEGURICEL'))
                usuarios_heroku= cursorheroku.fetchall()
                
                nro_usu_local = len(usuarios_local)
                nro_usu_heroku = len(usuarios_heroku)
            
                if nro_usu_heroku == nro_usu_local:
                    for usuario in usuarios_heroku:
                        try:
                            usuarios_local.index(usuario)
                        except ValueError:
                            cedula=usuario[0]
                            telegram_id=usuario[1]
                            cursorlocal.execute("UPDATE web_usuarios SET telegram_id=%s WHERE cedula=%s", (telegram_id,cedula))
                            connlocal.commit()
                etapa=3

            if etapa==3:

                cursorlocal.execute('SELECT * FROM web_usuarios')
                usuarios_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT cedula FROM web_usuarios where contrato_id=%s or contrato_id=%s', (CONTRATO,'SEGURICEL'))
                usuarios_heroku= cursorheroku.fetchall()

                nro_usu_local = len(usuarios_local)
                nro_usu_heroku = len(usuarios_heroku)
            
                #cuando se va a eliminar un usuario
                if nro_usu_local > nro_usu_heroku:

                    for usuario in usuarios_heroku:
                        cedula=usuario[0]
                        try:
                            listausuariosheroku.index(cedula)
                        except ValueError:
                            listausuariosheroku.append(cedula)
                    
                    for usuario in usuarios_local:
                        cedula=usuario[0]
                        try:
                            listausuarioslocal.index(cedula)
                        except ValueError:
                            listausuarioslocal.append(cedula)

                    for usuario in listausuarioslocal:
                        try:
                            listausuariosheroku.index(usuario)
                        except ValueError:
                            cursorlocal.execute('SELECT id_suprema FROM web_huellas where cedula=%s', (usuario,))
                            huellas_local= cursorlocal.fetchall()
                            HuellasPorBorrar=len(huellas_local)
                            HuellasBorradas=0
                            nroCaptahuellasSinHuella=0
                            captahuella_actual=0
                            for huella_local in huellas_local:
                                id_suprema = huella_local[0]
                                id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                for captahuella in captahuellas:
                                    if captahuella:
                                        captahuella_actual=captahuella_actual+1
                                        try:
                                            peticion = urllib.request.urlopen(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                            if peticion.getcode() == 200:
                                                nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                        except:
                                            print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                if nroCaptahuellasSinHuella == captahuella_actual:
                                    cursorlocal.execute('DELETE FROM web_huellas WHERE id_suprema=%s', (id_suprema,))
                                    connlocal.commit()
                                    HuellasBorradas=HuellasBorradas+1
                            if HuellasBorradas == HuellasPorBorrar:
                                cursorlocal.execute('DELETE FROM web_usuarios WHERE cedula=%s', (usuario,))
                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE cedula_id=%s', (usuario,))
                                connlocal.commit()
                    listausuariosheroku=[]
                    listausuarioslocal=[]

                # cuando se va a agregar usuarios
                if nro_usu_heroku > nro_usu_local:

                    for usuario in usuarios_heroku:
                        cedula=usuario[0]
                        try:
                            listausuariosheroku.index(cedula)
                        except ValueError:
                            listausuariosheroku.append(cedula)
                    
                    for usuario in usuarios_local:
                        cedula=usuario[0]
                        try:
                            listausuarioslocal.index(cedula)
                        except ValueError:
                            listausuarioslocal.append(cedula)

                    for usuario in listausuariosheroku:
                        try:
                            listausuarioslocal.index(usuario)
                        except ValueError:
                            cursorheroku.execute('SELECT cedula, nombre FROM web_usuarios where cedula=%s and (contrato_id=%s or contrato_id=%s)', (usuario, CONTRATO, 'SEGURICEL'))
                            usuario_heroku= cursorheroku.fetchall()
                            cedula=usuario_heroku[0][0]
                            nombre=usuario_heroku[0][1]
                            cursorlocal.execute('''INSERT INTO web_usuarios (cedula, nombre)
                            VALUES (%s, %s)''', (cedula, nombre))
                            connlocal.commit()
                    listausuariosheroku=[]
                    listausuarioslocal=[]
                etapa=4

            if etapa==4:
                cursorlocal.execute('SELECT * FROM web_dispositivos')
                dispositivos_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT dispositivo, descripcion, estado FROM web_dispositivos where contrato_id=%s', (CONTRATO,))
                dispositivos_heroku= cursorheroku.fetchall()

                if len(dispositivos_heroku) != len(dispositivos_local):
                    cursorheroku.execute('''DELETE FROM web_dispositivos * WHERE contrato_id=%s''', (CONTRATO,))
                    connheroku.commit()
                    cursorheroku.execute('SELECT dispositivo, descripcion, estado FROM web_dispositivos where contrato_id=%s', (CONTRATO,))
                    dispositivos_heroku= cursorheroku.fetchall()
                    for dispositivolocal in dispositivos_local:
                        try:
                            dispositivos_heroku.index(dispositivolocal)
                        except ValueError:
                            tz = pytz.timezone('America/Caracas')
                            caracas_now = datetime.now(tz)
                            fechaahora=str(caracas_now)[:10]
                            hora=str(caracas_now)[11:19]
                            horaahora = datetime.strptime(hora, '%H:%M:%S').time()
                            dispositivo=dispositivolocal[0]
                            descripcion=dispositivolocal[1]
                            estado=dispositivolocal[2]
                            acceso=dispositivolocal[3]
                            cursorheroku.execute('''INSERT INTO web_dispositivos (dispositivo, descripcion, estado, contrato_id, fecha, hora, acceso)
                            VALUES (%s, %s, %s, %s, %s, %s, %s);''', (dispositivo, descripcion, estado, CONTRATO, fechaahora, horaahora, acceso))
                            connheroku.commit()
                else:
                    for dispositivolocal in dispositivos_local:
                        try:
                            dispositivos_heroku.index(dispositivolocal)
                        except ValueError:
                            tz = pytz.timezone('America/Caracas')
                            caracas_now = datetime.now(tz)
                            fechaahora=str(caracas_now)[:10]
                            hora=str(caracas_now)[11:19]
                            horaahora = datetime.strptime(hora, '%H:%M:%S').time()
                            dispositivo=dispositivolocal[0]
                            descripcion=dispositivolocal[1]
                            estado=dispositivolocal[2]
                            cursorheroku.execute('UPDATE web_dispositivos SET estado=%s, fecha=%s, hora=%s WHERE dispositivo=%s AND descripcion=%s AND contrato_id=%s;', 
                            (estado,fechaahora,horaahora, dispositivo, descripcion, CONTRATO))
                            connheroku.commit()
                etapa=5
            
            if etapa==5:

                cursorlocal.execute('SELECT * FROM web_usuarios')
                usuarios_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT cedula FROM web_usuarios where contrato_id=%s or contrato_id=%s', (CONTRATO,'SEGURICEL'))
                usuarios_heroku= cursorheroku.fetchall()

                cursorheroku.execute('SELECT cedula FROM web_usuarios where contrato_id=%s', ('SEGURICEL',))
                empleados_seguricel= cursorheroku.fetchall()
                
                for usuario in usuarios_local:
                    cedula=usuario[0]
                    try:
                        listausuarioslocal.index(cedula)
                    except ValueError:
                        listausuarioslocal.append(cedula)

                for usuario in usuarios_heroku:
                    cedula=usuario[0]
                    try:
                        listausuariosheroku.index(cedula)
                    except ValueError:
                        listausuariosheroku.append(cedula)
                
                for empleado_seguricel in empleados_seguricel:
                    cedula=empleado_seguricel[0]
                    try:
                        listaempleadosseguricel.index(cedula)
                    except ValueError:
                        listaempleadosseguricel.append(cedula)
                
                if len(usuarios_local) == len(usuarios_heroku):

                    for usuario_local in listausuarioslocal:
                        cursorlocal.execute('SELECT template, id_suprema FROM web_huellas where cedula=%s', (usuario_local,))
                        huellas_local= cursorlocal.fetchall()

                        cursorheroku.execute('SELECT template, id_suprema FROM web_huellas where cedula=%s', (usuario_local,))
                        huellas_heroku= cursorheroku.fetchall()

                        nro_huellas_local = len(huellas_local)
                        nro_huellas_heroku = len(huellas_heroku)
                        #cuando se van a eliminar huellas
                        if nro_huellas_local > nro_huellas_heroku:

                            for usuario in huellas_heroku:
                                template=usuario[0]
                                try:
                                    listahuellasheroku.index(template)
                                except ValueError:
                                    listahuellasheroku.append(template)
                            
                            for usuario in huellas_local:
                                template=usuario[0]
                                try:
                                    listahuellaslocal.index(template)
                                except ValueError:
                                    listahuellaslocal.append(template)

                            for templateEnLista in listahuellaslocal:
                                try:
                                    listahuellasheroku.index(templateEnLista)
                                except ValueError:
                                    nroCaptahuellasSinHuella=0
                                    captahuella_actual=0
                                    cursorlocal.execute('SELECT id_suprema FROM web_huellas where template=%s', (templateEnLista,))
                                    huella_local= cursorlocal.fetchall()
                                    id_suprema = huella_local[0][0]
                                    id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                    id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                    for captahuella in captahuellas:
                                        if captahuella:
                                            captahuella_actual=captahuella_actual+1
                                            try:
                                                peticion = urllib.request.urlopen(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                                if peticion.getcode() == 200:
                                                    nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                            except:
                                                print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                    if nroCaptahuellasSinHuella == captahuella_actual:
                                        cursorlocal.execute('DELETE FROM web_huellas WHERE template=%s', (templateEnLista,))
                                        connlocal.commit()
                            listahuellasheroku=[]
                            listahuellaslocal=[]

                        # cuando se van a agregar huellas
                        if nro_huellas_heroku > nro_huellas_local:

                            for usuario in huellas_heroku:
                                template=usuario[0]
                                try:
                                    listahuellasheroku.index(template)
                                except ValueError:
                                    listahuellasheroku.append(template)
                            
                            for usuario in huellas_local:
                                template=usuario[0]
                                try:
                                    listahuellaslocal.index(template)
                                except ValueError:
                                    listahuellaslocal.append(template)

                            for templateEnLista in listahuellasheroku:
                                try:
                                    listahuellaslocal.index(templateEnLista)
                                except ValueError:
                                    cursorheroku.execute('SELECT id_suprema, cedula, template FROM web_huellas where template=%s', (templateEnLista,))
                                    huella_heroku= cursorheroku.fetchall()
                                    id_suprema=huella_heroku[0][0]
                                    cedula=huella_heroku[0][1]
                                    template=huella_heroku[0][2]
                                    nroCaptahuellasConHuella=0
                                    captahuella_actual=0
                                    IdSupremaContador=0 #esto lo uso para ver si hay id de suprema disponibles
                                    if not id_suprema:
                                        cursorlocal.execute('SELECT id_suprema FROM web_huellas ORDER BY id_suprema ASC')
                                        ids_suprema_local= cursorlocal.fetchall()
                                        nro_ids_suprema_local=len(ids_suprema_local)
                                        if not ids_suprema_local:
                                            id_suprema = 1
                                            if not cedula in listaempleadosseguricel:
                                                cursorheroku.execute('UPDATE web_huellas SET id_suprema=%s WHERE template=%s', (id_suprema, template))
                                                connheroku.commit()
                                        else:
                                            for id_suprema_local in ids_suprema_local:
                                                IdSupremaContador=IdSupremaContador+1
                                                if not id_suprema_local[0] == IdSupremaContador:
                                                    id_suprema=IdSupremaContador
                                                    if not cedula in listaempleadosseguricel:
                                                        cursorheroku.execute('UPDATE web_huellas SET id_suprema=%s WHERE template=%s', (id_suprema, template))
                                                        connheroku.commit()
                                                    break
                                            if nro_ids_suprema_local == IdSupremaContador:
                                                id_suprema=IdSupremaContador+1
                                                if not cedula in listaempleadosseguricel:
                                                    cursorheroku.execute('UPDATE web_huellas SET id_suprema=%s WHERE template=%s', (id_suprema, template))
                                                    connheroku.commit()
                                    id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                    id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                    for captahuella in captahuellas:
                                        if captahuella:
                                            captahuella_actual=captahuella_actual+1
                                            try:
                                                peticion = urllib.request.urlopen(url=f'{captahuella}/anadir/{id_suprema_hex}/{template}0A', timeout=3)
                                                if peticion.getcode() == 200:
                                                    nroCaptahuellasConHuella=nroCaptahuellasConHuella+1
                                            except:
                                                print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                    if nroCaptahuellasConHuella == captahuella_actual and captahuella_actual != 0:
                                        cursorlocal.execute('''INSERT INTO web_huellas (id_suprema, cedula, template)
                                        VALUES (%s, %s, %s)''', (id_suprema, cedula, template))
                                        connlocal.commit()
                                    elif captahuella_actual != nroCaptahuellasConHuella and nroCaptahuellasConHuella != 0:
                                        for captahuella in captahuellas:
                                            try:
                                                peticion = urllib.request.urlopen(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                                if peticion.getcode() == 200:
                                                    pass
                                            except:
                                                print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                            listahuellasheroku=[]
                            listahuellaslocal=[]
                listausuariosheroku=[]
                listausuarioslocal=[]
                listaempleadosseguricel=[]
                etapa=6

            if etapa==6:
                cursorlocal.execute('SELECT epc, cedula FROM web_tagsrfid')
                tags_local= cursorlocal.fetchall()

                cursorheroku.execute('SELECT epc, cedula FROM web_tagsrfid where contrato_id=%s or contrato_id=%s', (CONTRATO,'SEGURICEL'))
                tags_heroku= cursorheroku.fetchall()

                nro_tags_local = len(tags_local)
                nro_tags_heroku = len(tags_heroku)

                if nro_tags_heroku > nro_tags_local:
                    for tagherokuiterar in tags_heroku:
                        try:
                            tags_local.index(tagherokuiterar)
                        except ValueError:
                            epc=tagherokuiterar[0]
                            cedula=tagherokuiterar[1]
                            cursorlocal.execute('''INSERT INTO web_tagsrfid (epc, cedula)
                            VALUES (%s, %s);''', (epc, cedula))
                            connlocal.commit()

                if nro_tags_local > nro_tags_heroku:
                    for taglocaliterar in tags_local:
                        try:
                            tags_heroku.index(taglocaliterar)
                        except ValueError:
                            epc=taglocaliterar[0]
                            cedula=taglocaliterar[1]
                            cursorlocal.execute('DELETE FROM web_tagsrfid WHERE epc=%s AND cedula=%s',(epc, cedula))
                            connlocal.commit()
                etapa=7

            if etapa==7:
                cursorlocal.execute('SELECT id, estado FROM solicitud_aperturas')
                aperturas_local= cursorlocal.fetchall()
                if aperturas_local:
                    for aperturalocal in aperturas_local:
                        if aperturalocal[1] == 1:
                            idapertura=aperturalocal[0]
                            cursorheroku.execute('DELETE FROM web_apertura WHERE id=%s', (idapertura,))
                            connheroku.commit()
                            cursorlocal.execute('DELETE FROM solicitud_aperturas WHERE id=%s', (idapertura,))
                            connlocal.commit()
                etapa=0


    except (Exception, psycopg2.Error) as error:
        print("fallo en hacer las consultas")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
        if connheroku:
            cursorheroku.close()
            connheroku.close()
    finally:
        print("se ha cerrado la conexion a la base de datos")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
        if connheroku:
            cursorheroku.close()
            connheroku.close()
            
