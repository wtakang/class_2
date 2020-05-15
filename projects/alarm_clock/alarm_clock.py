#!/home/tanyi/development/pythonclass/class_2/projects/alarm_clock/bin/python3

from time import sleep
from datetime import datetime
import winsound

def set_alarm():
    print('your current time is:',datetime.now().strftime('%H:%M')) # print the current time to the user before the alarm
    
    min = int(input("Enter number of minutes to set the alarm: "))# get the users alarm time in minutes
 
 
    sec = min * 60 # convert the minutes to seconds
 
    if min >= 0:
        if min == 1:
            print("Alarm will ring in " + str(min) + ' minute')
            sleep(sec) #make the script to wait for the number of serconds
            print("Get up!")
            winsound.Beep(1500, 5000)# beep to wake up the user as alarm
        else:
            print("Alarm will ring in " + str(min) + ' minutes')
            sleep(sec)
            print("Get up!")
            winsound.Beep(1500, 5000)
 
    else:
        print("Please enter valid value!")
 

set_alarm()