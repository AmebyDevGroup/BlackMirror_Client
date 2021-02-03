#import required libraries
import time
import cv2
import requests

#if using the picamera, import those libraries as well
from picamera.array import PiRGBArray
from picamera import PiCamera

#Get serial number form cpu 
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


#point to the haar cascade file in the directory
faceCascade = cv2.CascadeClassifier(
    'Cascades/haarcascade_frontalface_default.xml')
#start the camera and define settings
camera = PiCamera()
camera.resolution = (320, 240) #a smaller resolution means faster processing
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

#give camera time to warm up
time.sleep(0.5)
t = 15
i = 0

# start video frame capture
for still in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # take the frame as an array, convert it to black and white, and look for facial features
        image = still.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
                image,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize=(30, 30),
        )

        secs = t
        t -= 1

        if len(faces) == 0:
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
                for(x,y,w,h) in faces:
                         i = i+1
            t = 15

        # clear the stream capture
        rawCapture.truncate(0)

        #set "q" as the key to exit the program when pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break
