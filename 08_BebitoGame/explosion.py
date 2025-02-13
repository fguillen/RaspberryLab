import time

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from vector_2d import Vector2D

class Explosion(Updatable, Drawable):
  def __init__(self, color, position, speed, canvas, duration=0.1):
    self.color = color
    self.position = position
    self.canvas = canvas
    self.duration = duration
    self.speed = speed
    self.started_at = time.time()

    Updatable.__init__(self)
    Drawable.__init__(self)

  def draw(self):
    self.canvas.fill(self.color)

  def update(self, delta):
    if time.time() > self.started_at + self.duration:
      self._sparks()
      self.destroy()

  def _sparks(self):
    directions = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]

    for direction in directions:
      moving_box = MovingBox(
        self.color,
        self.position,
        Vector2D(direction[0], direction[1]),
        self.speed,
        self.canvas
      )
      moving_box.set_on_collision(lambda mb=moving_box: mb.destroy())

  def destroy(self):
    Updatable.destroy(self)
    Drawable.destroy(self)
