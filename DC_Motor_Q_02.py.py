
import RPi.GPIO as GPIO
import time

MotorPin1 = 11    # pin11
MotorPin2 = 12    # pin12
MotorEnable = 13  # pin13

LedPinCW = 3      # LED for clockwise 
LedPinCCW = 5     # LED for anticlockwise 

def setup():
    GPIO.setmode(GPIO.BOARD)         
    GPIO.setup(MotorPin1, GPIO.OUT)  
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT)
    GPIO.setup(LedPinCW, GPIO.OUT)   # LED for clockwise rotation
    GPIO.setup(LedPinCCW, GPIO.OUT)  # LED for anticlockwise rotation
    GPIO.output(MotorEnable, GPIO.LOW) 
    GPIO.output(LedPinCW, GPIO.LOW)     # LED off
    GPIO.output(LedPinCCW, GPIO.LOW)    # LED off

def loop():
    while True:
        print('Motor rotating clockwise. Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH)  
        GPIO.output(MotorPin1, GPIO.HIGH)    # clockwise
        GPIO.output(MotorPin2, GPIO.LOW)
        GPIO.output(LedPinCW, GPIO.HIGH)     # turn on CW LED
        GPIO.output(LedPinCCW, GPIO.LOW)     # ensure CCW LED is off
        time.sleep(5)
        
        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        GPIO.output(LedPinCW, GPIO.LOW)     # turn off CW LED
        time.sleep(5)
        
        print('Motor rotating anticlockwise. Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH)  
        GPIO.output(MotorPin1, GPIO.LOW)    # anticlockwise
        GPIO.output(MotorPin2, GPIO.HIGH)
        GPIO.output(LedPinCW, GPIO.LOW)      # ensure CW LED is off
        GPIO.output(LedPinCCW, GPIO.HIGH)    # turn on CCW LED
        time.sleep(5)
        
        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        GPIO.output(LedPinCCW, GPIO.LOW)    # turn off CCW LED
        time.sleep(5)

def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.output(LedPinCW, GPIO.LOW)     # turn off CW LED
    GPIO.output(LedPinCCW, GPIO.LOW)    # turn off CCW LED
    GPIO.cleanup()                     

setup()
try:
    loop()
except KeyboardInterrupt: 
    destroy()
