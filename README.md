            
 San Francisco Bay University

CE450 Fundamentals of Embedded Engineering
Lab 7 DC Motor Control

Objectives:
In this week, students will design the program to control DC motor through GPIO ports on Raspberry Pi bord and do hands-on exercise through lab assignment.

Introduction:
DC motor and driving IC l293d are available in Sunfounder accessory box. The control circuit has been shown in the following schematic. To drive DC motor heavy load, the power module is needed in the hardware connection shown as follows.

Equipment: 
The equipment you require is as follows:
•	Laptop & Raspberry Pi 3 model Board
•	SunFounder Super Starter Kit V2.0 for Raspberry Pi 

The Laboratory Procedure: 
1.	Hardware connection 
 
 

2.	Control program in Python

# Python Program

import RPi.GPIO as GPIO
import time

MotorPin1   = 11    # pin11
MotorPin2   = 12    # pin12
MotorEnable = 13    # pin13

def setup():
	GPIO.setmode(GPIO.BOARD)          # Numbers GPIOs by physical location
	GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
	GPIO.setup(MotorPin2, GPIO.OUT)
	GPIO.setup(MotorEnable, GPIO.OUT)
	GPIO.output(MotorEnable, GPIO.LOW) # motor stop

def loop():
	while True:
		print 'Press Ctrl+C to end the program...'
		GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
		GPIO.output(MotorPin1, GPIO.HIGH)   # clockwise
		GPIO.output(MotorPin2, GPIO.LOW)
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.LOW) # motor stop
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
		GPIO.output(MotorPin1, GPIO.LOW)   # anticlockwise
		GPIO.output(MotorPin2, GPIO.HIGH)
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.LOW) # motor stop
		time.sleep(5)

def destroy():
	GPIO.output(MotorEnable, GPIO.LOW) # motor stop
	GPIO.cleanup()                     # Release resource


setup()
try:
	loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()

	*Note: Hardware connection reference and running command
https://learn.sunfounder.com/lesson-11-how-to-drive-a-dc-motor/
https://learn.sunfounder.com/category/super-kit-v3-0-for-raspberry-pi/

The Laboratory Assignments: 

1.	Build up the hardware circuit and run the example program to observe what will happen.

2.	Add two LEDs in the different colors of yellow and red to the above circuit. And switch on the yellow one if the DC motor is running in a clockwise direction. Otherwise, switch on the red one.

