def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

myserial = getserial ()

import time
import bme280
import requests
temperature,pressure,humidity = bme280.readBME280All()

data ={'temp':temperature, 'pressure':pressure, 'humidity':humidity}
url = 'https://myblackmirror.pl/api/v1/receive_data/sensor/'+str(myserial)
headers = {'content-length': '108','Content-Type': 'application/json'}

req = requests.post(url, headers=headers, json=data)

