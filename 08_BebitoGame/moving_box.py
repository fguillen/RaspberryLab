import time

from vector_2d import Vector2D
from canvas import Canvas
from color import Color

class MovingBox:
  def __init__(self, color, position, direction, speed, limit):
    self.color = color
    self.position = position
    self.direction = direction
    self.speed = speed
    self.limit = limit

  def update(self, delta = 1.0):
    self.position += self.direction * (self.speed * delta)

    if self.position.x < 0:
      self.position.x = 0
      self.on_collision()

    if self.position.x > self.limit.x:
      self.position.x = self.limit.x
      self.on_collision()

    if self.position.y < 0:
      self.position.y = 0
      self.on_collision()

    if self.position.y > self.limit.y:
      self.position.y = self.limit.y
      self.on_collision()

  """
  Draws the object on the given canvas.

  Args:
    canvas (Canvas): The canvas to draw on.
  """
  def draw(self, canvas):
    position_rounded = Vector2D(round(self.position.x), round(self.position.y))
    # print("position: ", self.position)
    # print("position_rounded: ", position_rounded)

    # color_before = canvas[position_rounded]
    # canvas[position_rounded] = canvas[position_rounded].mix_color_burn(self.color, 0.5)
    # color_after = canvas[position_rounded]
    # print("color_before: ", color_before, "color_after: ", color_after)

    canvas[position_rounded] = self.color



  def on_collision(self):
    self.direction = Vector2D(0, 0)
    self.speed = 0
