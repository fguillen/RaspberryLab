import random

class Color:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def mix(self, other, factor):
    r = self.r + (other.r - self.r) * factor
    g = self.g + (other.g - self.g) * factor
    b = self.b + (other.b - self.b) * factor
    return Color(r, g, b)

  def fade_out(self, factor):
    r = self.r * factor
    g = self.g * factor
    b = self.b * factor
    return Color(r, g, b)

  def rgb(self):
    return (self.r, self.g, self.b)

  def __str__(self):
    return f"({self.r}, {self.g}, {self.b})"

  @staticmethod
  def from_hex(hex_color):
    hex_color = hex_color.lstrip("#")
    return Color(
      int(hex_color[0:2], 16),
      int(hex_color[2:4], 16),
      int(hex_color[4:6], 16)
    )

  @staticmethod
  def from_rgb(rgb):
    return Color(rgb[0], rgb[1], rgb[2])

  @staticmethod
  def random():
    return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

  def to_hex(self):
    return f"#{self.r:02x}{self.g:02x}{self.b:02x}"
