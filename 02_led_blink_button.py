#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

LedPin = 17 # Set GPIO17 as LED pin
BtnPin = 12 # Set GPIO18 as button pin


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)  # Set LedPin's mode to output, and initial level to high (3.3v)
  GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set BtnPin's mode to input.

def my_callback(event = None):
  buttonStatus = GPIO.input(BtnPin)

  print ('Value in callback:', buttonStatus)

  GPIO.output(LedPin, buttonStatus)

  if buttonStatus:
    print ('LED OFF...')
  else:
    print ('...LED ON')

def main():
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=my_callback, bouncetime=30)
  while True:
    print ('Value:', GPIO.input(BtnPin))
    time.sleep(0.05)

def destroy():
  GPIO.output(LedPin, GPIO.HIGH)
  GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
  setup()
  try:
    main()
  except KeyboardInterrupt:
    destroy()
