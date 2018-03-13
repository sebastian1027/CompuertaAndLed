import socket 
import machine 


LED0 = machine.Pin(4, machine.Pin.OUT)

html = """ <!DOCTYPE html>
<html>
<body>
<head> <title> ESP8266 LED ON/OFF</title> </head>
<center><h1> Servidor web boton con micrpython</h1></center>
<center><h2>ESP8266</h2></center>
<div align="center">
<form>
LED GPIO 4
<input type="checkbox" name="LEDON" value="ON" type="submit">Verdadero?</button>
<input type="checkbox" name="LEDOFF" value="OFF" type="submit">Verdadero?</button>

<input type="submit" value="Enviar">
</form>
</div>
</body>
</html>
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Obtiendo conexion desde %s" % str(addr))
    request = conn.recv(1024)
    print("contiendo = %s" % str(request))
    request = str(request)
    true = request.find('/?LEDON=ON')
    false = request.find('/?LEDOFF=OFF')
    
    print("El valor de true es: ", true)
    print("El valor de false es: ", false)
    
    if   (true == 6 & false == 6):
          LED0.value(1)             # si los 2 estan seleccionados enciende el LED      
          
    elif ((true == 6 & false == -1) &  (true==6 & false==340)):
          LED0.value(0)             #Si uno de los 2 no esta seleccionado apaga o deja apagado el LED                
    
    elif (true == -1 & false == 6):
          LED0.value(0)             #Si uno de los 2 no esta seleccionado apaga o deja apagado el LED
          
    elif (true == -1 & false == -1):
          LED0.value(0)             #Si ninguno de los 2 esta seleccionado apaga o deja apagado el LED      
          
    else:
          LED0.value(0)             #Apague el LED
    
    
    response = html
    conn.send(response)
    conn.close()

    #if (true == 6 & false == -1):
    #    LED0.value(0)
    #if (true == -1 & false == 6):
    #    LED0.value(0)
    #if (true == 6 & false == 6):
    #    LED0.value(1)       
    #if (true == -1 & false == -1):
    #    LED0.value(0)






