import psycopg2
import os
import time
from dotenv import load_dotenv
from pathlib import Path
import random

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

descripcion_captahuella1=os.environ.get('RAZON_CAPTAHUELLA1')
descripcion_captahuella2=os.environ.get('RAZON_CAPTAHUELLA2')
descripcion_captahuella3=os.environ.get('RAZON_CAPTAHUELLA3')
descripcion_captahuella4=os.environ.get('RAZON_CAPTAHUELLA4')
descripcion_captahuella5=os.environ.get('RAZON_CAPTAHUELLA5')
descripcion_captahuella6=os.environ.get('RAZON_CAPTAHUELLA6')
descripcion_captahuella7=os.environ.get('RAZON_CAPTAHUELLA7')
descripcion_captahuella8=os.environ.get('RAZON_CAPTAHUELLA8')
descripcion_captahuella9=os.environ.get('RAZON_CAPTAHUELLA9')
descripcion_captahuella10=os.environ.get('RAZON_CAPTAHUELLA10')
descripcion_captahuella11=os.environ.get('RAZON_CAPTAHUELLA11')
descripcion_captahuella12=os.environ.get('RAZON_CAPTAHUELLA12')
descripcion_captahuella13=os.environ.get('RAZON_CAPTAHUELLA13')
descripcion_captahuella14=os.environ.get('RAZON_CAPTAHUELLA14')
descripcion_captahuella15=os.environ.get('RAZON_CAPTAHUELLA15')
descripcion_captahuella16=os.environ.get('RAZON_CAPTAHUELLA16')
descripcion_captahuella17=os.environ.get('RAZON_CAPTAHUELLA17')
descripcion_captahuella18=os.environ.get('RAZON_CAPTAHUELLA18')
descripcion_captahuella19=os.environ.get('RAZON_CAPTAHUELLA19')
descripcion_captahuella20=os.environ.get('RAZON_CAPTAHUELLA20')

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

descripcion_rfid1=os.environ.get('RAZON_RFID1')
descripcion_rfid2=os.environ.get('RAZON_RFID2')
descripcion_rfid3=os.environ.get('RAZON_RFID3')
descripcion_rfid4=os.environ.get('RAZON_RFID4')
descripcion_rfid5=os.environ.get('RAZON_RFID5')
descripcion_rfid6=os.environ.get('RAZON_RFID6')
descripcion_rfid7=os.environ.get('RAZON_RFID7')
descripcion_rfid8=os.environ.get('RAZON_RFID8')
descripcion_rfid9=os.environ.get('RAZON_RFID9')
descripcion_rfid10=os.environ.get('RAZON_RFID10')
descripcion_rfid11=os.environ.get('RAZON_RFID11')
descripcion_rfid12=os.environ.get('RAZON_RFID12')
descripcion_rfid13=os.environ.get('RAZON_RFID13')
descripcion_rfid14=os.environ.get('RAZON_RFID14')
descripcion_rfid15=os.environ.get('RAZON_RFID15')
descripcion_rfid16=os.environ.get('RAZON_RFID16')
descripcion_rfid17=os.environ.get('RAZON_RFID17')
descripcion_rfid18=os.environ.get('RAZON_RFID18')
descripcion_rfid19=os.environ.get('RAZON_RFID19')
descripcion_rfid20=os.environ.get('RAZON_RFID20')

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

descripcion_bluetooth1=os.environ.get('RAZON_BLUETOOTH1')
descripcion_bluetooth2=os.environ.get('RAZON_BLUETOOTH2')
descripcion_bluetooth3=os.environ.get('RAZON_BLUETOOTH3')
descripcion_bluetooth4=os.environ.get('RAZON_BLUETOOTH4')
descripcion_bluetooth5=os.environ.get('RAZON_BLUETOOTH5')
descripcion_bluetooth6=os.environ.get('RAZON_BLUETOOTH6')
descripcion_bluetooth7=os.environ.get('RAZON_BLUETOOTH7')
descripcion_bluetooth8=os.environ.get('RAZON_BLUETOOTH8')
descripcion_bluetooth9=os.environ.get('RAZON_BLUETOOTH9')
descripcion_bluetooth10=os.environ.get('RAZON_BLUETOOTH10')
descripcion_bluetooth11=os.environ.get('RAZON_BLUETOOTH11')
descripcion_bluetooth12=os.environ.get('RAZON_BLUETOOTH12')
descripcion_bluetooth13=os.environ.get('RAZON_BLUETOOTH13')
descripcion_bluetooth14=os.environ.get('RAZON_BLUETOOTH14')
descripcion_bluetooth15=os.environ.get('RAZON_BLUETOOTH15')
descripcion_bluetooth16=os.environ.get('RAZON_BLUETOOTH16')
descripcion_bluetooth17=os.environ.get('RAZON_BLUETOOTH17')
descripcion_bluetooth18=os.environ.get('RAZON_BLUETOOTH18')
descripcion_bluetooth19=os.environ.get('RAZON_BLUETOOTH19')
descripcion_bluetooth20=os.environ.get('RAZON_BLUETOOTH20')

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

descripcion_rele1=os.environ.get('RAZON_RELE1')
descripcion_rele2=os.environ.get('RAZON_RELE2')
descripcion_rele3=os.environ.get('RAZON_RELE3')
descripcion_rele4=os.environ.get('RAZON_RELE4')
descripcion_rele5=os.environ.get('RAZON_RELE5')
descripcion_rele6=os.environ.get('RAZON_RELE6')
descripcion_rele7=os.environ.get('RAZON_RELE7')
descripcion_rele8=os.environ.get('RAZON_RELE8')
descripcion_rele9=os.environ.get('RAZON_RELE9')
descripcion_rele10=os.environ.get('RAZON_RELE10')
descripcion_rele11=os.environ.get('RAZON_RELE11')
descripcion_rele12=os.environ.get('RAZON_RELE12')
descripcion_rele13=os.environ.get('RAZON_RELE13')
descripcion_rele14=os.environ.get('RAZON_RELE14')
descripcion_rele15=os.environ.get('RAZON_RELE15')
descripcion_rele16=os.environ.get('RAZON_RELE16')
descripcion_rele17=os.environ.get('RAZON_RELE17')
descripcion_rele18=os.environ.get('RAZON_RELE18')
descripcion_rele19=os.environ.get('RAZON_RELE19')
descripcion_rele20=os.environ.get('RAZON_RELE20')

######################################
#############MINOR IDs################
#######################################
minorid_acceso1=os.environ.get('MINORID_ACCESO1')
minorid_acceso2=os.environ.get('MINORID_ACCESO2')
minorid_acceso3=os.environ.get('MINORID_ACCESO3')
minorid_acceso4=os.environ.get('MINORID_ACCESO4')
minorid_acceso5=os.environ.get('MINORID_ACCESO5')
minorid_acceso6=os.environ.get('MINORID_ACCESO6')
minorid_acceso7=os.environ.get('MINORID_ACCESO7')
minorid_acceso8=os.environ.get('MINORID_ACCESO8')
minorid_acceso9=os.environ.get('MINORID_ACCESO9')
minorid_acceso10=os.environ.get('MINORID_ACCESO10')
minorid_acceso11=os.environ.get('MINORID_ACCESO11')
minorid_acceso12=os.environ.get('MINORID_ACCESO12')
minorid_acceso13=os.environ.get('MINORID_ACCESO13')
minorid_acceso14=os.environ.get('MINORID_ACCESO14')
minorid_acceso15=os.environ.get('MINORID_ACCESO15')
minorid_acceso16=os.environ.get('MINORID_ACCESO16')
minorid_acceso17=os.environ.get('MINORID_ACCESO17')
minorid_acceso18=os.environ.get('MINORID_ACCESO18')
minorid_acceso19=os.environ.get('MINORID_ACCESO19')
minorid_acceso20=os.environ.get('MINORID_ACCESO20')

dispositivos=[captahuella1, captahuella2, captahuella3, captahuella4, captahuella5,
              captahuella6, captahuella7, captahuella8, captahuella9, captahuella10,
              captahuella11, captahuella12, captahuella3, captahuella14, captahuella15,
              captahuella16, captahuella17, captahuella18, captahuella19, captahuella20,
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
              SERVIDOR_LOCAL
             ]

dispositivos_dict= {captahuella1:descripcion_captahuella1, 
                    captahuella2:descripcion_captahuella2, 
                    captahuella3:descripcion_captahuella3, 
                    captahuella4:descripcion_captahuella4, 
                    captahuella5:descripcion_captahuella5,
                    captahuella6:descripcion_captahuella6, 
                    captahuella7:descripcion_captahuella7, 
                    captahuella8:descripcion_captahuella8, 
                    captahuella9:descripcion_captahuella9, 
                    captahuella10:descripcion_captahuella10,
                    captahuella11:descripcion_captahuella11, 
                    captahuella12:descripcion_captahuella12, 
                    captahuella13:descripcion_captahuella13, 
                    captahuella14:descripcion_captahuella14, 
                    captahuella15:descripcion_captahuella15,
                    captahuella16:descripcion_captahuella16, 
                    captahuella17:descripcion_captahuella17, 
                    captahuella18:descripcion_captahuella18, 
                    captahuella19:descripcion_captahuella19, 
                    captahuella20:descripcion_captahuella20,
                    rfid1:descripcion_rfid1, 
                    rfid2:descripcion_rfid2,
                    rfid3:descripcion_rfid3,
                    rfid4:descripcion_rfid4,
                    rfid5:descripcion_rfid5,
                    rfid6:descripcion_rfid6, 
                    rfid7:descripcion_rfid7,
                    rfid8:descripcion_rfid8,
                    rfid9:descripcion_rfid9,
                    rfid10:descripcion_rfid10,
                    rfid11:descripcion_rfid11, 
                    rfid12:descripcion_rfid12,
                    rfid13:descripcion_rfid13,
                    rfid14:descripcion_rfid14,
                    rfid15:descripcion_rfid15,
                    rfid16:descripcion_rfid16, 
                    rfid17:descripcion_rfid17,
                    rfid18:descripcion_rfid18,
                    rfid19:descripcion_rfid19,
                    rfid20:descripcion_rfid20,
                    bluetooth1:descripcion_bluetooth1, 
                    bluetooth2:descripcion_bluetooth2,
                    bluetooth3:descripcion_bluetooth3,
                    bluetooth4:descripcion_bluetooth4,
                    bluetooth5:descripcion_bluetooth5,
                    bluetooth6:descripcion_bluetooth6, 
                    bluetooth7:descripcion_bluetooth7,
                    bluetooth8:descripcion_bluetooth8,
                    bluetooth9:descripcion_bluetooth9,
                    bluetooth10:descripcion_bluetooth10,
                    bluetooth11:descripcion_bluetooth11, 
                    bluetooth12:descripcion_bluetooth12,
                    bluetooth13:descripcion_bluetooth13,
                    bluetooth14:descripcion_bluetooth14,
                    bluetooth15:descripcion_bluetooth15,
                    bluetooth16:descripcion_bluetooth16, 
                    bluetooth17:descripcion_bluetooth17,
                    bluetooth18:descripcion_bluetooth18,
                    bluetooth19:descripcion_bluetooth19,
                    bluetooth20:descripcion_bluetooth20,
                    rele1:descripcion_rele1, 
                    rele2:descripcion_rele2,
                    rele3:descripcion_rele3,
                    rele4:descripcion_rele4,
                    rele5:descripcion_rele5,
                    rele6:descripcion_rele6, 
                    rele7:descripcion_rele7,
                    rele8:descripcion_rele8,
                    rele9:descripcion_rele9,
                    rele10:descripcion_rele10,
                    rele11:descripcion_rele11, 
                    rele12:descripcion_rele12,
                    rele13:descripcion_rele13,
                    rele14:descripcion_rele14,
                    rele15:descripcion_rele15,
                    rele16:descripcion_rele16, 
                    rele17:descripcion_rele17,
                    rele18:descripcion_rele18,
                    rele19:descripcion_rele19,
                    rele20:descripcion_rele20,
                    SERVIDOR_LOCAL:'SERVIDOR LOCAL'
                    }

accesos_dispositivos=[acceso1, acceso2, acceso3, acceso4,
                      acceso5, acceso6, acceso7, acceso8,
                      acceso9, acceso10, acceso11, acceso12,
                      acceso13, acceso14, acceso15, acceso16,
                      acceso17, acceso18, acceso19, acceso20]

accesos_dispositivos_dict ={acceso1:descripcion_acceso1, 
                            acceso2:descripcion_acceso2, 
                            acceso3:descripcion_acceso3, 
                            acceso4:descripcion_acceso4,
                            acceso5:descripcion_acceso5, 
                            acceso6:descripcion_acceso6, 
                            acceso7:descripcion_acceso7, 
                            acceso8:descripcion_acceso8,
                            acceso9:descripcion_acceso9, 
                            acceso10:descripcion_acceso10, 
                            acceso11:descripcion_acceso11, 
                            acceso12:descripcion_acceso12,
                            acceso13:descripcion_acceso13, 
                            acceso14:descripcion_acceso14, 
                            acceso15:descripcion_acceso15, 
                            acceso16:descripcion_acceso16,
                            acceso17:descripcion_acceso17, 
                            acceso18:descripcion_acceso18, 
                            acceso19:descripcion_acceso19, 
                            acceso20:descripcion_acceso20
                            }

accesos_minorid_dict ={acceso1:minorid_acceso1, 
                            acceso2:minorid_acceso2, 
                            acceso3:minorid_acceso3, 
                            acceso4:minorid_acceso4,
                            acceso5:minorid_acceso5, 
                            acceso6:minorid_acceso6, 
                            acceso7:minorid_acceso7, 
                            acceso8:minorid_acceso8,
                            acceso9:minorid_acceso9, 
                            acceso10:minorid_acceso10, 
                            acceso11:minorid_acceso11, 
                            acceso12:minorid_acceso12,
                            acceso13:minorid_acceso13, 
                            acceso14:minorid_acceso14, 
                            acceso15:minorid_acceso15, 
                            acceso16:minorid_acceso16,
                            acceso17:minorid_acceso17, 
                            acceso18:minorid_acceso18, 
                            acceso19:minorid_acceso19, 
                            acceso20:minorid_acceso20
                            }

accesos_dict = {acceso1:"1", 
                acceso2:"2", 
                acceso3:"3", 
                acceso4:"4",
                acceso5:"5", 
                acceso6:"6", 
                acceso7:"7", 
                acceso8:"8",
                acceso9:"9", 
                acceso10:"10", 
                acceso11:"11", 
                acceso12:"12",
                acceso13:"13", 
                acceso14:"14", 
                acceso15:"15", 
                acceso16:"16",
                acceso17:"17", 
                acceso18:"18", 
                acceso19:"19", 
                acceso20:"20"
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

        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_usuarios (id integer, rol varchar, cedula varchar(150), nombre varchar(255), telegram_id varchar(150), numero_telefonico varchar(150), cedula_propietario varchar(150), unidad_id integer, entrada_beacon_uuid varchar(150), salida_beacon_uuid varchar(150), internet boolean, wifi boolean, bluetooth boolean, captahuella boolean, rfid boolean, facial boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_logs_usuarios (nombre varchar(255), fecha date, hora time without time zone, razon varchar(150), contrato text, cedula_id varchar(150), subido boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_logs_vigilantes (vigilante_id integer, vigilante_nombre varchar(150), unidad_id integer, unidad_nombre varchar(150), fecha date, hora time without time zone, razon varchar(150), contrato text, personas integer, subido boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_logs_visitantes (vigilante_id integer, vigilante_nombre varchar(150), nombre varchar(255), fecha date, hora time without time zone, razon varchar(150), contrato text, cedula_id varchar(150), acompanantes integer, cedula_propietario varchar(150), unidad_id integer, subido boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_logs_incidentes (vigilante_id integer, vigilante_nombre varchar(150), fecha date, hora time without time zone, contrato text, tipo_incidente varchar(150), clasificacion_incidente varchar(150), descripcion varchar(150), comentario text, subido boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_horariospermitidos (id integer, usuario integer, fecha_entrada date, fecha_salida date, entrada time without time zone, salida time without time zone, cedula_id varchar(150), dia varchar(180), acompanantes integer)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS dias_acumulados (fecha varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_dispositivos (dispositivo varchar(150), descripcion varchar(150), estado varchar(150), acceso varchar(150), minor_id integer)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_huellas (id_suprema integer, cedula varchar(150), template text)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_tagsrfid (epc text, cedula varchar(150))')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS solicitud_aperturas (id integer, id_usuario varchar(150), acceso varchar(150), razon varchar(150), estado integer, peticionInternet boolean, feedback boolean, abriendo boolean, fecha date, hora time without time zone)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS accesos_abiertos (cedula varchar(150), acceso varchar(150), fecha date, hora time without time zone, estado boolean)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS control_horarios_visitantes (horario_id integer, aperturas_hechas integer)')
        cursorlocal.execute('CREATE TABLE IF NOT EXISTS web_unidades (id integer, nombre varchar(250), codigo integer)')
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
                    cursorlocal.execute('INSERT INTO web_dispositivos (dispositivo, descripcion, estado, acceso) values(%s, %s, %s, %s)',(dispositivo, descripcion, estado, ""))
                    connlocal.commit()
            
            for dispositivoAcceso in accesos_dispositivos:
                if dispositivoAcceso:
                    descripcion = accesos_dispositivos_dict[dispositivoAcceso]
                    acceso = accesos_dict[dispositivoAcceso]
                    estado = '0'
                    minor_id_existente=accesos_minorid_dict[dispositivoAcceso]
                    if minor_id_existente:
                        cursorlocal.execute('INSERT INTO web_dispositivos (dispositivo, descripcion, estado, acceso, minor_id) values(%s, %s, %s, %s, %s)',(dispositivoAcceso, descripcion, estado, acceso, minor_id_existente))
                        connlocal.commit()
                    else:
                        minor_id=random.randint(1, 65535)
                        cursorlocal.execute('INSERT INTO web_dispositivos (dispositivo, descripcion, estado, acceso, minor_id) values(%s, %s, %s, %s, %s)',(dispositivoAcceso, descripcion, estado, acceso, minor_id))
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
    
