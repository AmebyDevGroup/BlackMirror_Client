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


import json
import os

# Data to be written
dictionary ={
    "SN" : myserial
}
# Serializing jso
json_object = json.dumps(dictionary, indent = 4)
# Writing to sample.json
with open(os.path.join('/var/www/html/',"sn.json"), "w") as outfile:
    outfile.write(json_object)
