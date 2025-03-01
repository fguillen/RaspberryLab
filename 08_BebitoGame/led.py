import RPi.GPIO as GPIO
import time

from updatable import Updatable


class Led(Updatable):
  pool = []

  def __init__(self, name, bcm_pin_num):
    print("Led.init", name, bcm_pin_num)
    self.name = name
    self.pin = bcm_pin_num
    self.value = 0
    self.pwm = None
    self.cycle_duration = 0.0
    self.pulsating = False
    self.start_pulsating_at = None
    self.max_intensity = 1

    self._destroy_tween_in_the_pool()
    self._setup_gpio()

    Updatable.__init__(self)

    Led.pool.append(self)


  def set_value(self, new_value):
    self.value = new_value
    self.pwm.ChangeDutyCycle(self.value * self.max_intensity)


  def update(self, delta):
    if self.pulsating == False:
      return

    time_pulsating = time.time() - self.start_pulsating_at
    cycle_time = time_pulsating % self.cycle_duration
    duty = 100 * cycle_time
    self.set_value(duty)


  def start_pulsating(self, speed, max_intensity=1):
    print(">>>>> led.start_pulsating()", self.name)
    self.cycle_duration = speed
    self.pulsating = True
    self.start_pulsating_at = time.time()
    self.max_intensity = max_intensity


  def stop(self):
    self.cycle_duration = 0.0
    self.pulsating = False
    self.set_value(0)
    self.start_pulsating_at = None


  def destroy(self):
    self.set_value(0)
    self.pwm.stop()
    GPIO.cleanup(self.pin)
    Updatable.destroy(self)

    if self in Led.pool:
      Led.pool.remove(self)


  def __str__(self):
    return f"Led[{self.name}]:{self.value}"


  def _load_value(self):
    return GPIO.input(self.pin)


  def _destroy_tween_in_the_pool(self):
    tween = next((e for e in Led.pool if e.pin == self.pin), None)
    if tween != None:
      print("Tween found:", tween)
      tween.destroy()


  def _setup_gpio(self):
    GPIO.cleanup(self.pin)
    GPIO.setup(self.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin, 100)
    self.pwm.start(self.value)
