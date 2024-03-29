import psycopg2
import os
import time as tm
import pytz
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import requests

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)
CONTRATO=os.environ.get("CONTRATO")
CONTRATO_ID=os.environ.get("CONTRATO_ID")
URL_API=os.environ.get("URL_API")
TEMP_DIRECTORY=os.environ.get("TEMP_DIRECTORY")
connlocal = None
connheroku = None
cursorheroku=None
cursorlocal=None
total=0

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
        
        while True:
            try:
                try:
                    cursorlocal.execute('SELECT dispositivo, descripcion, estado, acceso, minor_id FROM web_dispositivos')
                    dispositivos_local= cursorlocal.fetchall()

                    request_json = requests.get(url=f'{URL_API}obtenerdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10).json()

                    dispositivosServidor=[]
                    for consultajson in request_json:
                        tuplaDispositivoIndividual=(consultajson['dispositivo'],consultajson['descripcion'], consultajson['estado'], consultajson['acceso'] if (consultajson['acceso']!=None) else "", consultajson['minor_id'],)
                        dispositivosServidor.append(tuplaDispositivoIndividual)

                    if len(dispositivosServidor) != len(dispositivos_local):
                        request_json = requests.delete(url=f'{URL_API}eliminartodosdispositivosapi/{CONTRATO}/', auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                        dispositivosServidor=[]
                        if request_json.status_code == 200:

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
                                    descripcion=dispositivolocal[1]
                                    estado=dispositivolocal[2]
                                    acceso=dispositivolocal[3]
                                    
                                    if descripcion=="SERVIDOR LOCAL":
                                        with open(TEMP_DIRECTORY) as f:
                                            temp = f.read()
                                            temp=temp[:2]
                                            minor_id=temp
                                            cursorlocal.execute('UPDATE web_dispositivos SET minor_id=%s WHERE dispositivo=%s', (minor_id, dispositivo))
                                            connlocal.commit()
                                    else:
                                        minor_id=dispositivolocal[4]

                                    agregarDispositivoJson = {
                                        "dispositivo": dispositivo,
                                        "descripcion": descripcion,
                                        "estado": estado,
                                        "contrato": CONTRATO_ID,
                                        "acceso": acceso,
                                        "fecha": fecha,
                                        "hora": hora,
                                        "minor_id": minor_id
                                    }
                                    requests.post(url=f'{URL_API}registrardispositivosapi/', 
                                    json=agregarDispositivoJson, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
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
                                descripcion=dispositivolocal[1]
                                estado=dispositivolocal[2]
                                if descripcion=="SERVIDOR LOCAL":
                                    # se usa la columna destinada al minor_id para guardar
                                    # la temperatura del servidor local
                                    with open(TEMP_DIRECTORY) as f:
                                        temp = f.read()
                                        temp=temp[:2]
                                        cursorlocal.execute('UPDATE web_dispositivos SET minor_id=%s WHERE dispositivo=%s', (temp, dispositivo))
                                        connlocal.commit()
                                    jsonActualizarDispositivo= {
                                        "contrato": CONTRATO_ID,
                                        "dispositivo": dispositivo,
                                        "descripcion": descripcion,
                                        "estado": estado,
                                        "fecha": fecha,
                                        "hora": hora,
                                        "minor_id": temp
                                    }
                                else:
                                    jsonActualizarDispositivo= {
                                        "contrato": CONTRATO_ID,
                                        "dispositivo": dispositivo,
                                        "descripcion": descripcion,
                                        "estado": estado,
                                        "fecha": fecha,
                                        "hora": hora
                                    }
                                requests.put(url=f'{URL_API}actualizardispositivosapi/{CONTRATO}/{dispositivo[7:]}/{estado}/',
                                json=jsonActualizarDispositivo, auth=('BaseLocal_access', 'S3gur1c3l_local@'), timeout=10)
                except requests.exceptions.ConnectionError:
                    print("fallo consultando api de dispositivos")   
            except Exception as e:
                print(f"{e} - fallo total en los dispositivos")  
    
    except (Exception, psycopg2.Error) as error:
        print(f"{error} - fallo en hacer las consultas de base de datos de dispositivos")
        print("se ha cerrado la conexion a la base de datos")
        if connlocal:
            cursorlocal.close()
            connlocal.close()
