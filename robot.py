 
import RPi.GPIO as GPIO
import time
import sys
from Tkinter import *

GPIO.setmode(GPIO.BOARD)
servoPin1 = 11
servoPin2 = 13
GPIO.setup(servoPin1, GPIO.OUT)
GPIO.setup(servoPin2, GPIO.OUT)

