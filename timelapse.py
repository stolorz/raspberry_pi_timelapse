#import libraries
from picamera import PiCamera
import time
from fractions import Fraction
from datetime import datetime, timedelta
import subprocess
import os


#Set up variables:
interval = 1
output_folder = '/home/pi/Sync/timelapse'


#Set up & start camera, & let it settle
camera = PiCamera()
PiCamera.CAPTURE_TIMEOUT = 600 # seconds
camera.resolution = (4056, 3040)
camera.hflip = True
camera.vflip = True
camera.awb_mode = "sunlight"
#camera.image_effect = "none"
#camera.shutter_speed = 6000000
#camera.sensor_mode=3
#camera.exposure_mode = 'off'
camera.exposure_mode = "verylong"
#camera.shutter_speed = 6000000
camera.framerate = Fraction(1,500)
camera.iso = 100

time.sleep(2)


for filename in camera.capture_continuous('/tmp/{timestamp:%Y-%m-%d_%H-%M-%S}.jpg', quality=85):
    print('Captured %s' % filename)
    print(os.path.basename(filename))
    filename_out = "{folder}/{file}".format(folder=output_folder, file=os.path.basename(filename))
    cmd = "convert {f1} -quality 85 {f2} && rm {f1}".format(f1=filename, f2=filename_out)
    subprocess.run(cmd, shell=True)
    time.sleep(interval)


#while True:
#    output_filename = '{0}/{1}_iso_{2}.jpg'.format(output_folder, time.strftime("%Y%m%d-%H%M%S"), camera.iso)
#    camera.capture( output_filename, quality=65)
#    time.sleep(interval)
