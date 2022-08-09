from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import argparse



def capturePic(camera, on, off, indx):   
    camera.start_preview()
    GPIO.output(40,True)
    sleep(1)
    camera.capture('/home/pi/cap/image_{}.jpg'.format(indx))
    camera.stop_preview()
    GPIO.output(40,False)
    sleep(2)
    

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ontime', default=1)
    parser.add_argument('-f', '--offtime', default=2)
    parser.add_argument('-t', '--totaltime', default=20)
    args = parser.parse_args()

    
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False) 
    GPIO.setup(40, GPIO.OUT)
    camera = PiCamera()
    
    tm=0
    
    while (tm < int(args.totaltime)):
        tm= tm + args.ontime
        tms = str(tm).zfill(3)
        capturePic(camera, args.ontime, args.offtime, tms)
        tm = tm  + args.offtime
#        indx = indx + 1


    camera.close()