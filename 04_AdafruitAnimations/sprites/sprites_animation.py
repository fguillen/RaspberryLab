from adafruit_led_animation.animation import Animation
from adafruit_led_animation.grid import PixelGrid, VERTICAL

from image_to_sprites import image_to_sprites


# Create a class Animation that receives an
# `image_path`, `num_columns`, `num_rows`, `sprite_ini`, `sprite_end`
# The class uses the function `image_to_sprites.py` to get the image,
# generate the sprites and select the ones between `sprite_ini` and `sprite_end`
#
# The class has a method to get each sprite of the animation
# Example usage
class SpritesAnimation(Animation):
  def __init__(self, pixel_object, speed, image_path, num_columns, num_rows, sprite_ini, sprite_end):
    super().__init__(pixel_object, speed, 0xff00ff)

    self.image_path = image_path
    self.num_columns = num_columns
    self.num_rows = num_rows
    self.sprite_ini = sprite_ini
    self.sprite_end = sprite_end
    self.sprites = self._generate_sprites()
    self.num_sprites = len(self.sprites)

    # create a PixelGrid helper to access our strand as a 2D grid
    self.pixel_grid = PixelGrid(pixel_object, 8, 8, orientation=VERTICAL, alternating=True)

    self.actual_sprite = 0

  def draw(self):
    sprite = self.get_sprite(self.actual_sprite)
    self._sprite_to_grid(sprite)


    sprite.print()
    print(f"\r\033[{sprite.height}A", end="")

    self.actual_sprite = (self.actual_sprite + 1) % len(self.sprites)

  def _sprite_to_grid(self, sprite):
    for x in range(sprite.height):
      for y in range(sprite.width):
        pixel = sprite.get_pixel(x, y)
        self.pixel_grid[x, y] = tuple(int(value * 255) for value in pixel.rgb)

  def get_sprite(self, index):
    if index < 0 or index >= len(self.sprites):
      raise IndexError("Sprite index out of range")
    return self.sprites[index]

  def _generate_sprites(self):
    sprites = image_to_sprites(self.image_path, self.num_columns, self.num_rows)
    return sprites[self.sprite_ini:self.sprite_end + 1]
