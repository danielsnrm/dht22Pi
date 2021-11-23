#!/usr/bin/python
"""
dht22.py
Temperature/Humidity monitor using Raspberry Pi and DHT22.
Coded by Daniel Sánchez
based on Adam Gargo thingspeak script.
November 2021
"""
import sys
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

myAPI = "myapi"

def printDateTime():
    now = datetime.now()
    return  ('[' + (now.strftime("%d/%m/%Y")) + ' - '  + (now.strftime("%H:%M:%S")) + ']')
def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
   return (str(RH), str(T))
def main():
    log = open ("/home/pi/Documents/logs/dht22.log", "a")
    print(printDateTime() + ' Arrancando...')
    log.write(printDateTime() + ' Arrancando...' + '\n')
    
    while True:
       try:
        print(printDateTime() + ' Intentando obtener datos del sensor')
        log.write(printDateTime() + ' Intentando obtener datos del sensor' + '\n')
        RH, T = getSensorData()
        print(printDateTime() + ' Intento (RH ,T): (' + str(RH) + ',' + str(T) + ')')
        log.write(printDateTime() + ' Intento (RH ,T): (' + str(RH) + ',' + str(T) + ')' + '\n')
        log.write(printDateTime() + ' Resultado: ' + f.read() + '\n')
        log.close
        sleep() #uploads DHT22 sensor values every 5 minutes (300)
       except:
        print(printDateTime() + ' Se ha producido una excepcion. Se reinicia el proceso.')
        log.write(printDateTime() + ' Se ha producido una excepcion. Se reinicia el proceso.' + '\n')
# call main
if __name__ == '__main__':
   main()
