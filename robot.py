 
import RPi.GPIO as GPIO
import time
import sys
from Tkinter import *

GPIO.setmode(GPIO.BOARD)
servoPin1 = 11
servoPin2 = 13
GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)
pwm1 = GPIO.PWM(servoPin1,50)
pwm2 = GPIO.PWM(servoPin2,50)

root = Tk() 
root.wm_title("Robot Control") 
root.config(background = "#FFFFFF")



leftFrame = Frame(root ,width = 200, height = 600)
leftFrame.grid(row = 0, column = 0, padx = 10, pady = 2)

