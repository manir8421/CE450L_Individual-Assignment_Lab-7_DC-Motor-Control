import RPi.GPIO as GPIO
import time

MotorPin1 = 11  # pin11
MotorPin2 = 12  # pin12
MotorEnable = 13  # pin13

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MotorPin1, GPIO.OUT)  
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT)
    GPIO.output(MotorEnable, GPIO.LOW) 

def loop():
    while True:
        print('Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH) 
        GPIO.output(MotorPin1, GPIO.HIGH)  # clockwise
        GPIO.output(MotorPin2, GPIO.LOW)
        time.sleep(5)
        
        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        time.sleep(5)
        
        GPIO.output(MotorEnable, GPIO.HIGH) 
        GPIO.output(MotorPin1, GPIO.LOW)  # anticlockwise
        GPIO.output(MotorPin2, GPIO.HIGH)
        time.sleep(5)
        
        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        time.sleep(5)

def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.cleanup() 

setup()
try:
    loop()
except KeyboardInterrupt: 
    destroy()
