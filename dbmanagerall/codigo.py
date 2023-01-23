import psycopg2
import os
import time as tm
import pytz
from datetime import datetime, date, time
from ping3 import ping
from dotenv import load_dotenv
from pathlib import Path
import requests

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)
CONTRATO=os.environ.get("CONTRATO")
URL_API=os.environ.get("URL_API")
maximo_dias_acumular=int(os.environ.get("DIAS_ACUMULAR"))
connlocal = None
cursorlocal=None
listaHuellasServidor=[]
listahuellaslocal=[]
listaempleadosseguricel=[]
total=0
fechahoy=None
fechaayer=None
dias_acumulados=[]
total_ping = 0
nroCaptahuellasConHuella=0
nroCaptahuellasSinHuella=0
captahuella_actual=0
TIEMPO_PING=int(os.environ.get('TIEMPO_PING'))
TIEMPO_CAMBIOS=int(os.environ.get('TIEMPO_CAMBIOS'))
TIEMPO_LOG=int(os.environ.get('TIEMPO_LOG'))
BorrarPeticionesListas= True
AccesosSinCerrar=True

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
    
    t1=tm.perf_counter()
    while total<=5:
        t2=tm.perf_counter()
        total=t2-t1
    total=0
    t1=0
    t2=0
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
        
        t1_ping=tm.perf_counter()
        t1_cambios=tm.perf_counter()
        t1_log=tm.perf_counter()
        while True:
            t2_ping=tm.perf_counter()
            t2_cambios=tm.perf_counter()
            t2_log=tm.perf_counter()
            total_ping=t2_ping-t1_ping
            total_cambios=t2_cambios-t1_cambios
            total_log=t2_log-t1_log

            try:
                try:
                    cursorlocal.execute('SELECT dispositivo, descripcion, estado, acceso FROM web_dispositivos')
                    dispositivos_local= cursorlocal.fetchall()

                    request_json = requests.get(url=f'{URL_API}obtenerdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                    dispositivosServidor=[]
                    for consultajson in request_json:
                        tuplaDispositivoIndividual=(consultajson['dispositivo'],consultajson['descripcion'], consultajson['estado'], consultajson['acceso'],)
                        dispositivosServidor.append(tuplaDispositivoIndividual)

                    if len(dispositivosServidor) != len(dispositivos_local):
                        request_json = requests.delete(url=f'{URL_API}eliminartodosdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                        if request_json.status_code == 200:

                            request_json = requests.get(url=f'{URL_API}obtenerdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                            dispositivosServidor=[]
                            for consultajson in request_json:
                                tuplaDispositivoIndividual=(consultajson['dispositivo'],consultajson['descripcion'], consultajson['estado'], consultajson['acceso'],)
                                dispositivosServidor.append(tuplaDispositivoIndividual)

                            for dispositivolocal in dispositivos_local:
                                try:
                                    dispositivosServidor.index(dispositivolocal)
                                except ValueError:
                                    tz = pytz.timezone('America/Caracas')
                                    caracas_now = datetime.now(tz)
                                    fecha=str(caracas_now)[:10]
                                    hora=str(caracas_now)[11:19]
                                    dispositivo=dispositivolocal[0]
                                    descripcion=dispositivolocal[1]
                                    estado=dispositivolocal[2]
                                    acceso=dispositivolocal[3]
                                    agregarDispositivoJson = {
                                        "dispositivo": dispositivo,
                                        "descripcion": descripcion,
                                        "estado": estado,
                                        "contrato": CONTRATO,
                                        "acceso": acceso,
                                        "fecha": fecha,
                                        "hora": hora
                                    }
                                    requests.post(url=f'{URL_API}registrardispositivosapi/', 
                                    json=agregarDispositivoJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                    else:
                        for dispositivolocal in dispositivos_local:
                            # try:
                            #     dispositivosServidor.index(dispositivolocal)
                            # except ValueError:
                            if not dispositivolocal in dispositivosServidor:
                                tz = pytz.timezone('America/Caracas')
                                caracas_now = datetime.now(tz)
                                fecha=str(caracas_now)[:10]
                                hora=str(caracas_now)[11:19]
                                dispositivo=dispositivolocal[0]
                                estado=dispositivolocal[2]
                                jsonActualizarDispositivo= {
                                    "estado": estado,
                                    "fecha": fecha,
                                    "hora": hora
                                }
                                requests.put(url=f'{URL_API}actualizardispositivosapi/{CONTRATO}/{dispositivo[7:]}/{estado}/',
                                json=jsonActualizarDispositivo, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                except requests.exceptions.ConnectionError:
                    print("fallo consultando api de dispositivos")   
            except Exception as e:
                print(f"{e} - fallo total en los dispositivos")  

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
                t1_ping=tm.perf_counter()

            if total_cambios > TIEMPO_CAMBIOS:
                try:
                    request_json = requests.get(url=f'{URL_API}vercambiosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                    for consultajson in request_json:
                        idCambio=consultajson['id']
                        tablaCambiada=consultajson['tabla']
                        cedulaUsuario=consultajson['cedula']

                        # print(f'idCambio:{idCambio}')
                        # print(f'tablaCambiada:{tablaCambiada}')
                        # print(f'cedulaUsuario:{cedulaUsuario}')

                        if tablaCambiada == 'Usuarios':
                            try:
                                try:
                                    banderaUsuario=True
                                    if cedulaUsuario == 'completo':
                                        cursorlocal.execute('SELECT cedula, nombre, telegram_id, internet, wifi, captahuella, rfid, facial FROM web_usuarios')
                                        usuarios_local= cursorlocal.fetchall()
                                        
                                        request_json_usuario = requests.get(url=f'{URL_API}obtenerusuariosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                                        usuariosServidor=[]
                                        for consultajson in request_json_usuario:
                                            tuplaUsuarioIndividual=(consultajson['cedula'],consultajson['nombre'],consultajson['telegram_id'], consultajson['telefonoInternet'], consultajson['telefonoWifi'], consultajson['captahuella'], consultajson['rfid'], consultajson['reconocimientoFacial'],)
                                            usuariosServidor.append(tuplaUsuarioIndividual)
                                        for usuario in usuariosServidor:
                                            # contador=contador+1
                                            # print(contador)
                                            # print(usuario)
                                            if not usuario in usuarios_local:
                                                cedula=usuario[0]
                                                telegram_id=usuario[2]
                                                internet=usuario[3]
                                                wifi=usuario[4]
                                                captahuella=usuario[5]
                                                rfid=usuario[6]
                                                facial=usuario[7]
                                                cursorlocal.execute("UPDATE web_usuarios SET telegram_id=%s, internet=%s, wifi=%s, captahuella=%s, rfid=%s, facial=%s WHERE cedula=%s", (telegram_id,internet,wifi,captahuella,rfid,facial,cedula))
                                                connlocal.commit()
                                        usuariosServidor=[]
                                    else:
                                        cursorlocal.execute('SELECT cedula, nombre, telegram_id, internet, wifi, captahuella, rfid, facial FROM web_usuarios WHERE cedula=%s',(cedulaUsuario,))
                                        usuario_local= cursorlocal.fetchall()

                                        request_json_usuario = requests.get(url=f'{URL_API}usuarioindividualapi/{CONTRATO}/{cedulaUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()
                                        usuarioLocal=len(usuario_local)
                                        usuarioServidor=len(request_json_usuario)
                                        if usuarioLocal and not usuarioServidor:
                                            cursorlocal.execute('SELECT id_suprema FROM web_huellas where cedula=%s', (cedulaUsuario,))
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
                                                            requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                                            nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                                        except:
                                                            print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                                            banderaUsuario=False
                                                if nroCaptahuellasSinHuella == captahuella_actual:
                                                    cursorlocal.execute('DELETE FROM web_huellas WHERE id_suprema=%s', (id_suprema,))
                                                    connlocal.commit()
                                                    HuellasBorradas=HuellasBorradas+1
                                            if HuellasBorradas == HuellasPorBorrar:
                                                cursorlocal.execute('DELETE FROM web_usuarios WHERE cedula=%s', (cedulaUsuario,))
                                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE cedula_id=%s', (cedulaUsuario,))
                                                connlocal.commit()
                                        elif not usuarioLocal and usuarioServidor: 
                                            for consultajson in request_json_usuario:
                                                cedula=consultajson['cedula']
                                                nombre=consultajson['nombre']
                                                telegram_id=consultajson['telegram_id']
                                                internet=consultajson['telefonoInternet']
                                                wifi=consultajson['telefonoWifi']
                                                captahuella=consultajson['captahuella']
                                                rfid=consultajson['rfid']
                                                facial=consultajson['reconocimientoFacial']
                                            cursorlocal.execute('''INSERT INTO web_usuarios (cedula, nombre, telegram_id, internet, wifi, captahuella, rfid, facial)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (cedula, nombre, telegram_id, internet, wifi, captahuella, rfid, facial))
                                            connlocal.commit()
                                        elif usuarioLocal and usuarioServidor:
                                            for consultajson in request_json_usuario:
                                                cedula=consultajson['cedula']
                                                telegram_id=consultajson['telegram_id']
                                                internet=consultajson['telefonoInternet']
                                                wifi=consultajson['telefonoWifi']
                                                captahuella=consultajson['captahuella']
                                                rfid=consultajson['rfid']
                                                facial=consultajson['reconocimientoFacial']
                                            cursorlocal.execute("UPDATE web_usuarios SET telegram_id=%s, internet=%s, wifi=%s, captahuella=%s, rfid=%s, facial=%s WHERE cedula=%s", (telegram_id,internet,wifi,captahuella,rfid,facial,cedula))
                                            connlocal.commit()
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en usuarios")
                                    banderaUsuario=False
                            except Exception as e:
                                print(f"{e} - fallo total usuarios")
                                banderaUsuario=False
                            if banderaUsuario:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                        elif tablaCambiada == 'Horarios':
                            try:
                                try:
                                    banderaHorario=True
                                    request_json_horarios = requests.get(url=f'{URL_API}obtenerhorariosindividualapi/{CONTRATO}/{cedulaUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()
                                            
                                    horariosServidor=[]
                                    for consultajson in request_json_horarios:
                                        entradaObjetohora=time.fromisoformat(consultajson['entrada'])
                                        salidaObjetohora=time.fromisoformat(consultajson['salida'])
                                        TuplaHorarioIndividual=(entradaObjetohora,salidaObjetohora,consultajson['cedula'],consultajson['dia'],)
                                        horariosServidor.append(TuplaHorarioIndividual)
                                    
                                    cursorlocal.execute('SELECT * FROM web_horariospermitidos WHERE cedula_id=%s',(cedulaUsuario,))
                                    horariosLocal= cursorlocal.fetchall()

                                    for horario in horariosServidor:
                                        if not horario in horariosLocal:
                                            entrada=horario[0]
                                            salida=horario[1]
                                            cedula=horario[2]
                                            dia=horario[3]
                                            cursorlocal.execute('''INSERT INTO web_horariospermitidos (entrada, salida, cedula_id, dia)
                                            VALUES (%s, %s, %s, %s);''', (entrada, salida, cedula, dia))
                                            connlocal.commit()

                                    for horariosLocaliterar in horariosLocal:
                                        if not horariosLocaliterar in horariosServidor:
                                            entrada=horariosLocaliterar[0]
                                            salida=horariosLocaliterar[1]
                                            cedula=horariosLocaliterar[2]
                                            dia=horariosLocaliterar[3]
                                            cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE entrada=%s AND salida=%s AND cedula_id=%s AND dia=%s',(entrada, salida, cedula, dia))
                                            connlocal.commit()
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en horarios")
                                    banderaHorario=False
                            except Exception as e:
                                print(f"{e} - fallo total horarios")
                                banderaHorario=False
                            if banderaHorario:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                        elif tablaCambiada == 'Huellas':
                            try:
                                try:
                                    banderaHuella = True
                                    cursorlocal.execute('SELECT template, id_suprema, cedula FROM web_huellas where cedula=%s', (cedulaUsuario,))
                                    huellas_local= cursorlocal.fetchall()

                                    request_json = requests.get(url=f'{URL_API}obtenerhuellasapi/{cedulaUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                                    huellasServidor=[]
                                    for consultajson in request_json:
                                        tuplaHuellaIndividual=(consultajson['template'], consultajson['id_suprema'], consultajson['cedula'],)
                                        huellasServidor.append(tuplaHuellaIndividual)

                                    for huella in huellas_local:
                                        if not huella in huellasServidor:
                                            nroCaptahuellasSinHuella=0
                                            captahuella_actual=0
                                            template=huella[0]
                                            id_suprema = huella[1]
                                            id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                            id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                            for captahuella in captahuellas:
                                                if captahuella:
                                                    captahuella_actual=captahuella_actual+1
                                                    try:
                                                        requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                                        nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                                    except:
                                                        print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")  
                                            if nroCaptahuellasSinHuella == captahuella_actual:
                                                cursorlocal.execute('DELETE FROM web_huellas WHERE template=%s', (template,))
                                                connlocal.commit()
                                            else:
                                                banderaHuella = False  

                                    for huella in huellasServidor:
                                        if not huella in huellas_local:
                                            id_suprema=huella[1]
                                            cedula=huella[2]
                                            template=huella[0]
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
                                                        requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                                else:
                                                    for id_suprema_local in ids_suprema_local:
                                                        IdSupremaContador=IdSupremaContador+1
                                                        if not id_suprema_local[0] == IdSupremaContador:
                                                            id_suprema=IdSupremaContador
                                                            if not cedula in listaempleadosseguricel:
                                                                requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                                            break
                                                    if nro_ids_suprema_local == IdSupremaContador:
                                                        id_suprema=IdSupremaContador+1
                                                        if not cedula in listaempleadosseguricel:
                                                            requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                            id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                            id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                            for captahuella in captahuellas:
                                                if captahuella:
                                                    captahuella_actual=captahuella_actual+1
                                                    try:
                                                        requests.get(url=f'{captahuella}/anadir/{id_suprema_hex}/{template}0A', timeout=3)
                                                        nroCaptahuellasConHuella=nroCaptahuellasConHuella+1
                                                    except:
                                                        print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                            if nroCaptahuellasConHuella == captahuella_actual and captahuella_actual != 0:
                                                cursorlocal.execute('''INSERT INTO web_huellas (id_suprema, cedula, template)
                                                VALUES (%s, %s, %s)''', (id_suprema, cedula, template))
                                                connlocal.commit()
                                            elif captahuella_actual != nroCaptahuellasConHuella and nroCaptahuellasConHuella != 0:
                                                banderaHuella = False  
                                                for captahuella in captahuellas:
                                                    try:
                                                        requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=3)
                                                    except:
                                                        print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en huellas")
                                    banderaHuella=False
                            except Exception as e:
                                print(f"{e} - fallo total huellas")
                                banderaHuella=False
                            if banderaHuella:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                        elif tablaCambiada == 'Tags':
                            try:
                                try:
                                    banderaTag=True
                                    cursorlocal.execute('SELECT epc, cedula FROM web_tagsrfid WHERE cedula=%s', (cedulaUsuario,))
                                    tags_local= cursorlocal.fetchall()
                                    
                                    request_json = requests.get(url=f'{URL_API}obtenertagsrfidindividualapi/{CONTRATO}/{cedulaUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()
                                    tagsServidor=[]
                                    for consultajson in request_json:
                                        tuplaTagIndividual=(consultajson['epc'],consultajson['cedula'],)
                                        tagsServidor.append(tuplaTagIndividual)

                                    nro_tags_local = len(tags_local)
                                    nro_tags_servidor = len(tagsServidor)

                                    for tagServidor in tagsServidor:
                                        if not tagServidor in tags_local:
                                            epc=tagServidor[0]
                                            cedula=tagServidor[1]
                                            cursorlocal.execute('''INSERT INTO web_tagsrfid (epc, cedula)
                                            VALUES (%s, %s);''', (epc, cedula))
                                            connlocal.commit()

                                    for taglocaliterar in tags_local:
                                        if not taglocaliterar in tagsServidor:
                                            epc=taglocaliterar[0]
                                            cedula=taglocaliterar[1]
                                            cursorlocal.execute('DELETE FROM web_tagsrfid WHERE epc=%s AND cedula=%s',(epc, cedula))
                                            connlocal.commit()
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en tags")
                                    banderaTag=False
                            except Exception as e:
                                print(f"{e} - fallo total tags")
                                banderaTag=False
                            if banderaTag:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                        else:
                            requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                    t1_cambios=tm.perf_counter()
                except Exception as e:
                    print(f"{e} - fallo en api para obtener cambios")
            
            if total_log > TIEMPO_LOG:
                try:
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

                    try:
                        cursorlocal.execute('SELECT * FROM web_interacciones where contrato=%s and fecha=%s', (CONTRATO,fechahoy))
                        interacciones_local= cursorlocal.fetchall()
                    
                        request_json = requests.get(url=f'{URL_API}obtenerinteraccionesapi/{CONTRATO}/{fechahoy}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()

                        listaLogsServidor=[]
                        for consultajson in request_json:
                            objetofecha= date.fromisoformat(consultajson['fecha'])
                            objetohora=time.fromisoformat(consultajson['hora'])
                            tuplaLogIndividual=(consultajson['nombre'],objetofecha,objetohora,consultajson['razon'],consultajson['contrato'],consultajson['cedula'])
                            listaLogsServidor.append(tuplaLogIndividual)

                        nro_int_local = len(interacciones_local)
                        nro_int_servidor = len(listaLogsServidor)

                        if nro_int_local != nro_int_servidor:

                            for interaccion in interacciones_local:
                                if not interaccion in listaLogsServidor:
                                    nombre=interaccion[0]
                                    fecha=interaccion[1]
                                    hora=interaccion[2]
                                    razon=interaccion[3]
                                    cedula=interaccion[5]
                                    anadirLogJson = {
                                        "nombre": nombre,
                                        "fecha": fecha.isoformat(),
                                        "hora": hora.isoformat(),
                                        "razon": razon,
                                        "contrato": CONTRATO,
                                        "cedula": cedula
                                    }
                                    requests.post(url=f'{URL_API}registrarinteraccionesapi/', 
                                    json=anadirLogJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                    except requests.exceptions.ConnectionError:
                        print("fallo consultando api de logs")
                except Exception as e:
                    print(f"{e} - fallo total al subir Log")
                BorrarPeticionesListas=True
                t1_log=tm.perf_counter()

            if BorrarPeticionesListas:
                try:
                    cursorlocal.execute('SELECT id, estado, peticionInternet, feedback FROM solicitud_aperturas')
                    aperturas_local= cursorlocal.fetchall()
                    if aperturas_local:
                        for aperturalocal in aperturas_local:
                            if aperturalocal[1] == 1:
                                idapertura=aperturalocal[0]
                                peticionDesdeInternet=aperturalocal[2]
                                feedbackPeticion=aperturalocal[3]
                                if peticionDesdeInternet and feedbackPeticion:
                                    try:
                                        request_json = requests.delete(url=f'{URL_API}eliminarsolicitudesaperturaapi/{idapertura}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                        if request_json.status_code == 200 or request_json.status_code == 500:
                                            cursorlocal.execute('DELETE FROM solicitud_aperturas WHERE id=%s', (idapertura,))
                                            connlocal.commit()
                                    except requests.exceptions.ConnectionError:
                                        print("fallo consultando api de peticiones de aperturas")
                                elif not peticionDesdeInternet:# and feedbackPeticion:
                                    cursorlocal.execute('DELETE FROM solicitud_aperturas WHERE id=%s', (idapertura,))
                                    connlocal.commit()
                    BorrarPeticionesListas=False
                except Exception as e:
                    print(f"{e} - fallo total eliminando peticiones de aperturas")
    
            if AccesosSinCerrar:
                try:
                    cursorlocal.execute('SELECT cedula, acceso, fecha, hora, estado FROM accesos_abiertos')
                    accesosAbiertos = cursorlocal.fetchall()

                    if accesosAbiertos:
                        for acceso_abierto in accesosAbiertos:
                            estado=acceso_abierto[4]
                            if estado:
                                try:
                                    cedula=acceso_abierto[0]
                                    fecha=acceso_abierto[2]
                                    hora=acceso_abierto[3]
                                    accesoo=acceso_abierto[1]
                                    requests.delete(url=f'{URL_API}eliminarpuertaabiertaapi/{CONTRATO}/{cedula}/{accesoo}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                    cursorlocal.execute('DELETE FROM accesos_abiertos WHERE cedula=%s AND fecha=%s AND hora=%s', (cedula, fecha, hora))
                                    connlocal.commit()
                                except Exception as e:
                                    print(f"{e} - fallo total borrando puerta abierta del acceso:{accesoo}")    
                            else:
                                tz = pytz.timezone('America/Caracas')
                                caracas_now = datetime.now(tz)
                                hora=str(caracas_now)[11:19]
                                hora_hora=int(hora[:2])
                                hora_minuto=int(hora[3:5])
                                fecha=str(caracas_now)[:10]

                                fecha_apertura=acceso_abierto[2].isoformat()
                                apertura_hora_completa = acceso_abierto[3].isoformat()
                                apertura_hora=int(apertura_hora_completa[:2])
                                apertura_minuto=int(apertura_hora_completa[3:5])
                                diferencia_horas=hora_hora-apertura_hora
                                diferencia_minutos=hora_minuto-apertura_minuto

                                if fecha_apertura != fecha or diferencia_horas!=0 or diferencia_minutos != 0:
                                    try:
                                        cedula=acceso_abierto[0]
                                        accesoo=acceso_abierto[1]
                                        comprobarAccesos = requests.get(url=f'{URL_API}eliminarpuertaabiertaapi/{CONTRATO}/{cedula}/{accesoo}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3).json()
                                        if not comprobarAccesos:
                                            anadirJson = {
                                                "contrato": CONTRATO,
                                                "cedula": cedula,
                                                "acceso": accesoo,
                                                "fecha": fecha_apertura,
                                                "hora": apertura_hora_completa
                                                }
                                            requests.post(url=f'{URL_API}agregarpuertaabiertaapi/', 
                                            json=anadirJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=3)
                                            #print("La puerta ha permanecido demasiado tiempo abierta!")
                                    except Exception as e:
                                        print(f"{e} - fallo total agregando puerta abierta del acceso:{accesoo}")    
                except Exception as e:
                    print(f"{e} - fallo total manejando los accesos sin cerrar")
    except (Exception, psycopg2.Error) as error:
        print(f"{error} - fallo en hacer las consultas en base ded atos de managerall")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
    finally:
        print("se ha cerrado la conexion a la base de datos")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
            
