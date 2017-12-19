import RPi.GPIO as GPIO
from time import sleep
import sys
import signal
import random
import tkinter as tk
import distance as dt
import subprocess
import classify as cs
#import classify_tf as cs

GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG2 = 24				# set dir2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(DIG1, 100)		# set pwm for M1
p2 = GPIO.PWM(DIG2, 100)		# set pwm for M2

################ Movement Definitions BEGIN #######################

def backward(tf):
  print ("Banckward")			# display "Forward" when programe run
  GPIO.output(AN1, GPIO.HIGH)		# set AN1 as HIGH, M1B will turn ON
  GPIO.output(AN2, GPIO.HIGH)		# set AN2 as HIGH, M2B will turn ON
  p1.start(0)				# set Direction for M1
  p2.start(0)				# set Direction for M2
  sleep(tf)
  GPIO.output(AN1, GPIO.LOW)           # set AN1 as HIGH, M1B will turn ON
  GPIO.output(AN2, GPIO.LOW)

def forward(tf):
  print ("Forward")
  GPIO.output(AN1, GPIO.HIGH)
  GPIO.output(AN2, GPIO.HIGH)
  p1.start(72)
  p2.start(100)
  sleep(tf)
  GPIO.output(AN1, GPIO.LOW)
  GPIO.output(AN2, GPIO.LOW)

def right(tf):
  print ("Right")
  GPIO.output(AN1, GPIO.HIGH)
  GPIO.output(AN2, GPIO.HIGH)
  p1.start(0)
  p2.start(100)
  sleep(tf)
  GPIO.output(AN1, GPIO.LOW)           
  GPIO.output(AN2, GPIO.LOW)

def left(tf):
  print ("Left")
  GPIO.output(AN1, GPIO.HIGH)
  GPIO.output(AN2, GPIO.HIGH)
  p1.start(100)
  p2.start(0)
  sleep(tf)
  GPIO.output(AN1, GPIO.LOW)           
  GPIO.output(AN2, GPIO.LOW)

def stop():
  print("STOP!")
  GPIO.output(AN1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
  GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
  p1.start(0)                          # Direction can ignore
  p2.start(0)                          # Direction can ignore
  sleep(3)                             #delay for 3 second

def sigint_handler(signum, frame):
  sys.exit(0)
  signal.signal(signal.SIGINT, sigint_handler)

def check_front():
  dist = dt.distance()
  if dist < 15:
    print("Too close,", dist)
    backward()
    dist = dt.distance()
    if dist < 15:
      print("Too close,", dist)
      left()
      dist = dt.distance()
      if dist.distanceM < 15:
        print("Too close, giving up", dist)
        sys.exit()

def key_input(event):
  key_press = event.keysym.lower()
  sleep_time = 0.20
  dt.the_distance()
  print(key_press)
  
  if key_press == 'w':
    forward(sleep_time)
    check_front()
  elif key_press == 's':
    backward(sleep_time)
    check_front()
  elif key_press == 'a':
    left(sleep_time)
    check_front()
  elif key_press == 'd':
    right(sleep_time)
    check_front()
  elif key_press == 'q':
    stop()
  elif key_press == 'z':
    stop()
    GPIO.cleanup()
    sys.exit(0)
  elif key_press == 'space':
    print('Analyze!')
    cs.classify()
    #cs.main()
  else:
    print('Wrong key kress')

def autonomy(): 
  tf = 0.030
  x = random.randrange(0,4)

  if x == 0:
    for y in range(30):
      check_front()
      forward()
  elif x == 1:
    for y in range(30):
      check_front()
      left()
  elif x == 2:
    for y in range(30) :
      check_front()
      right()
  elif x == 3:
    for y in range(30):
      check_front()
      left()

#for z in range(10):
#  autonomy()

# -------- Main Program Loop -----------

command = tk.Tk()
command.bind_all('<Key>', key_input)
command.mainloop()

#def pivot_right(tf):
#GPIO.cleanup()

