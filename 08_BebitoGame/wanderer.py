import random

from vector_2d import Vector2D
from moving_box import MovingBox

class Wanderer(MovingBox):
  def __init__(self, color, limit):
    position = self._random_position(limit)
    direction = self._random_direction(position, limit)
    speed = 10

    print("Wanderer.__init__", position, direction, speed)

    super().__init__(color, position, direction, speed, limit)

  def _random_position(self, limit):
    border_positions = []
    for row in [0, limit.y]:
      for col in range(0, limit.x + 1):
        border_positions.append(Vector2D(col, row))

    for row in range(0, limit.y + 1):
      for col in [0, limit.x]:
        border_positions.append(Vector2D(col, row))

    border_positions = list(set(border_positions)) # remove duplicates
    position = random.choice(border_positions)

    return position

  def _random_direction(self, position, limit):
    if position.y == 0 or position.y == limit.y:
      return random.choice([Vector2D(1, 0), Vector2D(-1, 0)])
    else:
      return random.choice([Vector2D(0, 1), Vector2D(0, -1)])

  def on_collision(self):
    if self.position.x == 0 and self.direction.y < 0:
      self.direction = Vector2D(1, 0)
    elif self.position.x == self.limit.x and self.direction.y > 0:
      self.direction = Vector2D(-1, 0)
    elif self.position.y == 0 and self.direction.x < 0:
      self.direction = Vector2D(0, 1)
    elif self.position.y == self.limit.y and self.direction.x > 0:
      self.direction = Vector2D(0, -1)

    print("on_collision", self.position, self.direction)
