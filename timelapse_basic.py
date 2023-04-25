#import libraries
from picamera import PiCamera
import time

#Set up variables:
interval = 1


#Set up & start camera, & let it settle
camera = PiCamera()
camera.resolution = (4056, 3040)
camera.rotation = 180
#camera.start_preview()
time.sleep(2)

while True:
    camera.capture('/home/pi/Sync/timelapse/' + time.strftime("%Y%m%d-%H%M%S") + '.jpg' )
    time.sleep(interval)
