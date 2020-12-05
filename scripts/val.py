#!/usr/bin/python
import time
import bme280
while True:
	temperature,pressure,humidity = bme280.readBME280All()
	print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperature, pressure, humidity))
	time.sleep(5)
