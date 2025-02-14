import RPi.GPIO as GPIO
import time

from updatable import Updatable

class Led(Updatable):
  def __init__(self, name, bcm_pin_num):
    self.name = name
    self.pin = bcm_pin_num
    self.value = 0
    self.pwm = None
    self.pulsing_speed = 0.0
    self.pulsing = False
    self.start_pulsing_at = None

    self._setup_gpio()

    Updatable.__init__(self)


  def set_value(self, new_value):
    self.value = new_value
    self.pwm.ChangeDutyCycle(self.value)


  def update(self, delta):
    if self.pulsing == False:
      return

    time_pulsing = time.time() - self.start_pulsing_at
    cycle_time = time_pulsing % self.pulsing_speed
    duty = 100 * cycle_time
    self.set_value = duty


  def start_pulsing(self, speed):
    self.pulsing_speed = speed
    self.pulsing = True
    self.start_pulsing_at = time.time()


  def stop(self):
    self.pulsing_speed = 0.0
    self.pulsing = False
    self.set_value(0)
    self.start_pulsing_at = None


  def destroy(self):
    Updatable.destroy(self)


  def __str__(self):
    return f"Button[{self.name}]:{self.value}"


  def _load_value(self):
    return GPIO.input(self.pin)


  def _setup_gpio(self):
    GPIO.cleanup(self.pin)
    GPIO.setup(self.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin, 100)
    self.pwm.start(self.value)
