#import libraries
import picamera 
import numpy as np
import time
from PIL import Image

#Set up variables:
interval = 1


#Set up & start camera, & let it settle
camera = picamera.PiCamera()
camera.resolution = (4056, 3040)
camera.rotation = 180
#camera.start_preview()
time.sleep(2)

output = picamera.array.PiRGBArray(camera)

while True:
    output_filename = '/home/pi/Sync/timelapse/' + time.strftime("%Y%m%d-%H%M%S") + '.jpg'
    camera.capture(output, 'rgb')
    im = Image.fromarray(output)
    im.save(filename)
    time.sleep(interval)
