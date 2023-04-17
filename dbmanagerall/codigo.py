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
CONTRATO_ID=os.environ.get("CONTRATO_ID")
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
BorrarPeticionesListas= False
AccesosSinCerrar=False
borrarHorariosVisitantes=False

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

######################################
##############BLUETOOTH################
#######################################

bluetooth1=os.environ.get('URL_BLUETOOTH1')
bluetooth2=os.environ.get('URL_BLUETOOTH2')
bluetooth3=os.environ.get('URL_BLUETOOTH3')
bluetooth4=os.environ.get('URL_BLUETOOTH4')
bluetooth5=os.environ.get('URL_BLUETOOTH5')
bluetooth6=os.environ.get('URL_BLUETOOTH6')
bluetooth7=os.environ.get('URL_BLUETOOTH7')
bluetooth8=os.environ.get('URL_BLUETOOTH8')
bluetooth9=os.environ.get('URL_BLUETOOTH9')
bluetooth10=os.environ.get('URL_BLUETOOTH10')
bluetooth11=os.environ.get('URL_BLUETOOTH11')
bluetooth12=os.environ.get('URL_BLUETOOTH12')
bluetooth13=os.environ.get('URL_BLUETOOTH13')
bluetooth14=os.environ.get('URL_BLUETOOTH14')
bluetooth15=os.environ.get('URL_BLUETOOTH15')
bluetooth16=os.environ.get('URL_BLUETOOTH16')
bluetooth17=os.environ.get('URL_BLUETOOTH17')
bluetooth18=os.environ.get('URL_BLUETOOTH18')
bluetooth19=os.environ.get('URL_BLUETOOTH19')
bluetooth20=os.environ.get('URL_BLUETOOTH20')

######################################
#################RELE##################
#######################################

rele1=os.environ.get('URL_RELE1')
rele2=os.environ.get('URL_RELE2')
rele3=os.environ.get('URL_RELE3')
rele4=os.environ.get('URL_RELE4')
rele5=os.environ.get('URL_RELE5')
rele6=os.environ.get('URL_RELE6')
rele7=os.environ.get('URL_RELE7')
rele8=os.environ.get('URL_RELE8')
rele9=os.environ.get('URL_RELE9')
rele10=os.environ.get('URL_RELE10')
rele11=os.environ.get('URL_RELE11')
rele12=os.environ.get('URL_RELE12')
rele13=os.environ.get('URL_RELE13')
rele14=os.environ.get('URL_RELE14')
rele15=os.environ.get('URL_RELE15')
rele16=os.environ.get('URL_RELE16')
rele17=os.environ.get('URL_RELE17')
rele18=os.environ.get('URL_RELE18')
rele19=os.environ.get('URL_RELE19')
rele20=os.environ.get('URL_RELE20')

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
            bluetooth1, bluetooth2, bluetooth3, bluetooth4, bluetooth5,
            bluetooth6, bluetooth7, bluetooth8, bluetooth9, bluetooth10,
            bluetooth11, bluetooth12, bluetooth13, bluetooth14, bluetooth15,
            bluetooth16, bluetooth17, bluetooth18, bluetooth19, bluetooth20,
            rele1, rele2, rele3, rele4, rele5,
            rele6, rele7, rele8, rele9, rele10,
            rele11, rele12, rele13, rele14, rele15,
            rele16, rele17, rele18, rele19, rele20,
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

            # try:
            #     try:
            #         cursorlocal.execute('SELECT dispositivo, descripcion, estado, acceso FROM web_dispositivos')
            #         dispositivos_local= cursorlocal.fetchall()

            #         request_json = requests.get(url=f'{URL_API}obtenerdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

            #         dispositivosServidor=[]
            #         for consultajson in request_json:
            #             tuplaDispositivoIndividual=(consultajson['dispositivo'],consultajson['descripcion'], consultajson['estado'], consultajson['acceso'],)
            #             dispositivosServidor.append(tuplaDispositivoIndividual)

            #         if len(dispositivosServidor) != len(dispositivos_local):
            #             request_json = requests.delete(url=f'{URL_API}eliminartodosdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
            #             if request_json.status_code == 200:

            #                 request_json = requests.get(url=f'{URL_API}obtenerdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

            #                 dispositivosServidor=[]
            #                 for consultajson in request_json:
            #                     tuplaDispositivoIndividual=(consultajson['dispositivo'],consultajson['descripcion'], consultajson['estado'], consultajson['acceso'],)
            #                     dispositivosServidor.append(tuplaDispositivoIndividual)

            #                 for dispositivolocal in dispositivos_local:
            #                     try:
            #                         dispositivosServidor.index(dispositivolocal)
            #                     except ValueError:
            #                         tz = pytz.timezone('America/Caracas')
            #                         caracas_now = datetime.now(tz)
            #                         fecha=str(caracas_now)[:10]
            #                         hora=str(caracas_now)[11:19]
            #                         dispositivo=dispositivolocal[0]
            #                         descripcion=dispositivolocal[1]
            #                         estado=dispositivolocal[2]
            #                         acceso=dispositivolocal[3]
            #                         agregarDispositivoJson = {
            #                             "dispositivo": dispositivo,
            #                             "descripcion": descripcion,
            #                             "estado": estado,
            #                             "contrato": CONTRATO,
            #                             "acceso": acceso,
            #                             "fecha": fecha,
            #                             "hora": hora
            #                         }
            #                         requests.post(url=f'{URL_API}registrardispositivosapi/', 
            #                         json=agregarDispositivoJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
            #         else:
            #             for dispositivolocal in dispositivos_local:
            #                 # try:
            #                 #     dispositivosServidor.index(dispositivolocal)
            #                 # except ValueError:
            #                 if not dispositivolocal in dispositivosServidor:
            #                     tz = pytz.timezone('America/Caracas')
            #                     caracas_now = datetime.now(tz)
            #                     fecha=str(caracas_now)[:10]
            #                     hora=str(caracas_now)[11:19]
            #                     dispositivo=dispositivolocal[0]
            #                     descripcion=dispositivolocal[1]
            #                     estado=dispositivolocal[2]
            #                     jsonActualizarDispositivo= {
            #                         "contrato": CONTRATO,
            #                         "dispositivo": dispositivo,
            #                         "descripcion": descripcion,
            #                         "estado": estado,
            #                         "fecha": fecha,
            #                         "hora": hora
            #                     }
            #                     requests.put(url=f'{URL_API}actualizardispositivosapi/{CONTRATO}/{dispositivo[7:]}/{estado}/',
            #                     json=jsonActualizarDispositivo, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
            #     except requests.exceptions.ConnectionError:
            #         print("fallo consultando api de dispositivos")   
            # except Exception as e:
            #     print(f"{e} - fallo total en los dispositivos")  

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
                    request_json = requests.get(url=f'{URL_API}vercambiosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                    for consultajson in request_json:
                        idCambio=consultajson['id']
                        tablaCambiada=consultajson['tabla']
                        idUsuario=consultajson['usuario']

                        # print(f'idCambio:{idCambio}')
                        # print(f'tablaCambiada:{tablaCambiada}')
                        # print(f'idUsuario:{idUsuario}')

                        if tablaCambiada == 'Usuarios':
                            try:
                                try:
                                    banderaUsuario=True
                                    if not idUsuario:
                                        cursorlocal.execute('SELECT id, rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet, wifi, bluetooth, captahuella, rfid, facial FROM web_usuarios')
                                        usuarios_local= cursorlocal.fetchall()
                                        
                                        request_json_usuario = requests.get(url=f'{URL_API}obtenerusuariosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                                        usuariosServidor=[]
                                        for consultajson in request_json_usuario:
                                            tuplaUsuarioIndividual=(consultajson['id'],consultajson['rol'],consultajson['cedula'],consultajson['nombre'],consultajson['telegram_id'], consultajson['numero_telefonico'], consultajson['cedula_propietario'], consultajson['unidad'],consultajson['entrada_beacon_uuid'], consultajson['salida_beacon_uuid'], consultajson['telefonoInternet'], consultajson['telefonoWifi'], consultajson['telefonoBluetooth'], consultajson['captahuella'], consultajson['rfid'], consultajson['reconocimientoFacial'],)
                                            usuariosServidor.append(tuplaUsuarioIndividual)
                                        for usuario in usuariosServidor:
                                            # contador=contador+1
                                            # print(contador)
                                            # print(usuario)
                                            if not usuario in usuarios_local:
                                                id_usuario=usuario[0]
                                                rol=usuario[1]
                                                cedula=usuario[2]
                                                nombre=usuario[3]
                                                telegram_id=usuario[4]
                                                numero_telefonico=usuario[5]
                                                cedula_propietario=usuario[6]
                                                unidad_id=usuario[7]
                                                entrada_beacon_uuid=usuario[8]
                                                salida_beacon_uuid=usuario[9]
                                                internet=usuario[10]
                                                wifi=usuario[11]
                                                bluetooth=usuario[12]
                                                captahuella=usuario[13]
                                                rfid=usuario[14]
                                                facial=usuario[15]
                                                cursorlocal.execute("UPDATE web_usuarios SET rol=%s, cedula=%s, nombre=%s, telegram_id=%s, numero_telefonico=%s, cedula_propietario=%s, unidad_id=%s, entrada_beacon_uuid=%s, salida_beacon_uuid=%s, internet=%s, wifi=%s, bluetooth=%s, captahuella=%s, rfid=%s, facial=%s WHERE id=%s", (rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet, wifi, bluetooth, captahuella, rfid, facial, id_usuario))
                                                connlocal.commit()
                                        usuariosServidor=[]
                                    else:
                                        cursorlocal.execute('SELECT id, rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet, wifi, bluetooth, captahuella, rfid, facial FROM web_usuarios WHERE id=%s',(idUsuario,))
                                        usuario_local= cursorlocal.fetchall()

                                        request_json_usuario = requests.get(url=f'{URL_API}usuarioindividualapi/{CONTRATO}/{idUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                                        usuarioLocal=len(usuario_local)
                                        usuarioServidor=len(request_json_usuario)
                                        if usuarioLocal and not usuarioServidor:
                                            cursorlocal.execute('SELECT id_suprema FROM web_huellas where cedula=%s', (usuario_local[0][2],))
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
                                                            requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=10)
                                                            nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                                        except:
                                                            print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                                            banderaUsuario=False
                                                if nroCaptahuellasSinHuella == captahuella_actual:
                                                    cursorlocal.execute('DELETE FROM web_huellas WHERE id_suprema=%s', (id_suprema,))
                                                    connlocal.commit()
                                                    HuellasBorradas=HuellasBorradas+1
                                            if HuellasBorradas == HuellasPorBorrar:
                                                cursorlocal.execute('DELETE FROM web_usuarios WHERE id=%s', (idUsuario,))
                                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE usuario=%s', (idUsuario,))
                                                connlocal.commit()
                                        elif not usuarioLocal and usuarioServidor: 
                                            for consultajson in request_json_usuario:
                                                id_usuario=consultajson['id']
                                                rol=consultajson['rol']
                                                cedula=consultajson['cedula']
                                                nombre=consultajson['nombre']
                                                telegram_id=consultajson['telegram_id']
                                                numero_telefonico=consultajson['numero_telefonico']
                                                cedula_propietario=consultajson['cedula_propietario']
                                                unidad_id=consultajson['unidad']
                                                entrada_beacon_uuid=consultajson['entrada_beacon_uuid']
                                                salida_beacon_uuid=consultajson['salida_beacon_uuid']
                                                internet=consultajson['telefonoInternet']
                                                wifi=consultajson['telefonoWifi']
                                                bluetooth=consultajson['telefonoBluetooth']
                                                captahuella=consultajson['captahuella']
                                                rfid=consultajson['rfid']
                                                facial=consultajson['reconocimientoFacial']
                                            cursorlocal.execute('''INSERT INTO web_usuarios (id, rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet, wifi, bluetooth, captahuella, rfid, facial)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (id_usuario, rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet, wifi, bluetooth, captahuella, rfid, facial))
                                            connlocal.commit()
                                        elif usuarioLocal and usuarioServidor:
                                            for consultajson in request_json_usuario:
                                                id_usuario=consultajson['id']
                                                rol=consultajson['rol']
                                                cedula=consultajson['cedula']
                                                nombre=consultajson['nombre']
                                                telegram_id=consultajson['telegram_id']
                                                numero_telefonico=consultajson['numero_telefonico']
                                                cedula_propietario=consultajson['cedula_propietario']
                                                unidad_id=consultajson['unidad']
                                                entrada_beacon_uuid=consultajson['entrada_beacon_uuid']
                                                salida_beacon_uuid=consultajson['salida_beacon_uuid']
                                                internet=consultajson['telefonoInternet']
                                                wifi=consultajson['telefonoWifi']
                                                bluetooth=consultajson['telefonoBluetooth']
                                                captahuella=consultajson['captahuella']
                                                rfid=consultajson['rfid']
                                                facial=consultajson['reconocimientoFacial']
                                            cursorlocal.execute("UPDATE web_usuarios SET rol=%s, cedula=%s, nombre=%s, telegram_id=%s, numero_telefonico=%s, cedula_propietario=%s, unidad_id=%s, entrada_beacon_uuid=%s, salida_beacon_uuid=%s, internet=%s, wifi=%s, bluetooth=%s, captahuella=%s, rfid=%s, facial=%s WHERE id=%s", (rol, cedula, nombre, telegram_id, numero_telefonico, cedula_propietario, unidad_id, entrada_beacon_uuid, salida_beacon_uuid, internet,wifi,bluetooth,captahuella,rfid,facial,id_usuario))
                                            connlocal.commit()
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en usuarios")
                                    banderaUsuario=False
                            except Exception as e:
                                print(f"{e} - fallo total usuarios")
                                banderaUsuario=False
                            if banderaUsuario:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        elif tablaCambiada == 'Unidades':
                            try:
                                banderaUnidad=True
                                if not idUsuario:
                                    try:
                                        cursorlocal.execute('SELECT id, nombre, codigo FROM web_unidades')
                                        unidades_local= cursorlocal.fetchall()

                                        request_json = requests.get(url=f'{URL_API}verunidadescontratoapi/{CONTRATO_ID}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                                        unidadesServidor=[]
                                        for consultajson in request_json:
                                            tuplaUnidadIndividual=(consultajson['id'],consultajson['nombre'],consultajson['codigo'])
                                            unidadesServidor.append(tuplaUnidadIndividual)

                                        # nro_unidades_local = len(unidades_local)
                                        nro_unidades_servidor = len(unidadesServidor)

                                        # print(f'unidades en local: {nro_unidades_local}')
                                        # print(f'unidades en servidor: {nro_unidades_servidor}')

                                        # contador=0
                                        for unidadServidor in unidadesServidor:
                                            # contador=contador+1
                                            # print(contador)
                                            # print(unidadServidor)
                                            # try:
                                            #     tags_local.index(tagServidor)
                                            # except ValueError:
                                            if not unidadServidor in unidades_local:
                                                id_unidad=unidadServidor[0]
                                                nombre=unidadServidor[1]
                                                codigo=unidadServidor[2]
                                                cursorlocal.execute('''INSERT INTO web_unidades (id, nombre, codigo)
                                                VALUES (%s, %s, %s);''', (id_unidad, nombre, codigo))
                                                connlocal.commit()

                                        # contador=0
                                        for unidadLocal in unidades_local:
                                            # contador=contador+1
                                            # print(contador)
                                            # print(unidadLocal)
                                            # try:
                                            #     tagsServidor.index(taglocaliterar)
                                            # except ValueError:
                                            if not unidadLocal in unidadesServidor:
                                                id_unidad=unidadLocal[0]
                                                cursorlocal.execute('DELETE FROM web_unidades WHERE id=%s',(id_unidad,))
                                                connlocal.commit()

                                        cursorlocal.execute('SELECT id, nombre FROM web_unidades')
                                        unidades_local= cursorlocal.fetchall()
                                        
                                        nro_unidades_local = len(unidades_local)

                                        if nro_unidades_local != nro_unidades_servidor:
                                            banderaUnidad=False
                                            print(f'el numero de unidades en local y servidor a la final no coincidio')
                                    except Exception as e:
                                        print(f"{e} - fallo trayendo todas las unidades en cambios")
                                        banderaUnidad=False
                                else:
                                    cursorlocal.execute('SELECT id, nombre, codigo FROM web_unidades WHERE id=%s',(idUsuario,))
                                    unidades_local= cursorlocal.fetchall()
                                    try:
                                        request_json = requests.get(url=f'{URL_API}editarunidadapi/{idUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                                        if not unidades_local:
                                            cursorlocal.execute('''INSERT INTO web_unidades (id, nombre, codigo)
                                                VALUES (%s, %s, %s);''', (request_json['id'], request_json['nombre'], request_json['codigo']))
                                            connlocal.commit()
                                        elif unidades_local:
                                            cursorlocal.execute("UPDATE web_unidades SET id=%s, nombre=%s, codigo=%s WHERE id=%s", (request_json['id'], request_json['nombre'], request_json['codigo'], idUsuario))
                                            connlocal.commit()
                                    except:
                                        if unidades_local:
                                            cursorlocal.execute('SELECT id, cedula FROM web_usuarios WHERE unidad_id=%s', (idUsuario,))
                                            usuarios_local= cursorlocal.fetchall()
                                            usuarios_unidad= len(usuarios_local)
                                            contador_usuarios_eliminados=0
                                            for usuario in usuarios_local:
                                                cursorlocal.execute('SELECT id_suprema FROM web_huellas where cedula=%s', (usuario[1],))
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
                                                                requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=10)
                                                                nroCaptahuellasSinHuella=nroCaptahuellasSinHuella+1
                                                            except:
                                                                print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                                                banderaUnidad=False
                                                    if nroCaptahuellasSinHuella == captahuella_actual:
                                                        cursorlocal.execute('DELETE FROM web_huellas WHERE id_suprema=%s', (id_suprema,))
                                                        connlocal.commit()
                                                        HuellasBorradas=HuellasBorradas+1
                                                if HuellasBorradas == HuellasPorBorrar:
                                                    cursorlocal.execute('DELETE FROM web_usuarios WHERE id=%s', (usuario[0],))
                                                    cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE usuario=%s', (usuario[0],))
                                                    connlocal.commit()
                                                    contador_usuarios_eliminados=contador_usuarios_eliminados+1
                                            if contador_usuarios_eliminados==usuarios_unidad:
                                                cursorlocal.execute('DELETE FROM web_unidades WHERE id=%s', (idUsuario,))
                                                connlocal.commit()
                                            else:
                                                banderaUnidad=False
                            except Exception as e:
                                print(f"{e} - fallo total unidades")
                                banderaUnidad=False
                            if banderaUnidad:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        elif tablaCambiada == 'Horarios':
                            try:
                                try:
                                    banderaHorario=True
                                    request_json_horarios = requests.get(url=f'{URL_API}obtenerhorariosindividualapi/{CONTRATO}/{idUsuario}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                                            
                                    horariosServidor=[]
                                    for consultajson in request_json_horarios:
                                        if consultajson['entrada'] and consultajson['salida']:
                                            entradaObjetohora=time.fromisoformat(consultajson['entrada'])
                                            salidaObjetohora=time.fromisoformat(consultajson['salida'])
                                        else:
                                            entradaObjetohora=None
                                            salidaObjetohora=None
                                        if consultajson['fecha_entrada'] and consultajson['fecha_salida']:
                                            entradaObjetofecha= date.fromisoformat(consultajson['fecha_entrada'])
                                            salidaObjetofecha= date.fromisoformat(consultajson['fecha_salida'])
                                        else:
                                            entradaObjetofecha=None
                                            salidaObjetofecha=None
                                        
                                        TuplaHorarioIndividual=(consultajson['id'], consultajson['usuario'],entradaObjetofecha,salidaObjetofecha,entradaObjetohora,salidaObjetohora,consultajson['cedula'],consultajson['dia'],consultajson['acompanantes'])
                                        horariosServidor.append(TuplaHorarioIndividual)
                                    
                                    cursorlocal.execute('SELECT id, usuario, fecha_entrada, fecha_salida, entrada, salida, cedula_id, dia, acompanantes FROM web_horariospermitidos WHERE usuario=%s',(idUsuario,))
                                    horariosLocal= cursorlocal.fetchall()

                                    for horario in horariosServidor:
                                        if not horario in horariosLocal:
                                            horario_id=horario[0]
                                            usuario_id=horario[1]
                                            fecha_entrada=horario[2]
                                            fecha_salida=horario[3]
                                            entrada=horario[4]
                                            salida=horario[5]
                                            cedula=horario[6]
                                            dia=horario[7]
                                            acompanantes=horario[8]
                                            cursorlocal.execute('''INSERT INTO web_horariospermitidos (id, usuario, fecha_entrada, fecha_salida, entrada, salida, cedula_id, dia, acompanantes)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (horario_id, usuario_id, fecha_entrada, fecha_salida, entrada, salida, cedula, dia, acompanantes))
                                            connlocal.commit()

                                    for horariosLocaliterar in horariosLocal:
                                        if not horariosLocaliterar in horariosServidor:
                                            horario_id=horariosLocaliterar[0]
                                            cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s',(horario_id,))
                                            connlocal.commit()
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en horarios")
                                    banderaHorario=False
                            except Exception as e:
                                print(f"{e} - fallo total horarios")
                                banderaHorario=False
                            if banderaHorario:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        elif tablaCambiada == 'Huellas':
                            try:
                                try:
                                    banderaHuella = True
                                    cursorlocal.execute('SELECT cedula FROM web_usuarios WHERE id=%s',(idUsuario,))
                                    usuario_local= cursorlocal.fetchall()
                                    cursorlocal.execute('SELECT template, id_suprema, cedula FROM web_huellas where cedula=%s', (usuario_local[0][0],))
                                    huellas_local= cursorlocal.fetchall()

                                    request_json = requests.get(url=f'{URL_API}obtenerhuellasapi/{usuario_local[0][0]}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

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
                                                        requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=10)
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
                                                        requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                                else:
                                                    for id_suprema_local in ids_suprema_local:
                                                        IdSupremaContador=IdSupremaContador+1
                                                        if not id_suprema_local[0] == IdSupremaContador:
                                                            id_suprema=IdSupremaContador
                                                            if not cedula in listaempleadosseguricel:
                                                                requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                                            break
                                                    if nro_ids_suprema_local == IdSupremaContador:
                                                        id_suprema=IdSupremaContador+1
                                                        if not cedula in listaempleadosseguricel:
                                                            requests.put(url=f'{URL_API}agregaridsupremaportemplateapi/{template}/{id_suprema}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                            id_suprema_hex = (id_suprema).to_bytes(4, byteorder='big').hex()
                                            id_suprema_hex = id_suprema_hex[6:]+id_suprema_hex[4:6]+id_suprema_hex[2:4]+id_suprema_hex[0:2]
                                            for captahuella in captahuellas:
                                                if captahuella:
                                                    captahuella_actual=captahuella_actual+1
                                                    try:
                                                        requests.get(url=f'{captahuella}/anadir/{id_suprema_hex}/{template}0A', timeout=10)
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
                                                        requests.get(url=f'{captahuella}/quitar/{id_suprema_hex}', timeout=10)
                                                    except:
                                                        print(f"fallo al conectar con la esp8266 con la ip:{captahuella}")
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en huellas")
                                    banderaHuella=False
                            except Exception as e:
                                print(f"{e} - fallo total huellas")
                                banderaHuella=False
                            if banderaHuella:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        elif tablaCambiada == 'Tags':
                            try:
                                try:
                                    banderaTag=True
                                    cursorlocal.execute('SELECT cedula FROM web_usuarios WHERE id=%s',(idUsuario,))
                                    usuario_local= cursorlocal.fetchall()
                                    if usuario_local:
                                        cursorlocal.execute('SELECT epc, cedula FROM web_tagsrfid WHERE cedula=%s', (usuario_local[0][0],))
                                        tags_local= cursorlocal.fetchall()
                                        
                                        request_json = requests.get(url=f'{URL_API}obtenertagsrfidindividualapi/{CONTRATO}/{usuario_local[0][0]}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
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
                                    else:
                                        requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                except requests.exceptions.ConnectionError:
                                    print("fallo consultando api en tags")
                                    banderaTag=False
                            except Exception as e:
                                print(f"{e} - fallo total tags")
                                banderaTag=False
                            if banderaTag:
                                requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        else:
                            requests.delete(url=f'{URL_API}eliminarcambioapi/{idCambio}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                    t1_cambios=tm.perf_counter()
                except Exception as e:
                    print(f"{e} - fallo en api para obtener cambios")

            
            
            if total_log > TIEMPO_LOG:
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
                        cursorlocal.execute('DELETE FROM web_logs_usuarios *')
                        cursorlocal.execute('DELETE FROM dias_acumulados *')
                        connlocal.commit()
                        
                    if not tupla_fecha_hoy in dias_acumulados:
                        cursorlocal.execute('''INSERT INTO dias_acumulados (fecha)
                        VALUES (%s);''', (fechahoy,))
                        connlocal.commit()

                try:
                    cursorlocal.execute('SELECT * FROM web_logs_usuarios where contrato=%s and fecha=%s', (CONTRATO,fechahoy))
                    logsUsuarios_local= cursorlocal.fetchall()
                
                    request_json = requests.get(url=f'{URL_API}obtenerlogsusuariosapi/{CONTRATO}/{fechahoy}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                    listaLogsServidor=[]
                    for consultajson in request_json:
                        objetofecha= date.fromisoformat(consultajson['fecha'])
                        objetohora=time.fromisoformat(consultajson['hora'])
                        tuplaLogIndividual=(consultajson['nombre'],objetofecha,objetohora,consultajson['razon'],consultajson['contrato'],consultajson['cedula'])
                        listaLogsServidor.append(tuplaLogIndividual)

                    nro_int_local = len(logsUsuarios_local)
                    nro_int_servidor = len(listaLogsServidor)

                    if nro_int_local != nro_int_servidor:

                        for interaccion in logsUsuarios_local:
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
                                requests.post(url=f'{URL_API}registrarlogsusuariosapi/', 
                                json=anadirLogJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                except Exception as e:
                    print(f"{e} - fallo total en Log de usuarios")
            

                try:
                    cursorlocal.execute('SELECT vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, razon, personas FROM web_logs_vigilantes where contrato=%s and fecha=%s', (CONTRATO, fechahoy))
                    logsVigilantes_local= cursorlocal.fetchall()
                    
                    request_json = requests.get(url=f'{URL_API}obtenerlogsvigilantesapi/{CONTRATO}/{fechahoy}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                    listaLogsVigilantesServidor=[]
                    for consultajson in request_json:
                        objetofecha= date.fromisoformat(consultajson['fecha'])
                        objetohora=time.fromisoformat(consultajson['hora'])
                        tuplaLogIndividual=(consultajson['vigilante_id'],consultajson['vigilante_nombre'],consultajson['unidad_id'],consultajson['unidad_nombre'],objetofecha,objetohora,consultajson['razon'], consultajson['personas'])
                        listaLogsVigilantesServidor.append(tuplaLogIndividual)

                    nro_int_local = len(logsVigilantes_local)
                    nro_log_vig_servidor = len(listaLogsVigilantesServidor)

                    if nro_int_local != nro_log_vig_servidor:

                        for logVigilante in logsVigilantes_local:
                            if not logVigilante in listaLogsVigilantesServidor:
                                vigilante_id=logVigilante[0]
                                vigilante_nombre=logVigilante[1]
                                unidad_id=logVigilante[2]
                                unidad_nombre=logVigilante[3]
                                fecha=logVigilante[4]
                                hora=logVigilante[5]
                                razon=logVigilante[6]
                                personas=logVigilante[7]
                                anadirLogJson = {
                                    "vigilante_nombre": vigilante_nombre,
                                    "vigilante_id": vigilante_id,
                                    "unidad_id": unidad_id,
                                    "unidad_nombre": unidad_nombre,
                                    "fecha": fecha.isoformat(),
                                    "hora": hora.isoformat(),
                                    "razon": razon,
                                    "contrato": CONTRATO,
                                    "personas": personas,
                                }
                                requests.post(url=f'{URL_API}registrarlogsvigilantesapi/', 
                                json=anadirLogJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                except Exception as e:
                    print(f"{e} - fallo total en Log de vigilantes")

                try:
                    cursorlocal.execute('SELECT vigilante_id, vigilante_nombre, nombre, fecha, hora, razon, cedula_id, acompanantes, cedula_propietario, unidad_id FROM web_logs_visitantes where contrato=%s and fecha=%s', (CONTRATO, fechahoy))
                    logsVisitantes_local= cursorlocal.fetchall()
                    
                    request_json = requests.get(url=f'{URL_API}obtenerlogsvisitantesapi/{CONTRATO}/{fechahoy}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                    # print(request_json)
                    listaLogsVisitantesServidor=[]
                    for consultajson in request_json:
                        objetofecha= date.fromisoformat(consultajson['fecha'])
                        objetohora=time.fromisoformat(consultajson['hora'])
                        tuplaLogIndividual=(consultajson['vigilante_id'],consultajson['vigilante_nombre'],consultajson['nombre'],objetofecha,objetohora,consultajson['razon'],consultajson['cedula'], consultajson['acompanantes'],consultajson['cedula_propietario'],consultajson['unidad_id'])
                        listaLogsVisitantesServidor.append(tuplaLogIndividual)

                    nro_int_local = len(logsVisitantes_local)
                    nro_log_vig_servidor = len(listaLogsVisitantesServidor)
                    # print(nro_int_local)
                    # print(nro_log_vig_servidor)
                    # print("Lista local")
                    # print(logsVisitantes_local)
                    # print("lista servidor")
                    # print(listaLogsVisitantesServidor)
                    if nro_int_local != nro_log_vig_servidor:

                        for logVisitante in logsVisitantes_local:
                            if not logVisitante in listaLogsVisitantesServidor:
                                # print(logVisitante)
                                vigilante_id=logVisitante[0]
                                vigilante_nombre=logVisitante[1]
                                nombre=logVisitante[2]
                                fecha=logVisitante[3]
                                hora=logVisitante[4]
                                razon=logVisitante[5]
                                cedula=logVisitante[6]
                                acompanantes=logVisitante[7]
                                cedula_propietario=logVisitante[8]
                                unidad_id=logVisitante[9]
                                anadirLogJson = {
                                    "vigilante_nombre": vigilante_nombre,
                                    "vigilante_id": vigilante_id,
                                    "nombre": nombre,
                                    "fecha": fecha.isoformat(),
                                    "hora": hora.isoformat(),
                                    "razon": razon,
                                    "contrato": CONTRATO,
                                    "cedula": cedula,
                                    "acompanantes": acompanantes,
                                    "cedula_propietario": "" if (cedula_propietario==None) else cedula_propietario,
                                    "unidad_id":unidad_id
                                }
                                requests.post(url=f'{URL_API}registrarlogsvisitantesapi/', 
                                json=anadirLogJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                # print(peticion.status_code)
                except Exception as e:
                    print(f"{e} - fallo total en Log de visitantes")

                BorrarPeticionesListas=True
                AccesosSinCerrar=True
                borrarHorariosVisitantes=True
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
                                        request_json = requests.delete(url=f'{URL_API}eliminarsolicitudesaperturaapi/{idapertura}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
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
                listaAccesosAbiertos=[]
                try:
                    cursorlocal.execute('SELECT cedula, acceso, fecha, hora, estado FROM accesos_abiertos')
                    accesosAbiertos = cursorlocal.fetchall()

                    comprobarAccesos = requests.get(url=f'{URL_API}eliminarpuertaabiertaapi/{CONTRATO}/blank/blank/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                    accesoAbiertosServidor=[]
                    for consultajson in comprobarAccesos:
                        tuplaAccesoAbiertoIndividual=(consultajson['cedula'],consultajson['acceso'])
                        accesoAbiertosServidor.append(tuplaAccesoAbiertoIndividual)
                    
                    if accesosAbiertos:
                        for acceso_abierto in accesosAbiertos:
                            cedula=acceso_abierto[0]
                            accesoo=acceso_abierto[1]
                            AccesoAbiertoLocal=(cedula,accesoo)
                            estado=acceso_abierto[4]
                            if estado:
                                try:
                                    # fecha=acceso_abierto[2]
                                    # hora=acceso_abierto[3]
                                    requests.delete(url=f'{URL_API}eliminarpuertaabiertaapi/{CONTRATO}/{cedula}/{accesoo}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                    cursorlocal.execute('DELETE FROM accesos_abiertos WHERE cedula=%s AND acceso=%s', (cedula, accesoo))
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
                                        # comprobarAccesos = requests.get(url=f'{URL_API}eliminarpuertaabiertaapi/{CONTRATO}/{cedula}/{accesoo}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()
                                        if not AccesoAbiertoLocal in accesoAbiertosServidor:
                                            # cedula=acceso_abierto[0]
                                            # accesoo=acceso_abierto[1]
                                            if not cedula in listaAccesosAbiertos and not accesoo in listaAccesosAbiertos:
                                                anadirJson = {
                                                    "contrato": CONTRATO,
                                                    "cedula": cedula,
                                                    "acceso": accesoo,
                                                    "fecha": fecha_apertura,
                                                    "hora": apertura_hora_completa
                                                    }
                                                requests.post(url=f'{URL_API}agregarpuertaabiertaapi/', 
                                                json=anadirJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                                #print("La puerta ha permanecido demasiado tiempo abierta!")
                                                listaAccesosAbiertos.append(cedula)
                                                listaAccesosAbiertos.append(accesoo)
                                    except Exception as e:
                                        print(f"{e} - fallo total agregando puerta abierta del acceso:{accesoo}")    
                except Exception as e:
                    print(f"{e} - fallo total manejando los accesos sin cerrar")
                AccesosSinCerrar=False
            
            if borrarHorariosVisitantes:

                cursorlocal.execute('SELECT a.id, a.usuario, a.fecha_salida, a.salida, b.cedula_propietario, c.aperturas_hechas FROM web_horariospermitidos AS a INNER JOIN web_usuarios AS b ON a.usuario = b.id LEFT JOIN control_horarios_visitantes AS c ON c.horario_id=a.id WHERE dia is NULL')
                horarios = cursorlocal.fetchall()
                for horario in horarios:
                    if horario[5]!=None:
                        if horario[5]>=2 and horario[4]!=None:
                            try:
                                request_json = requests.delete(url=f'{URL_API}editarhorariosvisitantesapi/{horario[0]}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                if request_json.status_code == 204 or request_json.status_code == 500:
                                    cursorlocal.execute('DELETE FROM control_horarios_visitantes WHERE horario_id=%s', (horario[0],))
                                    cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                    connlocal.commit() 
                            except Exception as e:
                                print(f"{e} - fallo total eliminando horario:{horario[0]}") 
                        elif horario[5]>=2 and horario[4]==None:
                            try:
                                cursorlocal.execute('DELETE FROM control_horarios_visitantes WHERE horario_id=%s', (horario[0],))
                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                cursorlocal.execute('DELETE FROM web_usuarios WHERE id=%s', (horario[1],))
                                connlocal.commit() 
                            except Exception as e:
                                print(f"{e} - fallo total eliminando horario:{horario[0]}")
                        elif horario[5]<2 and horario[4]!=None:
                            tz = pytz.timezone('America/Caracas')
                            caracas_now = datetime.now(tz)
                            horahoy = caracas_now.time()
                            fechahoy = caracas_now.date()
                            if ((fechahoy==horario[2] and horahoy>=horario[3] and horario[4]!=None) or (fechahoy>horario[2] and horario[4]!=None)):
                                try:
                                    request_json = requests.delete(url=f'{URL_API}editarhorariosvisitantesapi/{horario[0]}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                    if request_json.status_code == 204 or request_json.status_code == 500:
                                        cursorlocal.execute('DELETE FROM control_horarios_visitantes WHERE horario_id=%s', (horario[0],))
                                        cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                        connlocal.commit() 
                                except Exception as e:
                                    print(f"{e} - fallo total eliminando horario:{horario[0]}") 
                        elif horario[5]<2 and horario[4]==None:
                            tz = pytz.timezone('America/Caracas')
                            caracas_now = datetime.now(tz)
                            horahoy = caracas_now.time()
                            fechahoy = caracas_now.date()
                            if ((fechahoy==horario[2] and horahoy>=horario[3] and horario[4]==None) or (fechahoy>horario[2] and horario[4]==None)):
                                try:
                                    cursorlocal.execute('DELETE FROM control_horarios_visitantes WHERE horario_id=%s', (horario[0],))
                                    cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                    cursorlocal.execute('DELETE FROM web_usuarios WHERE id=%s', (horario[1],))
                                    connlocal.commit() 
                                except Exception as e:
                                    print(f"{e} - fallo total eliminando horario:{horario[0]}")
                    else:
                        tz = pytz.timezone('America/Caracas')
                        caracas_now = datetime.now(tz)
                        horahoy = caracas_now.time()
                        fechahoy = caracas_now.date()
                        if ((fechahoy==horario[2] and horahoy>=horario[3] and horario[4]!=None) or (fechahoy>horario[2] and horario[4]!=None)):
                            try:
                                request_json = requests.delete(url=f'{URL_API}editarhorariosvisitantesapi/{horario[0]}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                                if request_json.status_code == 204 or request_json.status_code == 500:
                                    cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                    connlocal.commit() 
                            except Exception as e:
                                print(f"{e} - fallo total eliminando horario:{horario[0]}") 
                        elif ((fechahoy==horario[2] and horahoy>=horario[3] and horario[4]==None) or (fechahoy>horario[2] and horario[4]==None)):
                            try:
                                cursorlocal.execute('DELETE FROM web_horariospermitidos WHERE id=%s', (horario[0],))
                                cursorlocal.execute('DELETE FROM web_usuarios WHERE id=%s', (horario[1],))
                                connlocal.commit() 
                            except Exception as e:
                                print(f"{e} - fallo total eliminando horario:{horario[0]}")
                borrarHorariosVisitantes=False

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
            
