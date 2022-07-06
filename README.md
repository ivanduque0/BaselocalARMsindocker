# BaselocalARMsindocker
Este repositorio corresponde a la baselocal que hay que clonar a dispositivos Armv7l que no se les pueda instalar docker, 
aunque tambien funciona con cualquier dispositivo con arquitectura ARM que tenga linux

instalar git
sudo apt-get install git

instalar postgres
sudo apt-get install postgresql postgresql-contrib

instalar python3.7
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
sudo tar xzf Python-3.7.3.tgz
cd Python-3.7.3
sudo ./configure --enable-optimizations
sudo make altinstall

poder instalar con pip
pip3.7 install package_name --user

instalar psycopg2
sudo apt-get install libpq-dev
pip3.7 install psycopg2

instalar pytelegrambotapi
ver su repositorio de github o desde pypi

instalar python-dotenv
pip3.7 install python-dotenv

----------------------------------

instalar nodejs
https://nodejs.org/download/release/v16.15.1/node-v16.15.1-linux-armv7l.tar.gz
tar -xzf node-v16.15.1-linux-armv7l.tar.gz
cd node-v16.15.1-linux-armv7l/
sudo cp -R * /usr/local/
node -v

-------------------------------------------------

instalar heroku
wget https://cli-assets.heroku.com/heroku-linux-arm.tar.gz
mkdir -p /usr/local/lib /usr/local/bin
sudo tar -xvzf heroku-linux-arm.tar.gz -C /usr/local/lib
sudo ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku
heroku version

---------------------------------------------

crear base de datos y usuario en postgresql
CREATE DATABASE tesis;
CREATE ROLE tesis WITH LOGIN CREATEDB CREATEROLE CREATEUSER INHERIT ENCRYPTED PASSWORD 'tesis';

--------------------------------------------

pasos para crear el bot

crear el bot con las instrucciones de botfather
primero se le introduce el nombre del bot, este nombre sera el que saldra
en el chat
seleccionar un username, este sera con el que se bscara al bot. Ejemplo: avilavilla_bot

----------------------------------------

foto de perfil del bot:

introducir el comando /setuserpic
seleccionar el bot
enviar la imagen
ejecutar /setinline
seleccionar el bot
enviarle el comando para inline. Ejemplo: accesos

------------------------------------------------

crear juegos para los accesos:

ingresar el nombre del juego. Ejemplo: PUERTA PRINCIPAL
ingresar una descripcion. Ejemplo PUERTA PRINCIPAL
subir la foto
ejecutar /empty si no se quiere poner un gift
INTRODUCIR EL "short name", este es el que va a ir en el codigo!!. Ejemplo: puerta_principal



-------------------------------------------

MUY IMPORTANTE!!!!!!!!!!

para que se pueda iniciar bien el script en python en rc.local, se debe 
editar el archivo /usr/local/bin/heroku
en la linea 18 se debe 
reemplazar $(cd && pwd) por la ruta al usuario en la carpeta home "/home/orangepi"

esto debido a que cuando corre directamente desde /etc/rc.local al parecer no se 
tiene acceso a la ruta

para hacer que el script corra al iniciar la orangepi

se debe editar el archivo /etc/rc.local y se debe 
escribir 
/usr/local/bin/python3.7 /BaselocalARMsindocker/archivoboot.py




se debe clonar el repositiorio con los codigo en la carpeta raiz
