from time import time, sleep
import RPi.GPIO as GPIO

delay = .05
waitForPlay = 2
pinButton = 40
pinLed = 38
state = "Idle"
sequenceRecord = []
sequenceIndex = 0
lastPulseAt = 0
buttonPressed = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinLed, GPIO.OUT)

def setState(value):
  global state
  state = value
  print(f"state: {state}")

setState("Idle")


try:
  while True:
    buttonValue = GPIO.input(pinButton)
    # print(buttonValue)

    if state == "Idle":
      if buttonValue == buttonPressed:
        lastPulseAt = time()
        setState("Recording")

    elif state == "Recording":
      sequenceRecord.append(buttonValue)
      # print(sequenceRecord)
      if buttonValue == buttonPressed:
        lastPulseAt = time()
      else:
        if lastPulseAt + waitForPlay < time():
          setState("Playing")

    elif state == "Playing":
      GPIO.output(pinLed, sequenceRecord[sequenceIndex])
      sequenceIndex += 1
      if sequenceIndex >= len(sequenceRecord):
        sequenceRecord = []
        sequenceIndex = 0
        setState("Idle")

    sleep(delay)
except KeyboardInterrupt:
  GPIO.cleanup()
  print("bye!")
