import time 
from machine import Pin

LED = Pin(4, Pin. OUT)  #Se crea el objeto LED, configurando GPIO4 LED externo
Pul = Pin(5, Pin. IN)  #Se crea el objeto Pul, GPIO5 pulsador
estado = 0
a=4
b=3

while True:  
  boton = Pul.value()
  LED.value(boton)  #obtener el estado del pulsador y transferirlo a LED
  print("El estado de pul es: %s" % str(boton))
  
  if(boton & estado == 0):      
      sum = a ^ b
      c = sum
      estado = 1
 
  if (boton & estado ==1):
   neg = ~ c
   estado = 0
  
  
