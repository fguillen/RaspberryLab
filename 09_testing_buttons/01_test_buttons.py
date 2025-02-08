from time import time, sleep
import RPi.GPIO as GPIO

delay = .05

pinsButtons = {
  "red": 33,
  "green": 35,
  "blue": 37,
  "white": 31
}

pinsLeds = {
  "red": 38,
  "green": 36,
  "blue": 32,
  "white": 40
}

valuesButtons = {
  "red": 0,
  "green": 0,
  "blue": 0,
  "white": 0
}


print("GPIO.getmode():", GPIO.getmode(), GPIO.BCM, GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)

for key in pinsButtons:
  GPIO.setup(pinsButtons[key], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for key in pinsLeds:
  GPIO.setup(pinsLeds[key], GPIO.OUT)


try:
  while True:
    for key in pinsButtons:
      valuesButtons[key] = GPIO.input(pinsButtons[key])

    for key in pinsLeds:
      GPIO.output(pinsLeds[key], valuesButtons[key])
      # GPIO.output(pinsLeds[key], 1)

    print(valuesButtons)


    sleep(delay)


except KeyboardInterrupt:
  GPIO.cleanup()
  print("bye!")
