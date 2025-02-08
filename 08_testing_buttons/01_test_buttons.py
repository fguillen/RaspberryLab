from time import time, sleep
import RPi.GPIO as GPIO

delay = .05

pinsButtons = {
  "red": 31,
  "green": 33,
  "blue": 35,
  "yellow": 37
}

pinsLeds = {
  "red": 32,
  "green": 36,
  "blue": 38,
  "yellow": 40
}

valuesButtons = {
  "red": 0,
  "green": 0,
  "blue": 0,
  "yellow": 0
}


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

    print(valuesButtons)


    sleep(delay)


except KeyboardInterrupt:
  GPIO.cleanup()
  print("bye!")
