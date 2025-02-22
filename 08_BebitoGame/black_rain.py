import time
import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from vector_2d import Vector2D
from color import Color

class BlackRain(Updatable, Drawable):
  def __init__(self, color, canvas, on_completedd=None):
    self.color = color
    self.canvas = canvas
    self.rain_canvas = self._init_rain_canvas()
    self.max_time_between_drops = 0.5
    self.drops = []
    self.nex_drop_at = time.time() + self.max_time_between_drops
    self.on_completedd = on_completedd

    Updatable.__init__(self)
    Drawable.__init__(self)


  def draw(self):
    for i in len(self.rain_canvas):
      if self.rain_canvas[i]:
        self.canvas[i] == self.color


  def update(self, delta=1.0):
    for drop in self.drops:
      flat_position = (drop.position.y * self.canvas.width) + drop.position.x
      self.rain_canvas[flat_position] = False


    if time.time() > self.nex_drop_at:
      self.nex_drop_at = self._calculate_next_drop_time
      if self._is_completed():
        self._completed()
      else:
        self._init_new_drop()


  def destroy(self):
    Updatable.destroy(self)
    Drawable.destroy(self)


  def _init_rain_canvas(self):
    return [[True for _ in range(self.canvas.width * self.canvas.height)]]


  def _get_rain_canvas_block_value(self, position):
    return self.rain_canvas[position.x + position.y * self.canvas.width]


  def _calculate_next_drop_time(self):
    return time.time() + random.uniform(0, self.max_time_between_drops)


  def _is_completed(self):
    return not any(self.rain_canvas)


  def _init_new_drop(self):
    random_start_position = random.randint(0, len(self.rain_canvas))

    for i in len(self.rain_canvas):
      index_position = random_start_position + i
      if self.rain_canvas(index_position % len(self.rain_canvas)):
        position = Vector2D(index_position % self.canvas.width, index_position // self.canvas.width)
        direction = Vector2D(0, -1)
        speed = 2
        drop = MovingBox(Color.from_name("black"), position, direction, speed, self.canvas)
        drop.set_on_collision(lambda d=drop: self._completed_drop(d))


  def _completed(self):
    print(f">>>>> BlackRain._completed()")
    if self.on_completed:
      self.on_completed()

    self.destroy()


  def _completed_drop(self, drop):
    self.drops.remove(drop)
    drop.destroy()
