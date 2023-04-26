#!/bin/bash

counter=0

log_folder="/home/pi/Sync/timelapse"

while true
do
printf -v log_filename "${log_folder}/log_%(%Y-%m-%d_%H-%M-%S)T.txt" -1
echo "starting timelapse python script ${counter}" >> "${log_filename}"
echo -e "current ifconfig:\n" >> "${log_filename}"
ifconfig >> "${log_filename}"
((counter+=1))
python3 timelapse.py
sleep 1
done
