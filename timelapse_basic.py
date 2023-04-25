#import libraries
from picamera import PiCamera
import time

#Set up variables:
interval = 1
output_folder = '/home/pi/Sync/timelapse/'


#Set up & start camera, & let it settle
camera = PiCamera()
camera.resolution = (4056, 3040)
camera.hflip = True
camera.vflip = True
camera.awb_mode = "sunlight"

#camera.start_preview()
time.sleep(2)


iso = 1

while True:
    camera.iso = iso
    output_filename = '{0}/{1}_iso_{2}.jpg'.format(output_folder, time.strftime("%Y%m%d-%H%M%S"), iso)
    camera.capture( output_filename )
    iso *=2
    time.sleep(interval)
