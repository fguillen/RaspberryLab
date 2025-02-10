
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

  def __mul__(self, scalar):
    if isinstance(scalar, (int, float)):
        return Vector2D(self.x * scalar, self.y * scalar)
    else:
        raise TypeError("Scalar must be a number:", scalar)

  def normalize(self):
    return Vector2D(self.x / self.length(), self.y / self.length())

  def round(self):
    result = Vector2D(round(self.x), round(self.y))
    return result

  def rotate_90_degrees_clockwise(self):
    return Vector2D(self.y, -self.x)

  def rotate_90_degrees_counterclock(self):
    return Vector2D(-self.y, self.x)

  def length(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

  def __str__(self):
    return f"({self.x}, {self.y})"

  def __eq__(self, other):
    if isinstance(other, Vector2D):
      return self.x == other.x and self.y == other.y
    return False

  def __hash__(self):
    return hash((self.x, self.y))
