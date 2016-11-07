import RPi.GPIO as GPIO
from time import sleep

def initialize():
    GPIO.setmode(GPIO.BOARD)
    pins = {'left'     : 11,
            'right'    : 18,
            'forward'  : 12,
            'backward' : 16 }
    GPIO.setmode(GPIO.BOARD)
    for pin in pins.attributes
        GPIO.setup(pins[pin],GPIO.OUT)
    return;

def stop():
    for pin in pins.attributes
        GPIO.output((pins[pin],0)
    return;

def go_forward(time):
    stop()
    GPIO.output(pins['forward'],1)
    sleep(int(time))
    GPIO.output(pins['forward'],0)
    return;

def go_backward(time):
    stop()
    GPIO.output(pins['backward'],1)
    sleep(int(time))
    GPIO.output(pins['backward'],0)
    return;

def go_forward_right(time):
    stop()
    GPIO.output(pins['right'],1)
    GPIO.output(pins['forward'],1)
    sleep(int(time))
    GPIO.output(pins['forward'],0)
    GPIO.output(pins['right'],0)
    return;

def go_forward_left(time):
    stop()
    GPIO.output(pins['left'],1)
    GPIO.output(pins['forward'],1)
    sleep(int(time))
    GPIO.output(pins['forward'],0)
    GPIO.output(pins['left'],0)
    return;

def go_backward_right(time):
    stop()
    GPIO.output(pins['right'],1)
    GPIO.output(pins['backward'],1)
    sleep(int(time))
    GPIO.output(pins['backward'],0)
    GPIO.output(pins['right'],0)
    return;

def go_backward_left(time):
    stop()
    GPIO.output(pins['left'],1)
    GPIO.output(pins['backward'],1)
    sleep(int(time))
    GPIO.output(pins['backward'],0)
    GPIO.output(pins['left'],0)
    return;


initialize()
go_forward(1)
go_forward_right(1)
go_backward_left(1)
go_forward(2)
go_backward(2)
go_forward_right(5)