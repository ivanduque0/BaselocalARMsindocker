import telebot
import time
import psycopg2
import os
import pytz
from datetime import datetime
from keyboa import Keyboa
import urllib.request
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/BaselocalARMsindocker/.env.manager')
load_dotenv(dotenv_path=dotenv_path)

dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
ultimahora = datetime.strptime('23:59:59', '%H:%M:%S').time()
primerahora = datetime.strptime('00:00:00', '%H:%M:%S').time()
token=os.environ.get("TOKEN_BOT")
bot = telebot.TeleBot(token, parse_mode=None)
total=0
CONTRATO=os.environ.get("CONTRATO")
conn = None
cursor = None

razon1=os.environ.get("RAZON_BOT1")
razon2=os.environ.get("RAZON_BOT2")
razon3=os.environ.get("RAZON_BOT3")
razon4=os.environ.get("RAZON_BOT4")

acceso1=os.environ.get('URL_ACCESO1')
acceso2=os.environ.get('URL_ACCESO2')
acceso3=os.environ.get('URL_ACCESO3')
acceso4=os.environ.get('URL_ACCESO4')
# pulseaqui = [
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
#     'pulse aqui',
    
# ]

# keyboard = Keyboa(items=pulseaqui)

markup = telebot.types.ReplyKeyboardMarkup()
markup.add("π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅\nπ΅π΅π΅π΅ENTRADA PRINCIPALπ΅π΅π΅π΅\nπ΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅")
markup.add("π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄\nπ΄π΄π΄π΄PORTON VEHICULARπ΄π΄π΄π΄\nπ΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄")
markup.add("πΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆ\nπΆπΆπΆπΆ PUERTA TRASERA πΆπΆπΆπΆ\nπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆ")

opciones = ['''π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅
π΅π΅π΅π΅ENTRADA PRINCIPALπ΅π΅π΅π΅
π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅''','''π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄
π΄π΄π΄π΄PORTON VEHICULARπ΄π΄π΄π΄
π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄π΄''','''πΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆ
πΆπΆπΆπΆ PUERTA TRASERA πΆπΆπΆπΆ
πΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆπΆ''']

markupentradaprincipal = telebot.types.InlineKeyboardMarkup()
markupentradaprincipal.add(telebot.types.InlineKeyboardButton(text='ABRIR ENTRADA PRINCIPAL', callback_game=''))
markupportonvehicular = telebot.types.InlineKeyboardMarkup()
markupportonvehicular.add(telebot.types.InlineKeyboardButton(text='ABRIR PORTON VEHICULAR', callback_game=''))
markuppuertatrasera = telebot.types.InlineKeyboardMarkup()
markuppuertatrasera.add(telebot.types.InlineKeyboardButton(text='ABRIR PUERTA TRASERA', callback_game=''))

def aperturaconcedida(nombref, fechaf, horaf, razonf, contratof, cedulaf, cursorf, connf, acceso):
    cursorf.execute('''INSERT INTO web_interacciones (nombre, fecha, hora, razon, contrato, cedula_id)
    VALUES (%s, %s, %s, %s, %s, %s);''', (nombref, fechaf, horaf, razonf, contratof, cedulaf))
    #cursorf.execute('UPDATE led SET onoff=1 WHERE onoff=0;')
    connf.commit()
    urllib.request.urlopen(f'{acceso}/on')


#def aperturadenegada(cursorf, connf, acceso):
    #cursorf.execute('UPDATE led SET onoff=2 WHERE onoff=0;')
    #connf.commit()
    
def aperturadenegada(acceso):
    urllib.request.urlopen(f'{acceso}/off')

@bot.message_handler(commands=['id'])
def send_welcome(message):
    message.text
    chatid = message.chat.id
    bot.reply_to(message, f"su ID es: {chatid}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    message.text
    chatid = message.chat.id
    #bot.send_message(chat_id=chatid,text='Pulse cualquier boton', reply_markup=keyboard())
    bot.send_game(chat_id=chatid, game_short_name='entrada_principal', reply_markup=markupentradaprincipal)
    bot.send_game(chat_id=chatid, game_short_name='porton_vehicular', reply_markup=markupportonvehicular)
    bot.send_game(chat_id=chatid, game_short_name='puerta_trasera', reply_markup=markuppuertatrasera)
    bot.send_message(chat_id=chatid,text='que acceso desea abrir?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def manejador_seleccion(call):

    chat_id = call.message.chat.id
    orden = call.game_short_name

    
    # if call.data == 'pulse aqui':
    #     markup = telebot.types.ReplyKeyboardMarkup()
    #     markup.add("entrada principal")
    #     markup.add("porton vehicular","puerta trasera")
    #     bot.send_message(chat_id=chatid,text='Pulse cualquier boton', reply_markup=keyboard())
    #     bot.send_message(chat_id=chatid,text='que acceso desea abrir?', reply_markup=markup)
    if orden == 'entrada_principal':
        diasusuario = []
        etapadia=0
        etapadiaapertura=0
        cantidaddias = 0
        contadoraux = 0
        cursor.execute("SELECT * FROM web_usuarios where telegram_id='%s'", (chat_id,))
        datosusuario = cursor.fetchall()
        #print(datosusuario)
        if len(datosusuario)!=0:
            cedula=datosusuario[0][0]
            nombre=datosusuario[0][1]
            cursor.execute('SELECT * FROM web_horariospermitidos where cedula_id=%s', (cedula,))
            horarios_permitidos = cursor.fetchall()
            if horarios_permitidos != []:
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
                        aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                        etapadiaapertura=1
                    elif dia==diahoy and cantidaddias==1:
                        hora=str(caracas_now)[11:19]
                        horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                        fecha=str(caracas_now)[:10]
                        etapadia=1
                        if entrada<salida:
                            if horahoy >= entrada and horahoy <= salida:
                                #print('entrada concedida')
                                aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                etapadiaapertura=1
                            else:
                                aperturadenegada(acceso1)
                                #print('fuera de horario')
                        if entrada>salida:
                            if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                #print('entrada concedida')
                                aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                etapadiaapertura=1
                            else:
                                aperturadenegada(acceso1)
                                #print('fuera de horario')
                    elif dia==diahoy and cantidaddias>1:
                        hora=str(caracas_now)[11:19]
                        horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                        fecha=str(caracas_now)[:10]
                        etapadia=1
                        if entrada<salida:
                            if horahoy >= entrada and horahoy <= salida:
                                #print('entrada concedida')
                                aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                etapadiaapertura=1
                                contadoraux=0
                            else:
                                contadoraux = contadoraux+1
                                if contadoraux == cantidaddias:
                                    aperturadenegada(acceso1)
                                    contadoraux=0
                        if entrada>salida:
                            if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                #print('entrada concedida')
                                aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                etapadiaapertura=1
                                contadoraux=0
                            else:
                                contadoraux = contadoraux+1
                                if contadoraux == cantidaddias:
                                    aperturadenegada(acceso1)
                                    contadoraux=0
                                #print('fuera de horario')
                if etapadia==0 and etapadiaapertura==0:
                    aperturadenegada(acceso1)
                    #print('Dia no permitido')
            if horarios_permitidos == []:
                aperturadenegada(acceso1) 
                #print('este usuario no tiene horarios establecidos')
            diasusuario=[]
        else:
            aperturadenegada(acceso1)   
@bot.message_handler(func=lambda message: True)
def manejador_seleccion(message):
	
    chatid=message.chat.id
    messageid=message.id
    try:
        opciones.index(message.text)
        #print(message.text)
        if message.text == "π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅\nπ΅π΅π΅π΅ENTRADA PRINCIPALπ΅π΅π΅π΅\nπ΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅π΅":
            diasusuario = []
            etapadia=0
            etapadiaapertura=0
            cantidaddias = 0
            contadoraux = 0
            chat_id = chatid
            cursor.execute("SELECT * FROM web_usuarios where telegram_id='%s'", (chat_id,))
            datosusuario = cursor.fetchall()
            #print(datosusuario)
            if len(datosusuario)!=0:
                cedula=datosusuario[0][0]
                nombre=datosusuario[0][1]
                cursor.execute('SELECT * FROM web_horariospermitidos where cedula_id=%s', (cedula,))
                horarios_permitidos = cursor.fetchall()
                if horarios_permitidos != []:
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
                            aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                            etapadiaapertura=1
                        elif dia==diahoy and cantidaddias==1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(acceso1)
                                    #print('fuera de horario')
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                    etapadiaapertura=1
                                else:
                                    aperturadenegada(acceso1)
                                    #print('fuera de horario')
                        elif dia==diahoy and cantidaddias>1:
                            hora=str(caracas_now)[11:19]
                            horahoy = datetime.strptime(hora, '%H:%M:%S').time()
                            fecha=str(caracas_now)[:10]
                            etapadia=1
                            if entrada<salida:
                                if horahoy >= entrada and horahoy <= salida:
                                    #print('entrada concedida')
                                    aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(acceso1)
                                        contadoraux=0
                            if entrada>salida:
                                if (horahoy>=entrada and horahoy <=ultimahora) or (horahoy>=primerahora and horahoy <= salida):
                                    #print('entrada concedida')
                                    aperturaconcedida(nombre, fecha, horahoy, razon1, CONTRATO, cedula, cursor, conn, acceso1)
                                    etapadiaapertura=1
                                    contadoraux=0
                                else:
                                    contadoraux = contadoraux+1
                                    if contadoraux == cantidaddias:
                                        aperturadenegada(acceso1)
                                        contadoraux=0
                                    #print('fuera de horario')
                    if etapadia==0 and etapadiaapertura==0:
                        aperturadenegada(acceso1)
                        #print('Dia no permitido')
                if horarios_permitidos == []:
                    aperturadenegada(acceso1) 
                    #print('este usuario no tiene horarios establecidos')
                diasusuario=[]
               
            else:
                aperturadenegada(acceso1) 
    except:
        pass
    finally:
        bot.delete_message(chat_id=chatid, message_id=messageid)

            

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
        bot.polling(skip_pending=True)
        bot.stop_polling()
        


    except (Exception, psycopg2.Error) as error:
        print("fallo en hacer las consultas")
        total=0

    finally:
        print("se ha cerrado la conexion a la base de datos")
        if conn:
            cursor.close()
            conn.close()
            total=0


