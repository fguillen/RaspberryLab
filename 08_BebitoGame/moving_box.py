import time

from vector_2d import Vector2D

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

  def draw(self, pixel_grid):
    position_rounded = Vector2D(round(self.position.x), round(self.position.y))
    # print("position: ", self.position)
    # print("position_rounded: ", position_rounded)

    pixel_grid[position_rounded.x, position_rounded.y] = self.color



  def on_collision(self):
    self.direction = Vector2D(0, 0)
    self.speed = 0
