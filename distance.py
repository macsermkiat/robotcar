import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
RpinTrigger = 5
RpinEcho = 6
MpinTrigger = 22
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

def the_distance():
  #try:
   # while True:
      def trigger_function(trigger):
        # set Trigger to HIGH
        GPIO.output(trigger, 1)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(trigger, 0)
        #startTime = time.time()
        #stopTime = time.time()
        #return startTime
        #return stopTime

      def echo_function(echo):
        # save start time
        while 0 == GPIO.input(echo):
          startTime = time.time()
        # save time of arrival
        while 1 == GPIO.input(echo):
          stopTime = time.time()
        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        #return distance
        #print ("Distance %s:  %.1f cm" %(echo, distance))
        if echo == 6 :
          distanceR = distance
          print("Distance Right: %s cm" % distanceR)
        elif echo == 27 :
          distanceM = distance
          print("Distance Front: %s cm" % distanceM)
        elif echo == 17 :
          distanceL = distance
          print("Distance Left: %s cm" % distanceL)
        all_distance = [distanceL, distanceM, distanceR]
        return all_distance
        time.sleep(1)
      
      #Define functions for position of sensor
      #def front_sensor():
      trigger_function(MpinTrigger)
      echo_function(MpinEcho)
      #def right_sensor():
      trigger_function(RpinTrigger)
      echo_function(RpinEcho)
      #def left_sensor():
      trigger_function(LpinTrigger)
      echo_function(LpinEcho)

      #Run functions
      #dfront = front_sensor()
      #dfront()
      #dright = right_sensor()
      #dright()
      #dleft = left_sensor()
      #dleft()
      #'''
  #except KeyboardInterrupt:
  #  print ("\n")
  #finally:
  #  GPIO.cleanup()

#the_distance()
