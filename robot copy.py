 
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

Label(leftFrame, text = "Instructions:").grid(row = 0, column = 0, padx = 10, pady = 2)

Instruct = Label(leftFrame, text = "Welcome to my rc robot project the controls are: \n 'w' to move forward\t's' to reverse\n'a' to go left\t'd' to go right\n 'q' the straighten the wheels ")
Instruct.grid(row = 1, column = 0, padx = 10, pady = 2)

def key_input(event):

        print ('Key: ', event.char)
        key_press = event.char

        if key_press.lower() == 'w':
                pwm1.start(1)
        elif key_press.lower() == ' ':
                pwm1.stop()
        elif key_press.lower() == 's':
                pwm1.start(90)
        elif key_press.lower() == 'd':
               	pwm2.start(5)
               	pwm2.ChangeDutyCycle(14)
        elif key_press.lower() == 'a':
               pwm2.start(5)
               pwm2.ChangeDutyCycle(1)
	elif key_press.lower() == 'q':
		pwm2.start(5)
		pwm2.ChangeDutyCycle(6)
        else :
                pwm1.stop()


root.bind('<KeyPress>',key_input)
root.mainloop()




