#!/bin/bash

# disable led on the webcam
#uvcdynctrl -s 'LED1 Mode' 0

# test focus full spectrum 0-250, reasonable is 40 (+-10)
counter=30
while [ $counter -le 55 ]
do
fswebcam \
 --device V4L2:/dev/video0 \
 --input 0 \
 --quiet \
 --resolution 1920x1080 \
 --rotate 180 \
 --set "LED1 Mode"=Off \
 --set "White Balance Temperature"=5000 \
 --set "Focus, Auto"=False \
 --set "Focus (absolute)"=$counter \
 --delay 3 \
 --skip 3 \
 --frames 60 \
 --title $counter \
 --save /home/pi/Sync/timelapse/test_focus_$(printf "%03d" $counter)_%Y-%m-%d_%H-%M-%S.jpg
((counter+=5))
done

#disable autofocus
v4l2-ctl -d /dev/video0 -c focus_auto=0
v4l2-ctl -d /dev/video0 -c focus_absolute=35

# start timelapse loop
fswebcam \
 --device V4L2:/dev/video0 \
 --input 0 \
 --loop 60 \
 --resolution 1920x1080 \
 --rotate 180 \
 --delay 3 \
 --skip 5 \
 --jpeg 98 \
 --frames 60 \
 --no-banner \
 --set "LED1 Mode"=Off \
 --set "White Balance Temperature"=5000 \
 --set "Backlight Compensation"=0 \
 --quiet \
 --save /home/pi/Sync/timelapse/%Y-%m-%d_%H-%M-%S.jpg
