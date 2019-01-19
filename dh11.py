#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print '{0:s}\t{1:0.1f} C\t{2:0.1f} %'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity)
    time.sleep(60)
