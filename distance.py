import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# set GPIO Pins
pinTrigger =(5, 22, 4)
RpinTrigger = 5
RpinEcho = 6
MpinTrigger = 22
pinEcho = (6, 27, 17)
MpinEcho = 27
LpinTrigger = 4
LpinEcho = 17

#def close(signal, frame):
#	print("\nTurning off ultrasonic distance detection...\n")
#	GPIO.cleanup() 
#	sys.exit(0)

#signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(LpinTrigger, GPIO.OUT)
GPIO.setup(MpinTrigger, GPIO.OUT)
GPIO.setup(RpinTrigger, GPIO.OUT)
GPIO.setup(LpinEcho, GPIO.IN)
GPIO.setup(MpinEcho, GPIO.IN)
GPIO.setup(RpinEcho, GPIO.IN)
all_distance =[0,0,0]

def the_distance():
  #try:
   # while True:
      def trigger_function(pinTrigger, pinEcho):
        for i in range(len(pinEcho)):
          # set Trigger to HIGH
          GPIO.output(pinTrigger[i], 1)
          # set Trigger after 0.01ms to LOW
          time.sleep(0.00001)
          GPIO.output(pinTrigger[i], 0)
          # save start time
          while 0 == GPIO.input(pinEcho[i]):
            startTime = time.time()
          # save time of arrival
          while 1 == GPIO.input(pinEcho[i]):
            stopTime = time.time()
          # time difference between start and arrival
          TimeElapsed = stopTime - startTime
          # multiply with the sonic speed (34300 cm/s)
          # and divide by 2, because there and back
          distance = (TimeElapsed * 34300) / 2

          if i == 0 :
            #print("Distance Right: %s cm" % distance)
            all_distance[0] = distance
          elif i == 1 :
            #print("Distance Front: %s cm" % distance)
            all_distance[1] = distance
          elif i == 2 :
            #print("Distance Left: %s cm" % distance)
            all_distance[2] = distance
        return all_distance 

      export_distance = trigger_function(pinTrigger,pinEcho)
      return export_distance
  #except KeyboardInterrupt:
  #  print ("\n")
  #finally:
#GPIO.cleanup()

#the_distance()


