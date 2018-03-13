import time 
from machine import Pin
LED = Pin(4, Pin. OUT)  #Se crea el objeto LED, configurando GPIO4 LED externo
Pul = Pin(5, Pin. IN)  #Se crea el objeto Pul, GPIO5 pulsador


while True:
  boton = Pul.value()
  LED.value(boton)  #obtener el estado del pulsador y transferirlo a LED
  print("El estado de pul es: %s" % str(boton))
  time.sleep_ms(200)
  
  if (boton ):
    print ('ON')
  else:
      print('off')
  time.sleep_ms(200)    

