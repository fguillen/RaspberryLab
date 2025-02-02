from time import sleep
import RPi.GPIO as GPIO

delay = .1
pinButton = 40
pinLed = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinButton, GPIO.IN)
GPIO.setup(pinLed, GPIO.OUT)

try:
  while True:
    buttonValue = GPIO.input(pinButton)
    print(buttonValue)
    if buttonValue == 1:
      GPIO.output(pinLed, 1)
    else:
      GPIO.output(pinLed, 0)

    sleep(delay)
except KeyboardInterrupt:
  GPIO.cleanup
  print("bye!")
