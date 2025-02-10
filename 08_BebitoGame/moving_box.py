import time

from updatable import Updatable
from drawable import Drawable
from vector_2d import Vector2D
from canvas import Canvas
from color import Color

class MovingBox(Updatable, Drawable):
  def __init__(self, color, position, direction, speed, canvas):
    self.color = color
    self.position = position
    self.direction = direction
    self.speed = speed
    self.canvas = canvas

    Updatable.__init__(self)
    Drawable.__init__(self)

  def update(self, delta = 1.0):
    self.position += self.direction * (self.speed * delta)

    if self.position.x < 0:
      self.position.x = 0
      self.on_collision()

    if self.position.x > self.canvas.width - 1:
      self.position.x = self.canvas.width - 1
      self.on_collision()

    if self.position.y < 0:
      self.position.y = 0
      self.on_collision()

    if self.position.y > self.canvas.height - 1:
      self.position.y = self.canvas.height - 1
      self.on_collision()

  """
  Draws the object on the given canvas.

  Args:
    canvas (Canvas): The canvas to draw on.
  """
  def draw(self):
    # color_before = canvas[position_rounded]
    # canvas[position_rounded] = canvas[position_rounded].mix_color_burn(self.color, 0.5)
    # color_after = canvas[position_rounded]
    # print("color_before: ", color_before, "color_after: ", color_after)

    self.canvas[self.position.round()] = self.color

  def on_collision(self):
    self.direction = Vector2D(0, 0)
    self.speed = 0

  def destroy(self):
    Updatable.destroy(self)
    Drawable.destroy(self)
