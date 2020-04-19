import RPi.GPIO as GPIO
import dht11
import time
import datetime
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

x=datetime.datetime.now()

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
       # print ('Hour',a,'Minute',s,'Second',d)
        f = open ('Temp and Humid.txt', 'a')
        f.write (datetime.datetime.now().ctime())
        f.write (" Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity +'\n')
        f.close()






