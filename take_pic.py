from picamera import PiCamera
from time import sleep
import sys

def TakePictures(directory,numbers):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    for i in range(int(numbers)):
        camera.capture(directory + '/image%s.jpg' % i)
        print 'taking picture #' +str(i)
        sleep(1)

    camera.stop_preview()
    return ;

TakePictures(sys.argv[1],sys.argv[2])
