#import libraries
from picamera import PiCamera
import time
from fractions import Fraction
from datetime import datetime, timedelta
import subprocess
import os
import pathlib


def is_between(datetime, time_range):
    time_str = time.strftime("%H:%M:%S", datetime)
    if time_range[1] < time_range[0]:
        return time_str >= time_range[0] or time_str <= time_range[1]
    return time_range[0] <= time_str <= time_range[1]

def is_night():
    return is_between(time.localtime(), ("22:00:00", "02:00:00"))

#Set up variables:
sleep_interval_day = 1
sleep_interval_night = 300
output_folder_base = '/home/pi/Sync/timelapse'


#Set up & start camera, & let it settle
camera = PiCamera()
PiCamera.CAPTURE_TIMEOUT = 600 # seconds
camera.resolution = (4056, 3040)
camera.led = False # make sure that led is off
camera.hflip = True
camera.vflip = True
camera.awb_mode = "sunlight"
camera.image_effect = "none"
#camera.shutter_speed = 6000000
#camera.exposure_mode = 'off'
camera.exposure_mode = "verylong"
camera.framerate = Fraction(1,500)
camera.iso = 100
camera.sensor_mode = 3
camera.meter_mode = 'matrix' # when tested in trier, this gave best results
time.sleep(2)


for filename in camera.capture_continuous('/tmp/{timestamp:%Y-%m-%d_%H-%M-%S}.jpg', format='jpeg', quality=85, use_video_port=True):
    print('Captured %s' % filename)
    print(os.path.basename(filename))
    output_folder = "{base}/{hour}".format(base=output_folder_base, hour=time.strftime("%Y%m%d-%H"))
    pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)
    filename_out = "{folder}/{file}".format(folder=output_folder, file=os.path.basename(filename))
    cmd = "convert {f1} -quality 85 {f2} && rm {f1}".format(f1=filename, f2=filename_out)
    subprocess.run(cmd, shell=True)
    sleep_interval = sleep_interval_night if is_night() else sleep_interval_day
    time.sleep(sleep_interval)


#while True:
#    output_filename = '{0}/{1}_iso_{2}.jpg'.format(output_folder, time.strftime("%Y%m%d-%H%M%S"), camera.iso)
#    camera.capture( output_filename, quality=65)
#    time.sleep(interval)
