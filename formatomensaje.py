import requests

numero_enviar=584241346337
contrato='PORTAL ALAMEDA'
link='https://webseguricel.up.railway.app/inicio'
fecha='2023-02-23'
nombres=['Pedro Perez', 'Alejandro Gonzales', 'Ernesto Villa']

for nombre in nombres:
    mensaje=f'INVITACION PARA {contrato}\n\nFecha:{fecha}\nNombre: {nombre}\nCodigo: 123456\n\nLinks de descarga: \n\nAndroid={link}\n\niOs={link}'
    request_mensaje = requests.get(url=f'http://api.callmebot.com/whatsapp.php?phone=584122810793&text=!sendto+{numero_enviar}+{mensaje}&apikey=5525175', timeout=3)
    # request_mensaje = requests.get(url=f'http://api.callmebot.com/whatsapp.php?phone=584122810793&text=!sendto+{numero_enviar}+{mensaje}&apikey=5525175', timeout=3)
    print(request_mensaje)