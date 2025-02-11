from updatable import Updatable

class Button(Updatable):
  def __init__(self, name, bcm_pin_num, on_button_pressed=None):
    self.name = name
    self.pin = bcm_pin_num
    self.value = 0
    self.pressed_in_the_last_frame = False
    self.on_button_pressed = on_button_pressed

    self._setup_gpio()

    super().__init__()

  def set_on_button_pressed(self, callback):
    self.on_button_pressed = callback

  def update(self, delta):
    pinValue = self._load_value()

    if pinValue == 1 and self.value == 0:
      # Button pressed in the last frame
      if self.on_button_pressed:
        self.on_button_pressed()

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
