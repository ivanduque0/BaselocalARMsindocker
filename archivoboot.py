import os

comandos = [
    "python3.7 /BaselocalARMsindocker/dbmaker/codigo.py &",
    "python3.7 /BaselocalARMsindocker/dbmanagerall/codigo.py &",
    # "python3.7 /BaselocalARMsindocker/dbmanagerusuarios/codigo.py &",
    # "python3.7 /BaselocalARMsindocker/dbmanagerhorarios/codigo.py &",
    # "python3.7 /BaselocalARMsindocker/dbmanagertelegramid/codigo.py &",
    # "python3.7 /BaselocalARMsindocker/dbmanagerinteracciones/codigo.py &",
    #"python3.7 /BaselocalARMsindocker/botelegram/codigo.py &",
    "python3.7 /BaselocalARMsindocker/servidorlocalwifi/codigo.py &"
    #"python3.7 /BaselocalARMsindocker/pingdispositivos/codigo.py &",
]

for x in comandos:
    os.system(x)

print('hecho!')