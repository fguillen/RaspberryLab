import RPi.GPIO as GPIO

class Button:
  def __init__(self, name, board_pin_num):
    self.name = name
    self.pin = board_pin_num
    self.value = 0

    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  def update(self):
    self.value = GPIO.input(self.pin)

  def on_destroy(self):
    GPIO.cleanup(self.pin)

  def __str__(self):
    return f"Button[{self.name}]:{self.value}"
