import time
import random
from datetime import datetime, time as dt_time

import board
import neopixel
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

# from neopixel_mock.neopixel_mock import NeoPixelMock
# from neopixel_mock.board_mock import BoardMock

from updatable import Updatable
from drawable import Drawable
from wanderer import Wanderer
from canvas import Canvas
from pulsating_sequence import PulsatingSequence
from check_elements import CheckElements
from led import Led
from black_rain import BlackRain
from color import Color

# from blinking_led import BlinkingLed
# from config import pins_buttons, pins_leds
from config import settings
# from button import Button

class Engine():
  def __init__(self):
    print(">>>> Engine.init")
    self.wanderers = []
    self.pulsatings = []

    self.board = board
    self.leds = neopixel.NeoPixel(self.board.D10, 64, brightness=0.02, auto_write=False)
    self.pixel_grid = PixelGrid(self.leds, 8, 8, orientation=HORIZONTAL, alternating=True)
    self.fps = 0
    self.fade_out_factor = 0.95
    self.canvas = Canvas(8, 8)
    self.last_updated_at = time.time()
    self.wanderers_started_at = time.time()
    self.asleep_at = None

    self.awake_slot_ini = datetime.strptime(settings.awake_slot_ini, "%H:%M").time(),
    self.awake_slot_end = datetime.strptime(settings.awake_slot_end, "%H:%M").time(),

    self.start_time = datetime.strptime(start_limit, "%H:%M").time()
    end_time = datetime.strptime(end_limit, "%H:%M").time()

    # self._check_elements()
    # self._init_pulsating_sequence()
    # self._init_led()
    # self._init_blinking_led()
    # self._init_buttons()
    # self._init_black_rain()

    self._awake()


  def update(self):
    delta = self._delta()

    if self.state == "wanderers":
      self._check_if_should_sleep()

    if self.state == "asleep":
      self._check_if_should_awake()

    if self.state == "wanderers" or self.state == "black_rain" or self.state == "calling":
      for updatable in Updatable.all:
        updatable.update(self._delta())

    if delta > 0:
      self.fps = 1 / delta

    self.last_updated_at = time.time()

    # Debug
    # print("                          Delta: ", delta, "FPS: ", self.fps)


  def draw(self):
    self.canvas.fade_out(self.fade_out_factor)

    for drawable in Drawable.all:
      drawable.draw()

    # render Canvas to PixelGrid
    for x in range(self.pixel_grid.width):
      for y in range(self.pixel_grid.height):
        color = self.canvas[x, y]
        self.pixel_grid[x, y] = color.rgb_rounded()

    self.pixel_grid.show()


  def init_wander(self, key):
    wanderer = Wanderer(key, self.canvas, speed=random.randint(5, 15))
    self.wanderers.append(wanderer)


  def _delta(self):
    now = time.time()
    delta = now - self.last_updated_at
    return delta


  def _check_elements(self):
    CheckElements(self.canvas, on_complete=lambda: self._init_pulsating_sequence())


  def _init_pulsating_sequence(self):
    PulsatingSequence("green", self.canvas, self, on_completed=lambda: self._activate_wanderers())


  def _destroy_all_elements(self):
    for updatable in Updatable.all:
      updatable.destroy()

    for drawable in Drawable.all:
      drawable.destroy()

    print(">>>> After destroy Updatable.all")
    for updatable in Updatable.all:
      print(">>>>>", id(updatable), updatable.__class__, updatable)
      updatable.destroy()

    print(">>>> After destroy Drawable.all")
    for drawable in Drawable.all:
      print(">>>>>", id(drawable), drawable.__class__, drawable)
      drawable.destroy()


  def _init_black_rain(self):
    self._change_state("black_rain")
    self._destroy_all_elements()
    color_name = random.choice(["maroon", "green", "teal", "white"])
    BlackRain(Color.from_name(color_name), self.canvas, on_completed=lambda: self._black_rain_completed())


  def _black_rain_completed(self):
    print(">>>> Engine._black_rain_completed")
    self._go_to_sleep()


  def _activate_wanderers(self):
    self._change_state("wanderers")
    self.wanderers_started_at = time.time()

    for wander in self.wanderers:
      wander.set_active(True)


  def _check_if_should_sleep(self):
    current_time = datetime.fromtimestamp(time.time()).time()

    if (
      (time.time() > self.wanderers_started_at + settings["awake_time_in_seconds"]) or
      not (self.awake_slot_ini <= current_time <= self.awake_slot_end)
    ):
      self._init_black_rain()


  def _go_to_sleep(self):
    self._change_state("asleep")
    self._destroy_all_elements()


    self.asleep_at = time.time()


  def _check_if_should_awake(self):
    current_time = datetime.fromtimestamp(time.time()).time()

    if (
      (time.time() > self.asleep_at + settings["sleep_time_in_seconds"]) and
      (self.awake_slot_ini <= current_time <= self.awake_slot_end)
    ):
      self._awake()



  def _awake(self):
    self._change_state("calling")
    self._init_pulsating_sequence()


  def _change_state(self, new_state):
    print(">>>> change_state:", new_state)
    self.state = new_state


  # def _init_buttons(self):
  #   for key in pins_buttons:
  #     Button(
  #         name=key,
  #         bcm_pin_num=pins_buttons[key]
  #     )




  # def _init_blinking_led(self):
  #   BlinkingLed(
  #     bcm_pin_num=pins_leds["maroon"],
  #     cycle_duration=0.1,
  #     duration_seconds=1
  #   )
