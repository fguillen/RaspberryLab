import time
import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from vector_2d import Vector2D
from color import Color

class BlackRain(Updatable, Drawable):
  def __init__(self, color, canvas, on_completed=None):
    self.color = color
    self.canvas = canvas
    self.rain_canvas = self._init_rain_canvas()
    self.max_time_between_drops = 0.3
    self.drops_speed = 20
    self.drops = []
    self.nex_drop_at = time.time() + self.max_time_between_drops
    self.on_completed = on_completed

    Updatable.__init__(self)
    Drawable.__init__(self)


  def draw(self):
    for i, value in enumerate(self.rain_canvas):
      if value:
        # print(">>>> set color at:", i, self.color)
        self.canvas[i] = self.color


  def update(self, delta=1.0):
    for drop in self.drops:
      flat_position = (drop.position.round().y * self.canvas.width) + drop.position.round().x
      if self.rain_canvas[flat_position]:
        print("BlackRain.deactivating_block at:", flat_position)
        self.rain_canvas[flat_position] = False


    if time.time() > self.nex_drop_at:
      self.nex_drop_at = self._calculate_next_drop_time()
      if self._is_completed():
        self._completed()
      else:
        self._init_new_drop()


  def destroy(self):
    Updatable.destroy(self)
    Drawable.destroy(self)


  def _init_rain_canvas(self):
    return [True for _ in range(self.canvas.width * self.canvas.height)]


  def _get_rain_canvas_block_value(self, position):
    return self.rain_canvas[position.x + position.y * self.canvas.width]


  def _calculate_next_drop_time(self):
    return time.time() + random.uniform(0, self.max_time_between_drops)


  def _is_completed(self):
    return not any(self.rain_canvas)


  def _init_new_drop(self):
    random_start_position = random.randint(0, len(self.rain_canvas))

    for i in range(len(self.rain_canvas)):
      index_position = random_start_position + i
      index_position = index_position % len(self.rain_canvas)
      if self.rain_canvas[index_position]:
        position = Vector2D(index_position % self.canvas.width, index_position // self.canvas.width)
        direction = Vector2D(0, 1)
        drop = MovingBox(Color.from_name("black"), position, direction, self.drops_speed, self.canvas)
        drop.set_on_collision(lambda d=drop: self._completed_drop(d))
        self.drops.append(drop)
        return

    raise Exception("Not active block found", random_start_position)


  def _completed(self):
    print(f">>>>> BlackRain._completed()")
    self.destroy()

    if self.on_completed:
      self.on_completed()


  def _completed_drop(self, drop):
    drop.destroy()
    self.drops.remove(drop)
