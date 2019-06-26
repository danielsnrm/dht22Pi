"""
dht22.py
Temperature/Humidity monitor using Raspberry Pi and DHT22.
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in
Modified by Adam Garbo on December 1, 2016
"""
import sys
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import Adafruit_DHT
import urllib2
GPIO.setmode(GPIO.BCM)
myAPI = "myapi"
def printDateTime():
    now = datetime.now()
    return  ('[' + (now.strftime("%d/%m/%Y")) + ' - '  + (now.strftime("%H:%M:%S")) + ']')
def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
   return (str(RH), str(T))
def main():
    log = open ("/home/pi/ThingSpeak/dht.log", "a")
    print printDateTime() + ' Arrancando...'
    log.write(printDateTime() + ' Arrancando...' + '\n')
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    while True:
       try:
        print printDateTime() + ' Intentando obtener datos del sensor'
        log.write(printDateTime() + ' Intentando obtener datos del sensor' + '\n')
        RH, T = getSensorData()
        print printDateTime() + ' Intento (RH ,T): (' + str(RH) + ',' + str(T) + ')'
        log.write(printDateTime() + ' Intento (RH ,T): (' + str(RH) + ',' + str(T) + ')' + '\n')
        print printDateTime() + ' Se va a intentar subir los datos a ThingSpeak'
        log.write(printDateTime() + ' Se va a intentar subir los datos a ThingSpeak' + '\n')
        print ' Se utilizara: ' + baseURL + "&field1=%s&field2=%s" % (str(T),str(RH))
        log.write(printDateTime() + ' Se utilizara: ' + baseURL + "&field1=%s&field2=%s" % (str(T),str(RH)) + '\n')
        f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (str(T), str(RH)))
        print printDateTime() + ' Resultado: ' + f.read()
        log.write(printDateTime() + ' Resultado: ' + f.read() + '\n')
        f.close(900000)
        log.close
        sleep() #uploads DHT22 sensor values every 5 minutes (300)
       except:
        print printDateTime() + ' Se ha producido una excepcion. Se reinicia el proceso.'
        log.write(printDateTime() + ' Se ha producido una excepcion. Se reinicia el proceso.' + '\n')
# call main
if __name__ == '__main__':
   main()
