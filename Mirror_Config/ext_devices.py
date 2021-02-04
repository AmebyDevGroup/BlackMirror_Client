from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
import RPi.GPIO as GPIO
import time
import bme280
import requests
from git import Repo
from distutils import dir_util
import os

def getserial():
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


def sensor():
	temperature,pressure,humidity = bme280.readBME280All()
	data ={'temp':temperature, 'pressure':pressure, 'humidity':humidity}
	url = 'https://myblackmirror.pl/api/v1/receive_data/sensor/'+str(myserial)
	headers = {'content-length': '108','Content-Type': 'application/json'}
	req = requests.post(url, headers=headers, json=data)


def status_backlight():
	data = {'status': 'on'}
	url = 'https://myblackmirror.pl/api/v1/receive_data/backlight/' + str(myserial)
	headers = {'content-length': '108', 'Content-Type': 'application/json'}
	req = requests.post(url, headers=headers, json=data)


#--------------------------FLASK API -------------------------------#


app = Flask(__name__)
scheduler = APScheduler()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

@app.route('/switchBacklight/<status>', methods=['GET'])
def switch_backlight(status):
	if status == "on":
		GPIO.output(21, GPIO.LOW)
		data = {'status':'on'}
		url = 'https://myblackmirror.pl/api/v1/receive_data/backlight/' + str(myserial)
		headers = {'content-length': '108', 'Content-Type': 'application/json'}
		req = requests.post(url, headers=headers, json=data)
		return jsonify({"message": "LED IS ON"})
	elif status == "off":
		GPIO.output(21, GPIO.HIGH)
		data = {'status': 'off'}
		url = 'https://myblackmirror.pl/api/v1/receive_data/backlight/' + str(myserial)
		headers = {'content-length': '108', 'Content-Type': 'application/json'}
		req = requests.post(url, headers=headers, json=data)
		return jsonify({"message": "LED IS OFF"})
	else:
		return jsonify({"message": "Not a valid status"})


@app.route('/system/update', methods=['GET'])
def web():
    dir_util.mkpath('temp')
    dir_util.remove_tree('temp')
    Repo.clone_from('https://github.com/AmebyDevGroup/BlackMirror_Client.git', 'temp')
    dir_util.remove_tree('/var/www/html')
    dir_util.copy_tree('temp/dist', "/var/www/html")
    dir_util.remove_tree('temp')
    os.system('sudo shutdown -r 1')
    return jsonify({"message": "SYSTEM UPDATED"})

if __name__ == '__main__':
    scheduler.add_job(id = 'sensor', func=sensor, trigger="interval", minutes=15)
    scheduler.start()
    status_backlight()
    app.run(host='0.0.0.0')
