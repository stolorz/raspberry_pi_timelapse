# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (4056, 3040)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(4056, 3040))

# allow the camera to warmup
time.sleep(0.1)

counter = 0;

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = rawCapture.array

    cv2.imwrite("/home/pi/Sync/timelapse/xxx_{0}.jpg".format(counter), image)
    counter += 1

    # show the frame
    # cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    time.sleep(10)
