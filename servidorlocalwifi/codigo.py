from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import psycopg2
import os
import pytz
from datetime import datetime
import requests
from dotenv import load_dotenv
from pathlib import Path
import json

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)
URL_API = os.environ.get("URL_API")
NUMERO_BOT = os.environ.get("NUMERO_BOT")
APIKEY_BOT = os.environ.get("APIKEY_BOT")
hostName = '0.0.0.0'
serverPort = 43157
conn = None
cursor = None
dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
ultimahora = datetime.strptime('23:59:59', '%H:%M:%S').time()
primerahora = datetime.strptime('00:00:00', '%H:%M:%S').time()
total=0
CONTRATO=os.environ.get("CONTRATO")

razon1=os.environ.get("RAZON_TELEFONO1")
razon2=os.environ.get("RAZON_TELEFONO2")
razon3=os.environ.get("RAZON_TELEFONO3")
razon4=os.environ.get("RAZON_TELEFONO4")
razon5=os.environ.get("RAZON_TELEFONO5")
razon6=os.environ.get("RAZON_TELEFONO6")
razon7=os.environ.get("RAZON_TELEFONO7")
razon8=os.environ.get("RAZON_TELEFONO8")
razon9=os.environ.get("RAZON_TELEFONO9")
razon10=os.environ.get("RAZON_TELEFONO10")
razon11=os.environ.get("RAZON_TELEFONO11")
razon12=os.environ.get("RAZON_TELEFONO12")
razon13=os.environ.get("RAZON_TELEFONO13")
razon14=os.environ.get("RAZON_TELEFONO14")
razon15=os.environ.get("RAZON_TELEFONO15")
razon16=os.environ.get("RAZON_TELEFONO16")
razon17=os.environ.get("RAZON_TELEFONO17")
razon18=os.environ.get("RAZON_TELEFONO18")
razon19=os.environ.get("RAZON_TELEFONO19")
razon20=os.environ.get("RAZON_TELEFONO20")


razonhuella1=os.environ.get("RAZON_CAPTAHUELLA1")
razonhuella2=os.environ.get("RAZON_CAPTAHUELLA2")
razonhuella3=os.environ.get("RAZON_CAPTAHUELLA3")
razonhuella4=os.environ.get("RAZON_CAPTAHUELLA4")
razonhuella5=os.environ.get("RAZON_CAPTAHUELLA5")
razonhuella6=os.environ.get("RAZON_CAPTAHUELLA6")
razonhuella7=os.environ.get("RAZON_CAPTAHUELLA7")
razonhuella8=os.environ.get("RAZON_CAPTAHUELLA8")
razonhuella9=os.environ.get("RAZON_CAPTAHUELLA9")
razonhuella10=os.environ.get("RAZON_CAPTAHUELLA10")
razonhuella11=os.environ.get("RAZON_CAPTAHUELLA11")
razonhuella12=os.environ.get("RAZON_CAPTAHUELLA12")
razonhuella13=os.environ.get("RAZON_CAPTAHUELLA13")
razonhuella14=os.environ.get("RAZON_CAPTAHUELLA14")
razonhuella15=os.environ.get("RAZON_CAPTAHUELLA15")
razonhuella16=os.environ.get("RAZON_CAPTAHUELLA16")
razonhuella17=os.environ.get("RAZON_CAPTAHUELLA17")
razonhuella18=os.environ.get("RAZON_CAPTAHUELLA18")
razonhuella19=os.environ.get("RAZON_CAPTAHUELLA19")
razonhuella20=os.environ.get("RAZON_CAPTAHUELLA20")

razonrfid1=os.environ.get("RAZON_RFID1")
razonrfid2=os.environ.get("RAZON_RFID2")
razonrfid3=os.environ.get("RAZON_RFID3")
razonrfid4=os.environ.get("RAZON_RFID4")
razonrfid5=os.environ.get("RAZON_RFID5")
razonrfid6=os.environ.get("RAZON_RFID6")
razonrfid7=os.environ.get("RAZON_RFID7")
razonrfid8=os.environ.get("RAZON_RFID8")
razonrfid9=os.environ.get("RAZON_RFID9")
razonrfid10=os.environ.get("RAZON_RFID10")
razonrfid11=os.environ.get("RAZON_RFID11")
razonrfid12=os.environ.get("RAZON_RFID12")
razonrfid13=os.environ.get("RAZON_RFID13")
razonrfid14=os.environ.get("RAZON_RFID14")
razonrfid15=os.environ.get("RAZON_RFID15")
razonrfid16=os.environ.get("RAZON_RFID16")
razonrfid17=os.environ.get("RAZON_RFID17")
razonrfid18=os.environ.get("RAZON_RFID18")
razonrfid19=os.environ.get("RAZON_RFID19")
razonrfid20=os.environ.get("RAZON_RFID20")

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

accesodict = {'1':acceso1, '2':acceso2, '3':acceso3, '4':acceso4, '5':acceso5,
                '6':acceso6, '7':acceso7, '8':acceso8, '9':acceso9, '10':acceso10,
                '11':acceso11, '12':acceso12, '13':acceso13, '14':acceso14, '15':acceso15,
                '16':acceso16, '17':acceso17, '18':acceso18, '19':acceso19, '20':acceso20
                }
razondict = {'1':razon1, '2':razon2, '3':razon3, '4':razon4, '5':razon5,
            '6':razon6, '7':razon7, '8':razon8, '9':razon9, '10':razon10,
            '11':razon11, '12':razon12, '13':razon13, '14':razon14, '15':razon15,
                '16':razon16, '17':razon17, '18':razon18, '19':razon19, '20':razon20}

razondicthuellas = {'1':razonhuella1, '2':razonhuella2, '3':razonhuella3, '4':razonhuella4,  '5':razonhuella5,
                    '6':razonhuella6, '7':razonhuella7, '8':razonhuella8, '9':razonhuella9,  '10':razonhuella10,
                    '11':razonhuella11, '12':razonhuella12, '13':razonhuella13, '14':razonhuella14, '15':razonhuella15,
                    '16':razonhuella16, '17':razonhuella17, '18':razonhuella18, '19':razonhuella19, '20':razonhuella20}

razondictrfids = {'1':razonrfid1, '2':razonrfid2, '3':razonrfid3, '4':razonrfid4, '5':razonrfid5,
                    '6':razonrfid6, '7':razonrfid7, '8':razonrfid8, '9':razonrfid9, '10':razonrfid10,
                    '11':razonrfid11, '12':razonrfid12, '13':razonrfid13, '14':razonrfid14, '15':razonrfid15,
                    '16':razonrfid16, '17':razonrfid17, '18':razonrfid18, '19':razonrfid19, '20':razonrfid20}

# def aperturaconcedidawifi(nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso):

#     try:
#         if accesodict[acceso]:
#             requests.get(url=f'{accesodict[acceso]}/on', timeout=3)
#             cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
#             VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razondict[acceso], contratof, cedulaf))
#             #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
#             connf.commit()
#     except:
#         cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
#         VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, f'fallo_{razondict[acceso]}', contratof, cedulaf))
#         #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
#         connf.commit()
#     finally:
#         pass

def aperturaConcedidaVigilante(vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, contrato, cursorf, connf, acceso, razon, personas):
    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}-{razon}"
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursorf.execute('''INSERT INTO web_logs_vigilantes (vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, razon, contrato, personas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, razonRegistrar, contrato, personas))
            connf.commit()
            if razon=='entrada':
                mensaje=f'El vigilante ha dejado entrar {personas} persona que se dirige a su hogar' if (personas=='1' or personas=='0') else f"El vigilante ha dejado entrar {personas} personas que se dirigen a su hogar"
            else:
                mensaje=f'El vigilante ha dejado salir {personas} persona proveniente de su hogar' if (personas=='1' or personas=='0') else f"El vigilante ha dejado salir {personas} personas provenientes de su hogar"
            cursorf.execute('SELECT numero_telefonico FROM web_usuarios WHERE unidad_id=%s AND rol=%s',(unidad_id,'Propietario'))
            propietarios_unidad= cursorf.fetchall()
            for propietario in propietarios_unidad:
                try:
                    requests.get(f'https://api.callmebot.com/whatsapp.php?phone={NUMERO_BOT}&text=!sendto+{propietario[0][1:]}+{mensaje}&apikey={APIKEY_BOT}', timeout=5)
                except Exception as e:
                    print(f"{e} - fallo intentando enviar mensaje vigilante")
    except Exception as e:
        cursorf.execute('''INSERT INTO web_logs_vigilantes (vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, razon, contrato, personas)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, f"fallo_{razonRegistrar}", contrato, personas))
        connf.commit()
        print(f"{e} - fallo intentando abrir el acceso {acceso} con permiso de vigilante")

def aperturaConcedidaVigilanteVisitante2(acceso):
    try:
        if accesodict[acceso]:
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
    except Exception as e:
        print(f"{e} - fallo intentando abrir el acceso {acceso} con permiso de vigilante2")

def aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso, razon, horario_id, aperturasRealizadas, acompanantes, cedula_propietario, numero_propietario, unidad_id, fueraDeHora):
    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}(vigilante)" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}(vigilante)-{razon}"
            # requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursorf.execute('SELECT aperturas_hechas FROM control_horarios_visitantes WHERE horario_id=%s',(horario_id,))
            control_visitante= cursorf.fetchall()
            if aperturasRealizadas<2:
                cursorf.execute('UPDATE control_horarios_visitantes SET aperturas_hechas=%s WHERE horario_id=%s', (aperturasRealizadas+1,horario_id))
                # cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado)
                # VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
                # cursorf.execute('''INSERT INTO web_logs_visitantes (vigilante_id, vigilante_nombre, nombre, fecha, hora, razon, contrato, cedula_id, acompanantes, cedula_propietario)
                # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (vigilante_id, vigilante_nombre, nombref, fechaf, horaf, razonRegistrar, contratof, cedulaf, acompanantes, cedula_propietario))
                connf.commit()
            if cedula_propietario!=None:
                if razon=='entrada':
                    if fueraDeHora:
                        mensaje=f"El invitado *{nombref}* acaba de ingresar de nuevo por medio del sistema de vigilancia y lo hizo fuera del tiempo de su invitacion" if (control_visitante[0][0]==1 and aperturasRealizadas==0) else f"El invitado *{nombref}* llego antes de tiempo y acaba de ingresar por medio del sistema de vigilancia"
                    else:
                        mensaje=f"El invitado *{nombref}* acaba de ingresar de nuevo por medio del sistema de vigilancia" if (control_visitante[0][0]==1 and aperturasRealizadas==0) else f"El invitado *{nombref}* acaba de ingresar por medio del sistema de vigilancia"
                else:
                    if aperturasRealizadas==2:
                        if fueraDeHora:
                            mensaje=f"El invitado *{nombref}* acaba de salir sin antes haber entrado por medio del sistema de vigilancia y lo hizo fuera del tiempo de su invitacion"
                        else:
                            mensaje=f"El invitado *{nombref}* acaba de salir sin antes haber entrado por medio del sistema de vigilancia"
                    else:
                        if fueraDeHora:
                            mensaje=f"El invitado *{nombref}* acaba de salir de nuevo por medio del sistema de vigilancia y lo hizo fuera del tiempo de su invitacion" if (control_visitante[0][0]==2 and aperturasRealizadas==1) else f"El invitado *{nombref}* acaba de salir por medio del sistema de vigilancia despues de vencido su tiempo de invitacion"
                        else:
                            mensaje=f"El invitado *{nombref}* acaba de salir de nuevo por medio del sistema de vigilancia" if (control_visitante[0][0]==2 and aperturasRealizadas==1) else f"El invitado *{nombref}* acaba de salir por medio del sistema de vigilancia"
                try:
                    requests.get(f'https://api.callmebot.com/whatsapp.php?phone={NUMERO_BOT}&text=!sendto+{numero_propietario[1:]}+{mensaje}&apikey={APIKEY_BOT}', timeout=5)
                except Exception as e:
                    print(f"{e} - fallo intentando enviar mensaje vigilante visitante")
            else:
                cursorf.execute('SELECT numero_telefonico FROM web_usuarios WHERE unidad_id=%s AND rol=%s',(unidad_id,'Propietario'))
                propietarios= cursorf.fetchall()
                for propietario in propietarios:
                    if razon=='entrada':
                        mensaje=f"La vigilancia acaba de dejar ingresar a su visita sin invitacion *{nombref}*"
                    else:
                        mensaje=f"La vigilancia acaba de dejar salir a su visita sin invitacion *{nombref}*"
                    try:
                        requests.get(f'https://api.callmebot.com/whatsapp.php?phone={NUMERO_BOT}&text=!sendto+{propietario[0][1:]}+{mensaje}&apikey={APIKEY_BOT}', timeout=5)
                    except Exception as e:
                        print(f"{e} - fallo intentando enviar mensaje vigilante visitante")


    except Exception as e:
        cursorf.execute('''INSERT INTO web_logs_visitantes (vigilante_id, vigilante_nombre, nombre, fecha, hora, razon, contrato, cedula_id, acompanantes, cedula_propietario, unidad_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (vigilante_id, vigilante_nombre, nombref, fechaf, horaf, f"fallo_{razonRegistrar}", contratof, cedulaf, acompanantes, cedula_propietario, unidad_id))
        connf.commit()
        print(f"{e} - fallo intentando abrir el acceso {acceso} con permiso de vigilante")

def controlhorariovisitante(cursorf, connf, horario_id, razon):
    abrir=False
    cantidad_aperturas=0
    cursorf.execute('SELECT aperturas_hechas FROM control_horarios_visitantes WHERE horario_id=%s',(horario_id,))
    control_visitante= cursorf.fetchall()
    if not control_visitante:
        if razon=='entrada':
            cursorf.execute('''INSERT INTO control_horarios_visitantes (horario_id, aperturas_hechas) 
            VALUES (%s, %s)''', (horario_id, 0))
            connf.commit()
            abrir=True
        elif razon=='salida':
            cursorf.execute('''INSERT INTO control_horarios_visitantes (horario_id, aperturas_hechas) 
            VALUES (%s, %s)''', (horario_id, 2))
            connf.commit()
            cantidad_aperturas=1
            # abrir=True
    elif not control_visitante and horario_id=='0':
        abrir=True
    elif control_visitante[0][0]==0 and razon=='entrada':
        abrir=True
    elif control_visitante[0][0]<2:
        if razon=='salida':
            cantidad_aperturas=control_visitante[0][0]
            abrir=True
        else:
            cantidad_aperturas=control_visitante[0][0]
    elif control_visitante[0][0]==2:
        cantidad_aperturas=2

    return abrir, cantidad_aperturas

def aperturaconcedidawifi(id_usuariof, cursorf, connf, acceso, cedulaf, nombref, fechaf, horaf, razon):
    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}(Wifi)" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}(Wifi)-{razon}"
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
            VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, CONTRATO, cedulaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            # connf.commit()
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado) 
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            connf.commit()
    except:
        IdContador=0
        cursorf.execute('SELECT id FROM solicitud_aperturas ORDER BY id ASC')
        ids_peticiones_local= cursorf.fetchall()
        nro_ids_peticiones_local=len(ids_peticiones_local)
        if not ids_peticiones_local:
            idPeticion = 1
        else:
            for id_peticion_local in ids_peticiones_local:
                IdContador=IdContador+1
                if not id_peticion_local[0] == IdContador:
                    idPeticion=IdContador
                    break
            if nro_ids_peticiones_local == IdContador:
                idPeticion=IdContador+1

        if accesodict[acceso]:
            cursorf.execute('''INSERT INTO solicitud_aperturas (id, id_usuario, acceso, razon, estado, peticionInternet, feedback, abriendo, fecha, hora)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (idPeticion, id_usuariof, acceso, razon, 0, 'f', 'f', 'f', fechaf, horaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            connf.commit()

def aperturaconcedidawifivisitante(id_usuariof, cursorf, connf, acceso, cedulaf, nombref, fechaf, horaf, razon, horario_id, aperturasRealizadas):
    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}(Wifi)" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}(Wifi)-{razon}"
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursor.execute('UPDATE control_horarios_visitantes SET aperturas_hechas=%s WHERE horario_id=%s', (aperturasRealizadas+1,horario_id))
            cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
            VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, CONTRATO, cedulaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            # connf.commit()
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado) 
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            connf.commit()        
    except:
        IdContador=0
        cursorf.execute('SELECT id FROM solicitud_aperturas ORDER BY id ASC')
        ids_peticiones_local= cursorf.fetchall()
        nro_ids_peticiones_local=len(ids_peticiones_local)
        if not ids_peticiones_local:
            idPeticion = 1
        else:
            for id_peticion_local in ids_peticiones_local:
                IdContador=IdContador+1
                if not id_peticion_local[0] == IdContador:
                    idPeticion=IdContador
                    break
            if nro_ids_peticiones_local == IdContador:
                idPeticion=IdContador+1

        if accesodict[acceso]:
            cursorf.execute('''INSERT INTO solicitud_aperturas (id, id_usuario, acceso, razon, estado, peticionInternet, feedback, abriendo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (idPeticion, id_usuariof, acceso, razon, 0, 'f', 'f', 'f'))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            connf.commit()


def aperturaconcedidahuella(nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso, razon):

    try:
        if accesodict[acceso]:
            razonRegistrar=razondicthuellas[acceso] if (razon in razondicthuellas[acceso].lower()) else f"{razondicthuellas[acceso]}-{razon}"
            requests.get(url=f'{accesodict[acceso]}/onrh', timeout=5)
            cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
            VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, contratof, cedulaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado) 
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            connf.commit()
    except:
        cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
        VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, f'fallo_{razonRegistrar}', contratof, cedulaf))
        #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
        connf.commit()
    finally:
        pass

def aperturaconcedidarfid(nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso):

    try:
        if accesodict[acceso]:
            razonRegistrar=razondictrfids[acceso] if (razon in razondictrfids[acceso].lower()) else f"{razondictrfids[acceso]}-{razon}"
            requests.get(url=f'{accesodict[acceso]}/onrh', timeout=5)
            cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
            VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, contratof, cedulaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado) 
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            connf.commit()
    except:
        cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
        VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, f'fallo_{razonRegistrar}', contratof, cedulaf))
        #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
        connf.commit()
    finally:
        pass

def aperturaconcedidabluetooth(nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso, razon):

    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}(Bluetooth)" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}(Bluetooth)-{razon}"
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
            VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, CONTRATO, cedulaf))
            #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
            # connf.commit()
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado) 
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            connf.commit()
    except:
        cursorf.execute('''INSERT INTO web_logs_usuarios (nombre, fecha, hora, razon, contrato, cedula_id)
        VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, f'fallo_{razonRegistrar}', contratof, cedulaf))
        #cursorf.execute('''UPDATE led SET onoff=1 WHERE onoff=0;''')
        connf.commit()
    finally:
        pass

def aperturaconcedidabluetoothvisitante(nombref, fechaf, horaf, contratof, cedulaf, cursorf, connf, acceso, razon, horario_id, aperturasRealizadas, acompanantes, cedula_propietario, numero_propietario, unidad_id):

    try:
        if accesodict[acceso]:
            razonRegistrar=f"{razondict[acceso]}(bluetooth)" if (razon in razondict[acceso].lower()) else f"{razondict[acceso]}(bluetooth)-{razon}"
            requests.get(f'{accesodict[acceso]}/on', timeout=5)
            cursorf.execute('UPDATE control_horarios_visitantes SET aperturas_hechas=%s WHERE horario_id=%s', (aperturasRealizadas+1,horario_id))
            cursorf.execute('''INSERT INTO accesos_abiertos (cedula, acceso, fecha, hora, estado)
            VALUES (%s, %s, %s, %s, %s)''', (cedulaf, acceso, fechaf, horaf, 'f'))
            cursorf.execute('''INSERT INTO web_logs_visitantes (nombre, fecha, hora, razon, contrato, cedula_id, acompanantes, cedula_propietario, unidad_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonRegistrar, contratof, cedulaf, acompanantes, cedula_propietario, unidad_id))
            connf.commit()
            if razon=='entrada':
                mensaje=f"El invitado {nombref} acaba de ingresar por medio de bluetooth"
            else:
                mensaje=f"El invitado {nombref} acaba de salir por medio de bluetooth"
            try:
                requests.get(f'https://api.callmebot.com/whatsapp.php?phone={NUMERO_BOT}&text=!sendto+{numero_propietario[1:]}+{mensaje}&apikey={APIKEY_BOT}', timeout=5)
            except Exception as e:
                print(f"{e} - fallo intentando enviar mensaje visitante bluetooth")
    except Exception as e:
        cursorf.execute('''INSERT INTO web_logs_visitantes (nombre, fecha, hora, razon, contrato, cedula_id, acompanantes, cedula_propietario, unidad_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, f"fallo_{razonRegistrar}", contratof, cedulaf, acompanantes, cedula_propietario, unidad_id))
        connf.commit()
        print(f"{e} - fallo intentando abrir el acceso {acceso} por bluetooth")

def aperturadenegada(cursorf, connf, acceso):
    # cursorf.execute('''UPDATE led SET onoff=2 WHERE onoff=0;''')
    # connf.commit()
    try:
        requests.get(url=f'{accesodict[acceso]}/off', timeout=2)
    except:
        print("fallo en peticion http")
    finally:
        pass

def invertir_uuid(uuid_beacon):
    uuidInvertido=''
    cont=36
    for char in range(1,17):
        uuidInvertido=uuidInvertido+uuid_beacon[cont-2:cont]
        cont=cont-2
        if char==4:
            uuidInvertido+='-'
        if char==6:
            cont=cont-1
            uuidInvertido+='-'
        if char==8:
            cont=cont-1
            uuidInvertido+='-'
        if char==10:
            cont=cont-1
            uuidInvertido+='-'
        if char==12:
            cont=cont-1
    return uuidInvertido

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        peticion=self.path[1::].split("/")

        if self.path == "/seguricel_ping":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            
        if len(peticion) == 2 and peticion[0] == "obtenerinvitacionvigilanteapi":
            _, horario_id = peticion
            cursor.execute("SELECT usuario, fecha_entrada, fecha_salida, entrada, salida, acompanantes FROM web_horariospermitidos where id=%s", (int(horario_id),))
            datosHorario = cursor.fetchall()
            if datosHorario:
                usuario=datosHorario[0][0]
                fecha_entrada=datosHorario[0][1]
                fecha_salida=datosHorario[0][2]
                entrada=datosHorario[0][3]
                salida=datosHorario[0][4]
                acompanantes=datosHorario[0][5]
                cursor.execute("SELECT cedula, nombre, cedula_propietario, unidad_id FROM web_usuarios where id=%s", (usuario,))
                datosInvitado = cursor.fetchall()
                cursor.execute("SELECT codigo FROM web_unidades where id=%s", (datosInvitado[0][3],))
                unidad = cursor.fetchall()
                if datosInvitado:
                    cursor.execute("SELECT aperturas_hechas FROM control_horarios_visitantes where horario_id=%s", (horario_id,))
                    aperturasConInvitacion = cursor.fetchall()
                    if not aperturasConInvitacion:
                        cedula=datosInvitado[0][0]
                        nombre=datosInvitado[0][1]
                        cedula_propietario=datosInvitado[0][2]
                        codigo_unidad=unidad[0][0]
                        invitacion={
                            "id": horario_id,
                            "fecha_entrada": fecha_entrada.isoformat(),
                            "fecha_salida": fecha_salida.isoformat(),
                            "entrada": entrada.isoformat(),
                            "salida": salida.isoformat(),
                            "cedula": cedula,
                            "cedula_propietario": cedula_propietario,
                            "acompanantes": acompanantes,
                            "usuario": usuario,
                            "codigo_unidad": codigo_unidad,
                            "nombre":nombre,
                            "unidad":datosInvitado[0][3]
                            }
                        invitacion_json = json.dumps(invitacion)
                        self.send_response(code=200)
                        self.send_header(keyword='Content-type', value='application/json')
                        self.end_headers()
                        self.wfile.write(invitacion_json.encode('utf-8'))
                    elif aperturasConInvitacion[0][0]<=1:
                        cedula=datosInvitado[0][0]
                        nombre=datosInvitado[0][1]
                        cedula_propietario=datosInvitado[0][2]
                        codigo_unidad=unidad[0][0]
                        invitacion={
                            "id": horario_id,
                            "fecha_entrada": fecha_entrada.isoformat(),
                            "fecha_salida": fecha_salida.isoformat(),
                            "entrada": entrada.isoformat(),
                            "salida": salida.isoformat(),
                            "cedula": cedula,
                            "cedula_propietario": cedula_propietario,
                            "acompanantes": acompanantes,
                            "usuario": usuario,
                            "codigo_unidad": codigo_unidad,
                            "nombre":nombre,
                            "unidad":datosInvitado[0][3]
                            }
                        invitacion_json = json.dumps(invitacion)
                        self.send_response(code=200)
                        self.send_header(keyword='Content-type', value='application/json')
                        self.end_headers()
                        self.wfile.write(invitacion_json.encode('utf-8'))
                    elif aperturasConInvitacion[0][0]==2:
                        self.send_response(402)
                        self.send_header(keyword='Content-type', value='application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps([]).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.send_header(keyword='Content-type', value='application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps([]).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(json.dumps([]).encode('utf-8'))
        
        if len(peticion) == 1 and peticion[0] == "obtenerunidades":
            # _, horario_id = peticion
            cursor.execute("SELECT id, nombre, codigo FROM web_unidades ORDER BY codigo ASC")
            unidades = cursor.fetchall()
            if unidades:
                unidadesJson=[]
                for unidad in unidades:
                    unidadDict={'id':unidad[0], 'nombre':unidad[1], 'codigo':unidad[2]}
                    unidadesJson.append(unidadDict)
                unidades_json = json.dumps(unidadesJson)
                self.send_response(code=200)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(unidades_json.encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(json.dumps([]).encode('utf-8'))
        
        if len(peticion) == 1 and peticion[0] == "obtenerunidadesvisitantes":
            # _, horario_id = peticion
            cursor.execute("SELECT b.id, b.nombre, b.codigo FROM web_usuarios AS a INNER JOIN web_unidades AS b ON a.unidad_id = b.id WHERE a.rol='Visitante' GROUP BY b.id, b.nombre, b.codigo ORDER BY b.id ASC")
            unidades = cursor.fetchall()
            if unidades:
                unidadesJson=[]
                for unidad in unidades:
                    unidadDict={'id':unidad[0], 'nombre':unidad[1], 'codigo':unidad[2]}
                    unidadesJson.append(unidadDict)
                unidades_json = json.dumps(unidadesJson)
                self.send_response(code=200)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(unidades_json.encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(json.dumps([]).encode('utf-8'))
        
        if len(peticion) == 2 and peticion[0] == "obtenervisitantes":
            _, unidad_id = peticion
            cursor.execute(f"SELECT a.id, a.nombre, a.cedula, a.cedula_propietario, b.id FROM web_usuarios AS a INNER JOIN web_unidades AS b ON a.unidad_id = b.id WHERE a.rol='Visitante' AND a.unidad_id={unidad_id}")
            visitantes = cursor.fetchall()
            if visitantes:
                visitantesJson=[]
                for visitante in visitantes:
                    visitanteDict={'usuario_id':visitante[0], 'nombre':visitante[1], 'cedula':visitante[2], 'cedula_propietario':visitante[3], 'unidad_id':visitante[4]}
                    visitantesJson.append(visitanteDict)
                visitantes_json = json.dumps(visitantesJson)
                self.send_response(code=200)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(visitantes_json.encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header(keyword='Content-type', value='application/json')
                self.end_headers()
                self.wfile.write(json.dumps([]).encode('utf-8'))

        if len(peticion) == 2 and peticion[0] == "obtenerinvitacioninvitado":
            _, usuario_id = peticion
            horarioEncontrado=False
            cursor.execute("SELECT id, fecha_entrada, fecha_salida, entrada, salida, acompanantes FROM web_horariospermitidos WHERE usuario=%s ORDER BY id ASC", (int(usuario_id),))
            invitaciones = cursor.fetchall()
            tz = pytz.timezone('America/Caracas')
            caracas_now = datetime.now(tz)
            horahoy = caracas_now.time()
            fechahoy = caracas_now.date()
            if invitaciones:
                for horario_id, fecha_entrada, fecha_salida, entrada, salida, acompanantes in invitaciones:
                    cursor.execute("SELECT aperturas_hechas FROM control_horarios_visitantes where horario_id=%s", (horario_id,))
                    aperturasConInvitacion = cursor.fetchall()
                    if (fecha_entrada!=fecha_salida):
                        if not aperturasConInvitacion:
                            if (fechahoy==fecha_entrada and horahoy>=entrada) or (fechahoy > fecha_entrada and fechahoy<fecha_salida) or (fechahoy==fecha_salida and horahoy<=salida):
                                horarioEncontrado=True
                                visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                                self.send_response(code=200)
                                self.send_header(keyword='Content-type', value='application/json')
                                self.end_headers()
                                self.wfile.write(visitantes_json.encode('utf-8'))
                                break
                        elif aperturasConInvitacion[0][0]<=1: 
                            horarioEncontrado=True
                            visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                            self.send_response(code=200)
                            self.send_header(keyword='Content-type', value='application/json')
                            self.end_headers()
                            self.wfile.write(visitantes_json.encode('utf-8'))
                            break
                    else:
                        if not aperturasConInvitacion:
                            if (horahoy>=entrada and horahoy<=salida):
                                horarioEncontrado=True
                                visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                                self.send_response(code=200)
                                self.send_header(keyword='Content-type', value='application/json')
                                self.end_headers()
                                self.wfile.write(visitantes_json.encode('utf-8'))
                                break
                        elif aperturasConInvitacion[0][0]<=1: 
                            if (horahoy>=entrada and horahoy<=salida):
                                horarioEncontrado=True
                                visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                                self.send_response(code=200)
                                self.send_header(keyword='Content-type', value='application/json')
                                self.end_headers()
                                self.wfile.write(visitantes_json.encode('utf-8'))
                                break
                if horarioEncontrado==False:
                    for horario_id, fecha_entrada, fecha_salida, entrada, salida, acompanantes in invitaciones:
                        cursor.execute("SELECT aperturas_hechas FROM control_horarios_visitantes where horario_id=%s", (horario_id,))
                        aperturasConInvitacion = cursor.fetchall()
                        if not aperturasConInvitacion:
                            visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                            self.send_response(code=400)
                            self.send_header(keyword='Content-type', value='application/json')
                            self.end_headers()
                            self.wfile.write(visitantes_json.encode('utf-8'))
                            break
                        elif aperturasConInvitacion[0][0]<=1: 
                            visitantes_json = json.dumps({'horario_id':horario_id, 'acompanantes':acompanantes})
                            self.send_response(code=400)
                            self.send_header(keyword='Content-type', value='application/json')
                            self.end_headers()
                            self.wfile.write(visitantes_json.encode('utf-8'))
                            break
                        elif aperturasConInvitacion[0][0]==2:
                            self.send_response(402)
                            self.send_header(keyword='Content-type', value='application/json')
                            self.end_headers()
                            self.wfile.write(json.dumps({}).encode('utf-8'))
                            break

            else:
                visitantes_json = json.dumps({})
                if horarioEncontrado==False:
                    self.send_response(401)
                    self.send_header(keyword='Content-type', value='application/json')
                    self.end_headers()
                    self.wfile.write(visitantes_json.encode('utf-8'))
        # else:
        #     print("cerrado")
        #     webServer.shutdown()
        
        # peticion=self.path[1::].split("/")
        # print(f"peticion = {peticion}")
        # self.send_header("Content-type", "utf-8")
        # self.end_headers()
        #self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))

        

    def do_POST(self):
        peticion=self.path[1::].split("/")

        if len(peticion) == 1 and peticion[0] == "crearinvitacionprovisional":
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(self.data_string)
            #print(data)
            id_usuario=0
            id_horario=0
            IdUsuarioContador=0
            IdHorarioContador=0
            cursor.execute('SELECT id FROM web_usuarios ORDER BY id ASC')
            ids_usuarios_local= cursor.fetchall()
            nro_ids_usuarios_local=len(ids_usuarios_local)
            if not ids_usuarios_local:
                id_usuario = 1
            else:
                for id_usuario_local in ids_usuarios_local:
                    IdUsuarioContador=IdUsuarioContador+1
                    if not id_usuario_local[0] == IdUsuarioContador:
                        id_usuario=IdUsuarioContador
                        break
                if nro_ids_usuarios_local == IdUsuarioContador:
                    id_usuario=IdUsuarioContador+1

            cursor.execute('SELECT id FROM web_horariospermitidos ORDER BY id ASC')
            ids_horarios_local= cursor.fetchall()
            nro_ids_horarios_local=len(ids_horarios_local)
            if not ids_horarios_local:
                id_horario = 1
            else:
                for id_horario_local in ids_horarios_local:
                    IdHorarioContador=IdHorarioContador+1
                    if not id_horario_local[0] == IdHorarioContador:
                        id_horario=IdHorarioContador
                        break
                if nro_ids_horarios_local == IdHorarioContador:
                    id_horario=IdHorarioContador+1

            tz = pytz.timezone('America/Caracas')
            caracas_now = datetime.now(tz)
            hora=str(caracas_now)[11:19]
            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
            cursor.execute('''INSERT INTO web_usuarios (id, rol, nombre, cedula, unidad_id, internet, wifi, bluetooth, captahuella, rfid, facial)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', 
            (id_usuario, "Visitante", data['nombre'], data['cedula'], data['unidad_id'], 'f', 'f', 'f', 'f', 'f', 'f',))
            conn.commit()
            cursor.execute('''INSERT INTO web_horariospermitidos (id, usuario, fecha_entrada, fecha_salida, entrada, salida, cedula_id, acompanantes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (id_horario, id_usuario, data['fecha_entrada'], data['fecha_salida'], horahoy, horahoy, data['cedula'], data['acompanantes']))
            conn.commit()
            self.send_response(200)
            self.send_header(keyword='Content-type', value='application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'horario_id':id_horario, 'usuario_id':id_usuario}).encode('utf-8'))
        
        if len(peticion) == 1 and peticion[0] == "enviarloglocal":
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(self.data_string)
            #print(data)
            cursor.execute('''INSERT INTO web_logs_visitantes (vigilante_id, vigilante_nombre, nombre, fecha, hora, razon, contrato, cedula_id, acompanantes, cedula_propietario, unidad_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (data['vigilante_id'], data['vigilante_nombre'], data['nombre'], data['fecha'], data['hora'], data['razon'], data['contrato'], data['cedula'], data['acompanantes'], data['cedula_propietario'], data['unidad_id']))
            conn.commit()
            self.send_response(200)
            self.send_header(keyword='Content-type', value='application/json')
            self.end_headers()
            self.wfile.write(json.dumps([]).encode('utf-8'))

        if len(peticion) == 2 and peticion[1] == "cerrandoacceso":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            acceso_solicitud, _ = peticion
            cursor.execute('UPDATE accesos_abiertos SET estado=%s WHERE acceso=%s', ('t', acceso_solicitud))
            conn.commit()
        
        if len(peticion) == 2 and peticion[1] == "noregistrado":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            acceso_solicitud, _ = peticion
            aperturadenegada(cursor, conn, acceso_solicitud)

        if len(peticion) == 6 and peticion[5] == "seguricel_wifi_vigilante":
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))
            id_usuario, codigo_unidad, personas, acceso_solicitud, razonApertura, _ = peticion
            # print(codigo_unidad)
            # print(personas)
            # print(acceso_solicitud)
            # print(razonApertura)

            cursor.execute("SELECT id, nombre FROM web_usuarios where telegram_id=%s", (id_usuario,))
            datosVigilante = cursor.fetchall()
            cursor.execute("SELECT id, nombre FROM web_unidades where codigo=%s", (int(codigo_unidad),))
            datosUnidad = cursor.fetchall()
            
            # print(datosUnidad)
            if len(datosUnidad)!=0 and len(datosVigilante)!=0:
                tz = pytz.timezone('America/Caracas')
                caracas_now = datetime.now(tz)
                hora=str(caracas_now)[11:19]
                fecha=str(caracas_now)[:10]
                unidad_id=datosUnidad[0][0]
                unidad_nombre=datosUnidad[0][1]
                vigilante_id=datosVigilante[0][0]
                vigilante_nombre=datosVigilante[0][1]
                
                aperturaConcedidaVigilante(vigilante_id, vigilante_nombre, unidad_id, unidad_nombre, fecha, hora, CONTRATO, cursor, conn, acceso_solicitud, razonApertura, personas)
                self.send_response(200)
                self.send_header("Content-type", "utf-8")
                self.end_headers()
            else:
                aperturadenegada(cursor, conn, acceso_solicitud)
                self.send_response(400)
                self.send_header("Content-type", "utf-8")
                self.end_headers()
        
        if len(peticion) == 6 and peticion[5] == "seguricel_wifi_vigilante_invitado":
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))
            id_usuario, horario_id, acompanantes, acceso_solicitud, razonApertura, _ = peticion
            # print(codigo_unidad)
            # print(personas)
            # print(acceso_solicitud)
            # print(razonApertura)

            if id_usuario=='blank' and horario_id=="blank" and acompanantes=="blank" and razonApertura=="blank":
                aperturaConcedidaVigilanteVisitante2(acceso_solicitud)
                self.send_response(200)
                self.send_header("Content-type", "utf-8")
                self.end_headers()
            else:
                cursor.execute("SELECT id, nombre FROM web_usuarios where telegram_id=%s", (id_usuario,))
                datosVigilante = cursor.fetchall()
                cursor.execute("SELECT usuario, fecha_entrada, fecha_salida, entrada, salida FROM web_horariospermitidos where id=%s", (int(horario_id),))
                datosHorario = cursor.fetchall()
                datosPropietario=None
                if len(datosHorario)!=0:
                    cursor.execute("SELECT cedula, nombre, cedula_propietario, unidad_id FROM web_usuarios where id=%s", (int(datosHorario[0][0]),))
                    datosInvitado = cursor.fetchall()
                    if datosInvitado[0][2]!=None:
                        cursor.execute("SELECT numero_telefonico FROM web_usuarios where cedula=%s", (datosInvitado[0][2],))
                        datosPropietario = cursor.fetchall()
                    if len(datosInvitado)!=0:
                        tz = pytz.timezone('America/Caracas')
                        caracas_now = datetime.now(tz)
                        horahoy = caracas_now.time()
                        fechahoy = caracas_now.date()
                        for _, fecha_entrada, fecha_salida, entrada, salida in datosHorario:
                            if (fecha_entrada!=fecha_salida):
                                if (fechahoy==fecha_entrada and horahoy>=entrada) or (fechahoy > fecha_entrada and fechahoy<fecha_salida) or (fechahoy==fecha_salida and horahoy<=salida):
                                    permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                    if permitir:
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(202)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='entrada':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 0, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(406)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==2 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 1, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(407)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 2, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(405)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()  
                                else:
                                    permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                    if permitir:
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(202)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='entrada':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 0, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(406)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==2 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 1, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(407)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 2, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(405)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers() 
                            else:
                                if (horahoy>=entrada and horahoy<=salida):
                                    permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                    if permitir:
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(202)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='entrada':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 0, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(406)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==2 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 1, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(407)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 2, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], False)
                                        self.send_response(405)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()  
                                else:
                                    permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                    if permitir:
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(202)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='entrada':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 0, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(406)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==2 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 1, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(407)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()
                                    elif aperturasRealizadas==1 and razonApertura=='salida':
                                        invitado_cedula=datosInvitado[0][0]
                                        invitado_nombre=datosInvitado[0][1]
                                        vigilante_id=datosVigilante[0][0]
                                        vigilante_nombre=datosVigilante[0][1]
                                        fecha=str(caracas_now)[:10]
                                        
                                        aperturaConcedidaVigilanteVisitante(vigilante_id, vigilante_nombre, invitado_nombre, fecha, horahoy, CONTRATO, invitado_cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, 2, acompanantes, datosInvitado[0][2], f"" if (datosPropietario==None) else f"{datosPropietario[0][0]}", datosInvitado[0][3], True)
                                        self.send_response(405)
                                        self.send_header("Content-type", "utf-8")
                                        self.end_headers()  
                    else:
                        aperturadenegada(cursor, conn, acceso_solicitud)
                        self.send_response(404)
                        self.send_header("Content-type", "utf-8")
                        self.end_headers()
                else:
                    aperturadenegada(cursor, conn, acceso_solicitud)
                    self.send_response(404)
                    self.send_header("Content-type", "utf-8")
                    self.end_headers()

        if len(peticion) == 4 and peticion[3] == "seguricel_wifi_activo":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))

            id_usuario, acceso_solicitud, razonApertura, _ = peticion
            #print(id_usuario)
            #print(acceso_solicitud)

            diasusuario = []
            etapadia=0
            etapadiaapertura=0
            cantidaddias = 0
            contadoraux = 0
            cursor.execute("SELECT cedula, nombre, wifi, telegram_id, rol, id FROM web_usuarios where telegram_id=%s", (id_usuario,))
            datosUsuario = cursor.fetchall()
            #print(datosUsuario)
            if len(datosUsuario)!=0:
                cedula=datosUsuario[0][0]
                nombre=datosUsuario[0][1]
                permisoAperturaWifi = datosUsuario[0][2]
                idUsuario = datosUsuario[0][3]
                rol=datosUsuario[0][4]
                usuario_id=datosUsuario[0][5]
                cursor.execute('SELECT id, fecha_entrada, fecha_salida, entrada, salida, dia FROM web_horariospermitidos where usuario=%s', (usuario_id,))
                horarios_permitidos = cursor.fetchall()
                if (horarios_permitidos != [] and permisoAperturaWifi == True and rol=='Secundario'):
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    dia = caracas_now.weekday()
                    diahoy = dias_semana[dia]
                    for _, _, _, entrada, salida, dia in horarios_permitidos:
                        diasusuario.append(dia)
                    cantidaddias = diasusuario.count(dia)
                    for _, _, _, entrada, salida, dia in horarios_permitidos:
                        if 'Siempre' in diasusuario:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                            aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                            etapadiaapertura=1
                        elif dia==diahoy and cantidaddias==1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                        elif dia==diahoy and cantidaddias>1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                                    #print('fuera de horario')
                    if etapadia==0 and etapadiaapertura==0:
                        aperturadenegada(cursor, conn, acceso_solicitud)
                        #print('Dia no permitido')
                elif rol=='Propietario' and permisoAperturaWifi == True:
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    hora=str(caracas_now)[11:19]
                    horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                    fecha=str(caracas_now)[:10]
                    aperturaconcedidawifi(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, horahoy, razonApertura)
                elif (horarios_permitidos != [] and permisoAperturaWifi == True and rol=='Visitante'):
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    hora=str(caracas_now)[11:19]
                    horahoy = caracas_now.time()
                    fechahoy = caracas_now.date()
                    for horario_id, fecha_entrada, fecha_salida, entrada, salida, _ in horarios_permitidos:
                        if (fechahoy==fecha_entrada and horahoy>=entrada) or (fechahoy > fecha_entrada and fechahoy<fecha_salida) or (fechahoy==fecha_salida and horahoy<=salida):
                            permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                            if permitir:
                                fecha=str(caracas_now)[:10]
                                aperturaconcedidawifivisitante(idUsuario, cursor, conn, acceso_solicitud, cedula, nombre, fecha, hora, razonApertura, horario_id, aperturasRealizadas)
                            else:
                                aperturadenegada(cursor, conn, acceso_solicitud)  
                        else:
                            aperturadenegada(cursor, conn, acceso_solicitud)
                else:
                    aperturadenegada(cursor, conn, acceso_solicitud)
                # if horarios_permitidos == []:
                #     aperturadenegada(cursor, conn, acceso_solicitud)
                #     #print('este usuario no tiene horarios establecidos')
                diasusuario=[]
            else:
                aperturadenegada(cursor, conn, acceso_solicitud)

        if len(peticion) == 4 and peticion[3] == "seguricel_bluetooth_activo":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))

            uuid_usuario, acceso_solicitud, razonApertura, _ = peticion
            #print(id_usuario)
            #print(acceso_solicitud)
            #uuid_usuario = invertir_uuid(uuid_usuario)

            diasusuario = []
            etapadia=0
            etapadiaapertura=0
            cantidaddias = 0
            contadoraux = 0
            cursor.execute("SELECT cedula, nombre, bluetooth, rol, id, cedula_propietario, unidad_id FROM web_usuarios where entrada_beacon_uuid=%s", (uuid_usuario,))
            datosUsuario = cursor.fetchall()
            razonApertura='entrada'
            if not datosUsuario:
                cursor.execute("SELECT cedula, nombre, bluetooth, rol, id, cedula_propietario, unidad_id FROM web_usuarios where salida_beacon_uuid=%s", (uuid_usuario,))
                datosUsuario = cursor.fetchall()
                razonApertura='salida'
            #print(datosUsuario)
            if len(datosUsuario)!=0:
                cedula=datosUsuario[0][0]
                nombre=datosUsuario[0][1]
                permisoAperturaBluetooth = datosUsuario[0][2]
                rol=datosUsuario[0][3]
                usuario_id=datosUsuario[0][4]
                cedula_propietario=datosUsuario[0][5]
                unidad_id=datosUsuario[0][6]
                cursor.execute('SELECT id, fecha_entrada, fecha_salida, entrada, salida, dia, acompanantes FROM web_horariospermitidos where usuario=%s', (usuario_id,))
                horarios_permitidos = cursor.fetchall()
                if horarios_permitidos != [] and permisoAperturaBluetooth == True and rol=='Secundario':
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    dia = caracas_now.weekday()
                    diahoy = dias_semana[dia]
                    for _, _, _, entrada, salida, dia, _ in horarios_permitidos:
                        diasusuario.append(dia)
                    cantidaddias = diasusuario.count(dia)
                    for _, _, _, entrada, salida, dia, _ in horarios_permitidos:
                        if 'Siempre' in diasusuario:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                            aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                            etapadiaapertura=1
                        elif dia==diahoy and cantidaddias==1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                        elif dia==diahoy and cantidaddias>1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                                    aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                                    #print('fuera de horario')
                    if etapadia==0 and etapadiaapertura==0:
                        aperturadenegada(cursor, conn, acceso_solicitud)
                        #print('Dia no permitido')
                elif rol=='Propietario' and permisoAperturaBluetooth == True:
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    hora=str(caracas_now)[11:19]
                    horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                    fecha=str(caracas_now)[:10]
                    #aperturaconcedidawifi(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud)
                    aperturaconcedidabluetooth(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                elif (horarios_permitidos != [] and permisoAperturaBluetooth == True and rol=='Visitante'):
                    cursor.execute("SELECT numero_telefonico FROM web_usuarios where cedula=%s", (cedula_propietario,))
                    datosPropietario = cursor.fetchall()
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    horahoy = caracas_now.time()
                    fechahoy = caracas_now.date()
                    for horario_id, fecha_entrada, fecha_salida, entrada, salida, _, acompanantes in horarios_permitidos:
                        if (fecha_entrada!=fecha_salida):
                            if (fechahoy==fecha_entrada and horahoy>=entrada) or (fechahoy > fecha_entrada and fechahoy<fecha_salida) or (fechahoy==fecha_salida and horahoy<=salida):
                                permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                if permitir and len(datosPropietario):
                                    fecha=str(caracas_now)[:10]
                                    aperturaconcedidabluetoothvisitante(nombre, fecha, hora, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, cedula_propietario, datosPropietario[0][0],unidad_id)
                                    break
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)  
                            else:
                                aperturadenegada(cursor, conn, acceso_solicitud)
                        else:
                            if (horahoy>=entrada and horahoy<=salida):
                                permitir, aperturasRealizadas = controlhorariovisitante(cursor, conn, horario_id, razonApertura)
                                if permitir and len(datosPropietario):
                                    fecha=str(caracas_now)[:10]
                                    aperturaconcedidabluetoothvisitante(nombre, fecha, hora, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura, horario_id, aperturasRealizadas, acompanantes, cedula_propietario, datosPropietario[0][0],unidad_id)
                                    break
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)  
                            else:
                                aperturadenegada(cursor, conn, acceso_solicitud)
                else:
                    aperturadenegada(cursor, conn, acceso_solicitud)
                    #print('este usuario no tiene horarios establecidos')
                diasusuario=[]
            else:
                aperturadenegada(cursor, conn, acceso_solicitud)

        if len(peticion) == 4 and peticion[3] == "seguricel_captahuella_activo":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))

            id_suprema, acceso_solicitud, razonApertura, _ = peticion
            id_suprema = id_suprema[6:]+id_suprema[4:6]+id_suprema[2:4]+id_suprema[0:2]
            id_suprema = int(id_suprema, 16)
            #print(id_suprema)
            #print(acceso_solicitud)

            diasusuario = []
            etapadia=0
            etapadiaapertura=0
            cantidaddias = 0
            contadoraux = 0
            cursor.execute("SELECT cedula FROM web_huellas where id_suprema=%s", (id_suprema,))
            datosusuario_huella = cursor.fetchall()
            #print(datosUsuario)
            if len(datosusuario_huella)!=0:
                cursor.execute("SELECT cedula, nombre, captahuella, rol, id FROM web_usuarios where cedula=%s", (datosusuario_huella[0][0],))
                datosUsuario = cursor.fetchall()
                cedula=datosUsuario[0][0]
                nombre=datosUsuario[0][1]
                permisoAperturaHuella = datosUsuario[0][2]
                rol=datosUsuario[0][3]
                usuario_id=datosUsuario[0][4]
                cursor.execute('SELECT * FROM web_horariospermitidos where usuario=%s', (usuario_id,))
                horarios_permitidos = cursor.fetchall()
                if horarios_permitidos != [] and permisoAperturaHuella == True and rol=='Secundario':
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    dia = caracas_now.weekday()
                    diahoy = dias_semana[dia]
                    for entrada, salida, _, dia in horarios_permitidos:
                        diasusuario.append(dia)
                    cantidaddias = diasusuario.count(dia)
                    for entrada, salida, _, dia in horarios_permitidos:
                        if 'Siempre' in diasusuario:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                            etapadiaapertura=1
                        elif dia==diahoy and cantidaddias==1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                        elif dia==diahoy and cantidaddias>1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                                    #print('fuera de horario')
                    if etapadia==0 and etapadiaapertura==0:
                        aperturadenegada(cursor, conn, acceso_solicitud)
                        #print('Dia no permitido')
                elif rol=='Propietario' and permisoAperturaHuella == True:
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    hora=str(caracas_now)[11:19]
                    horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                    fecha=str(caracas_now)[:10]
                    aperturaconcedidahuella(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                else:
                    aperturadenegada(cursor, conn, acceso_solicitud)
                # if horarios_permitidos == []:
                #     aperturadenegada(cursor, conn, acceso_solicitud)
                #     #print('este usuario no tiene horarios establecidos')
                diasusuario=[]
            else:
                aperturadenegada(cursor, conn, acceso_solicitud)

        if len(peticion) == 4 and peticion[3] == "seguricel_rfid_activo":
            self.send_response(200)
            self.send_header("Content-type", "utf-8")
            self.end_headers()
            # self.wfile.write(bytes(f"{self.path[1::]}", "utf-8"))
            epc, acceso_solicitud, razonApertura, _ = peticion
            diasusuario = []
            etapadia=0
            etapadiaapertura=0
            cantidaddias = 0
            contadoraux = 0
            cursor.execute("SELECT cedula FROM web_tagsrfid where epc=%s", (epc,))
            datosusuario_rfid = cursor.fetchall()
            #print(datosusuario)
            if len(datosusuario_rfid)!=0:
                cursor.execute("SELECT cedula, nombre, rfid, rol, id  FROM web_usuarios where cedula=%s", (datosusuario_rfid[0][0],))
                datosUsuario = cursor.fetchall()
                cedula=datosUsuario[0][0]
                nombre=datosUsuario[0][1]
                permisoAperturaRFID = datosUsuario[0][2]
                rol=datosUsuario[0][3]
                usuario_id=datosUsuario[0][4]
                cursor.execute('SELECT * FROM web_horariospermitidos where usuario=%s', (usuario_id,))
                horarios_permitidos = cursor.fetchall()
                if horarios_permitidos != [] and permisoAperturaRFID == True and rol=='Secundario':
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    dia = caracas_now.weekday()
                    diahoy = dias_semana[dia]
                    for entrada, salida, _, dia in horarios_permitidos:
                        diasusuario.append(dia)
                    cantidaddias = diasusuario.count(dia)
                    for entrada, salida, _, dia in horarios_permitidos:
                        if 'Siempre' in diasusuario:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                            etapadiaapertura=1
                        elif dia==diahoy and cantidaddias==1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(cursor, conn, acceso_solicitud)
                                    #print('fuera de horario')
                        elif dia==diahoy and cantidaddias>1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(cursor, conn, acceso_solicitud)
                                        contadoraux=0
                                    #print('fuera de horario')
                    if etapadia==0 and etapadiaapertura==0:
                        aperturadenegada(cursor, conn, acceso_solicitud)
                        #print('Dia no permitido')
                elif rol=='Propietario' and permisoAperturaRFID == True:
                    tz = pytz.timezone('America/Caracas')
                    caracas_now = datetime.now(tz)
                    hora=str(caracas_now)[11:19]
                    horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                    fecha=str(caracas_now)[:10]
                    aperturaconcedidarfid(nombre, fecha, horahoy, CONTRATO, cedula, cursor, conn, acceso_solicitud, razonApertura)
                else:
                    aperturadenegada(cursor, conn, acceso_solicitud)    
                # if horarios_permitidos == []:
                #     aperturadenegada(cursor, conn, acceso_solicitud)
                #     #print('este usuario no tiene horarios establecidos')
                diasusuario=[]
            else:
                aperturadenegada(cursor, conn, acceso_solicitud)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    while True:

        t11=time.perf_counter()
        while total<=5:
            t22=time.perf_counter()
            total=t22-t11
        total=0
        try:
            conn = psycopg2.connect(
                database=os.environ.get("DATABASE"),
                user=os.environ.get("USERDB"),
                password=os.environ.get("PASSWORD"),
                host=os.environ.get("HOST"),
                port=os.environ.get("PORT")
            )
            cursor = conn.cursor()
            webServer.serve_forever()
            print("fallo server")
        except (Exception, psycopg2.Error, KeyboardInterrupt) as error:
            print("fallo en hacer las consultas")
            total=0
        finally:
            print("se ha cerrado la conexion a la base de datos")
            print("Server stopped.")
            if conn:
                cursor.close()
                conn.close()
                total=0
            webServer.server_close()