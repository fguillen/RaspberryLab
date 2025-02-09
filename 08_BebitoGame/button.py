from updatable import Updatable

class Button(Updatable):
  def __init__(self, name, bcm_pin_num):
    self.name = name
    self.pin = bcm_pin_num
    self.value = 0
    self.pressed_in_the_last_frame = False

    self._setup_gpio()

    super().__init__()

  def update(self, delta):
    pinValue = self._load_value()

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

  def _load_value(self):
    return GPIO.input(self.pin)

  def _setup_gpio(self):
    import RPi.GPIO as GPIO
    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
