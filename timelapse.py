import time
from picamera2 import Picamera2, Preview

picam = Picamera2()

config = picam.create_preview_configuration()
picam.configure(config)

#picam.start_preview(Preview.QTGL)

interval = 15 
frame = 0

picam.start()
time.sleep(2)
picam.capture_file("test-python.jpg")

while True:
        picam.capture_file('/home/pi/Sync/timelapse/ice_%04d.jpg' % (frame))
        frame = frame + 1
        time.sleep(interval)

picam.close()


