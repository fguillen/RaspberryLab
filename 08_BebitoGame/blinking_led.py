import time

from updatable import Updatable
from led import Led

class BlinkingLed(Updatable):
  def __init__(self, bcm_pin_num, on_completed=None, cycle_duration=2, duration_seconds=1):
    self.bcm_pin_num = bcm_pin_num
    self.cycle_duration = cycle_duration
    self.duration_seconds = duration_seconds
    self.led = self._init_led()
    self.on_completed = on_completed
    self.started_at = time.time()

    Updatable.__init__(self)


  def set_on_completed(self, callback):
    self.on_completed = callback


  def update(self, delta = 1.0):
    if time.time() > self.started_at + self.duration_seconds:
      self._completed()


  def draw(self):
    for pixel in self._pixels_by_size():
      self.canvas[pixel] = self.color


  def destroy(self):
    self.led.destroy()
    Updatable.destroy(self)


  def _completed(self):
    self.destroy()

    if self.on_completed:
      self.on_completed()


  def _init_led(self):
    led = Led(
      name="BlinkingLed",
      bcm_pin_num=self.bcm_pin_num
    )
    led.start_pulsating(self.cycle_duration)

    return led
