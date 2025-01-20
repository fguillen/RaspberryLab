#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import random

RedPin = 17
GreenPin = 27
YellowPin = 5
Leds = [RedPin, GreenPin, YellowPin]
Activations = [GPIO.LOW, GPIO.HIGH]

def setup():
  GPIO.setmode(GPIO.BCM)
  for led in Leds:
    GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

def main():
  while True:
    randomActivations()
    time.sleep(0.05)

def randomActivations():
  for led in Leds:
    GPIO.output(led, random.sample(Activations, 1))

def destroy():
  for led in Leds:
    GPIO.output(led, GPIO.HIGH)

  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    main()
  # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
  except KeyboardInterrupt:
    destroy()
