class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

  def __mul__(self, scalar):
    return Vector2D(self.x * scalar, self.y * scalar)

  def normalize(self):
    return Vector2D(self.x / self.length(), self.y / self.length())

  def length(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

  def __str__(self):
    return f"({self.x}, {self.y})"
