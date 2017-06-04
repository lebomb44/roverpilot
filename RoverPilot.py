#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO

def setDC(dc, step):
    dc = dc +step
    if 100 < dc:
        dc = 100
    if 0 > dc:
        dc = 0
    return dc

# Use GPIO number like GPIOXX
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo Front - Back
FRONT_BACK_PIN = 22
GPIO.setup(FRONT_BACK_PIN, GPIO.OUT)
pilotFrontBack = GPIO.PWM(FRONT_BACK_PIN, 50)  # frequency=50Hz
pilotFrontBack_DC = 50
pilotFrontBack.start(pilotFrontBack_DC)

# Servo Left - Right
LEFT_RIGHT_PIN = 23
GPIO.setup(LEFT_RIGHT_PIN, GPIO.OUT)
pilotLeftRight = GPIO.PWM(LEFT_RIGHT_PIN, 50)  # frequency=50Hz
pilotLeftRight_DC = 50
pilotLeftRight.start(pilotFrontBack_DC)

# Servo Camera Tilt Up - Down
TILT_UP_DOWN_PIN = 17
GPIO.setup(TILT_UP_DOWN_PIN, GPIO.OUT)
tiltUpDown = GPIO.PWM(TILT_UP_DOWN_PIN, 50)  # frequency=50Hz
tiltUpDown_DC = 50
tiltUpDown.start(tiltUpDown_DC)

# Servo Camera Pan Left - Right
PAN_LEFT_RIGHT_PIN = 18
GPIO.setup(PAN_LEFT_RIGHT_PIN, GPIO.OUT)
panLeftRight = GPIO.PWM(PAN_LEFT_RIGHT_PIN, 50)  # frequency=50Hz
panLeftRight_DC = 50
panLeftRight.start(panLeftRight_DC)

# Servo Power Lock - Unlock
POWER_LOCK_UNLOCK_PIN = 27
GPIO.setup(POWER_LOCK_UNLOCK_PIN, GPIO.OUT)
powerLockUnlock = GPIO.PWM(POWER_LOCK_UNLOCK_PIN, 50)  # frequency=50Hz
powerLockUnlock.start(0)

# Relay
RELAY_PIN = 3
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, False)

try:
    while 1:
        print "Loop"
        with open("/var/www/PILOT_FIFO") as f:
            line = f.readline()
            cmd = line.rstrip('\n')
            print cmd

            if "pilotFront" == cmd:
                pilotFrontBack_DC = setDC(pilotFrontBack_DC, 10)
                pilotFrontBack.ChangeDutyCycle(pilotFrontBack_DC)
                print pilotFrontBack_DC
            if "pilotBack" == cmd:
                pilotFrontBack_DC = setDC(pilotFrontBack_DC, -10)
                pilotFrontBack.ChangeDutyCycle(pilotFrontBack_DC)
                print pilotFrontBack_DC

            if "pilotLeft" == cmd:
                pilotLeftRight_DC = setDC(pilotLeftRight_DC, 10)
                pilotLeftRight.ChangeDutyCycle(pilotLeftRight_DC)
                print pilotLeftRight_DC
            if "pilotRight" == cmd:
                pilotLeftRight_DC = setDC(pilotLeftRight_DC, -10)
                pilotLeftRight.ChangeDutyCycle(pilotLeftRight_DC)
                print pilotLeftRight_DC

            if "pilotStop" == cmd:
                pilotFrontBack_DC = 50
                pilotLeftRight_DC = 50
                pilotFrontBack.ChangeDutyCycle(pilotFrontBack_DC)
                pilotLeftRight.ChangeDutyCycle(pilotLeftRight_DC)
                print pilotFrontBack_DC
                print pilotLeftRight_DC

            if "tiltUp" == cmd:
                tiltUpDown_DC = setDC(tiltUpDown_DC, 10)
                tiltUpDown.ChangeDutyCycle(tiltUpDown_DC)
                print tiltUpDown_DC
            if "tiltDown" == cmd:
                tiltUpDown_DC = setDC(tiltUpDown_DC, -10)
                tiltUpDown.ChangeDutyCycle(tiltUpDown_DC)
                print tiltUpDown_DC

            if "panLeft" == cmd:
                panLeftRight_DC = setDC(panLeftRight_DC, 10)
                panLeftRight.ChangeDutyCycle(panLeftRight_DC)
                print panLeftRight_DC
            if "panRight" == cmd:
                panLeftRight_DC = setDC(panLeftRight_DC, -10)
                panLeftRight.ChangeDutyCycle(panLeftRight_DC)
                print panLeftRight_DC

            if "ptzCenter" == cmd:
                tiltUpDown_DC = 50
                panLeftRight_DC = 50
                tiltUpDown.ChangeDutyCycle(tiltUpDown_DC)
                panLeftRight.ChangeDutyCycle(panLeftRight_DC)
                print tiltUpDown_DC
                print panLeftRight_DC
            if "ptzPower" == cmd:
                tiltUpDown_DC = 0
                panLeftRight_DC = 50
                tiltUpDown.ChangeDutyCycle(tiltUpDown_DC)
                panLeftRight.ChangeDutyCycle(panLeftRight_DC)
                print tiltUpDown_DC
                print panLeftRight_DC

            if "powerLock" == cmd:
                powerLockUnlock.ChangeDutyCycle(0)
                print "Power Locked"
            if "powerUnlock" == cmd:
                powerLockUnlock.ChangeDutyCycle(100)
                print "Power Unlocked"

            if "samsungPower" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_POWER")
                print "TV Power"
            if "samsungSource" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 input")
                print "TV Source"
            if "goTV" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 input")
	        time.sleep(1)
		os.system("irsend SEND_ONCE LG_AKB72915207 KEY_LEFT")
                time.sleep(1)
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_OK")
                print "Go TV"
            if "goSkype" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 input")
                time.sleep(1)
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_RIGHT")
                time.sleep(1)
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_OK")
                print "Go Skype"

            if "samsungSelect" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_OK")
                print "TV OK"

            if "samsungLeft" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_LEFT")
                print "TV Left"
            if "samsungRight" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_RIGHT")
                print "TV Right"

            if "samsungUp" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_UP")
                print "TV Up"
            if "samsungDown" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_DOWN")
                print "TV Down"

            if "samsungVolumeUp" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_VOLUMEUP")
                print "TV Volume Up"
            if "samsungVolumeDown" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_VOLUMEDOWN")
                print "TV Volume Down"

            if "samsungProgramUp" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_CHANNELUP")
                print "TV Program Up"
            if "samsungProgramDown" == cmd:
                os.system("irsend SEND_ONCE LG_AKB72915207 KEY_CHANNELDOWN")
                print "TV Program Down"

            if "relayHPC" == cmd:
                print "Relay Opening..."
                GPIO.output(RELAY_PIN, True)
                time.sleep(3)
                GPIO.output(RELAY_PIN, False)
                print "Relay closed"

        time.sleep(0.1)

except KeyboardInterrupt:
    print "Bye Bye !!"

except:
    print "Bye bye by another eception"

finally:
    print "Clearing GPIO"
    pilotFrontBack.stop()
    pilotLeftRight.stop()
    tiltUpDown.stop()
    panLeftRight.stop()
    powerLockUnlock.stop()
    GPIO.output(RELAY_PIN, False)

    GPIO.cleanup()

