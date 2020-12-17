import numpy as np
import cv2
import time
import requests

def getserial():
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial

myserial = getserial()

faceCascade = cv2.CascadeClassifier(
    'Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

t = 15

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    secs = t
    time.sleep(1)
    t -= 1

    if type(faces) == tuple:
        if t == 0:
            data = {'turnOff': True}
            url = 'https://myblackmirror.pl/api/v1/receive_data/camera/'+str(myserial)
            headers = {'content-length': '108','Content-Type': 'application/json'}
            req = requests.post(url, headers=headers, json=data)

    else:
        if t < 0:
            data = {'turnOff': False}
            url = 'https://myblackmirror.pl/api/v1/receive_data/camera/'+str(myserial)
            headers = {'content-length': '108','Content-Type': 'application/json'}
            req = requests.post(url, headers=headers, json=data)
        t = 15

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
