import time 
from machine import Pin

a= 4
b = 3

while True:
  
  Y = a & b
  O = a | b
  neg = ~ a 
  sum = a ^ b
  print ('la AND es %s: ' %str(Y))
  time.sleep_ms(250)
  print ('la OR es %s: ' %str(O))
  time.sleep_ms(250)
  print ('la NOT es %s: ' %str(neg))
  time.sleep_ms(250)
  print ('la XOR es %s: ' %str(sum))
  time.sleep_ms(250)

