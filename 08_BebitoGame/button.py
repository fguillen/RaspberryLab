import RPi.GPIO as GPIO

class Button:
  def __init__(self, name, bcm_pin_num):
    self.name = name
    self.pin = bcm_pin_num
    self.value = 0
    self.pressed_in_the_last_frame = False

    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  def update(self):
    pinValue = GPIO.input(self.pin)

    if pinValue == 1 and self.value == 0:
      print("pressend_in_the_last_frame")
      self.pressed_in_the_last_frame = True
    else:
      self.pressed_in_the_last_frame = False

    self.value = pinValue

  def on_destroy(self):
    GPIO.cleanup(self.pin)

  def __str__(self):
    return f"Button[{self.name}]:{self.value}"
