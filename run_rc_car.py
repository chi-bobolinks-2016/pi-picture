import RPi.GPIO as GPIO
from time import sleep

def PiCar():

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.pins = {'left'     : 11,
                     'right'    : 18,
                     'forward'  : 12,
                     'backward' : 16 }
        for pin_number in self.pins.itervalues():
            GPIO.setup(pin_number,GPIO.OUT)
        return;

    def stop():
        for pin_number in self.pins.itervalues():
            GPIO.output(pin_number,0)
        return;

    def go_forward(time):
        stop()
        GPIO.output(self.pins['forward'],1)
        sleep(int(time))
        GPIO.output(self.pins['forward'],0)
        return;

    def go_backward(time):
        stop()
        GPIO.output(self.pins['backward'],1)
        sleep(int(time))
        GPIO.output(self.pins['backward'],0)
        return;

    def go_forward_right(time):
        stop()
        GPIO.output(self.pins['right'],1)
        GPIO.output(self.pins['forward'],1)
        sleep(int(time))
        GPIO.output(self.pins['forward'],0)
        GPIO.output(self.pins['right'],0)
        return;

    def go_forward_left(time):
        stop()
        GPIO.output(self.pins['left'],1)
        GPIO.output(self.pins['forward'],1)
        sleep(int(time))
        GPIO.output(self.pins['forward'],0)
        GPIO.output(self.pins['left'],0)
        return;

    def go_backward_right(time):
        stop()
        GPIO.output(self.pins['right'],1)
        GPIO.output(self.pins['backward'],1)
        sleep(int(time))
        GPIO.output(self.pins['backward'],0)
        GPIO.output(self.pins['right'],0)
        return;

    def go_backward_left(time):
        stop()
        GPIO.output(self.pins['left'],1)
        GPIO.output(self.pins['backward'],1)
        sleep(int(time))
        GPIO.output(self.pins['backward'],0)
        GPIO.output(self.pins['left'],0)
        return;


picar = PiCar()
picar.go_forward(1)
picar.go_forward_right(1)
picar.go_backward_left(1)
picar.go_forward(2)
picar.go_backward(2)
picar.go_forward_right(5)