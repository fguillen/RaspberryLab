import random

class Color:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  """
  Mixes the current color with another color by a given factor.

  Args:
    other (Color): The other color to mix with.
    factor (float): The factor by which to mix the colors.
            Should be between 0 and 1, where 0 returns the current color
            and 1 returns the other color.

  Returns:
    Color: A new Color instance representing the mixed color.
  """
  def mix(self, other, factor):
    r = self.r + (other.r - self.r) * factor
    g = self.g + (other.g - self.g) * factor
    b = self.b + (other.b - self.b) * factor
    return Color(r, g, b)

  def mix_multiply(self, other, factor):
    r = min(max(self.r * other.r * factor, 0), 255)
    g = min(max(self.g * other.g * factor, 0), 255)
    b = min(max(self.b * other.b * factor, 0), 255)
    return Color(r, g, b)

  def mix_color_burn(self, other, factor):
    r = 255 - (255 - self.r) / other.r * factor
    g = 255 - (255 - self.g) / other.g * factor
    b = 255 - (255 - self.b) / other.b * factor
    return Color(r, g, b)

  def fade_out(self, factor):
    r = self.r * factor
    g = self.g * factor
    b = self.b * factor
    return Color(r, g, b)

  def rgb(self):
    return (self.r, self.g, self.b)

  def rgb_rounded(self):
    return [int(e) for e in self.rgb()]

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

  def __eq__(self, other):
    return self.r == other.r and self.g == other.g and self.b == other.b
