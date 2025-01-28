# import board
# import neopixel
import os

from sprites_animation import SpritesAnimation

from neopixel_mock.neopixel_mock import NeoPixelMock
from neopixel_mock.board_mock import BoardMock

# Update to match the pin connected to your NeoPixels
pixel_pin = BoardMock.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = NeoPixelMock(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

demo_anim = SpritesAnimation(pixels, speed=0.4, image_path="heart.png", num_columns=2, num_rows=1, sprite_ini=0, sprite_end=1)


# animations = []
# monster_folder = "./monsters"

# for filename in os.listdir(monster_folder):
#   if filename.endswith(".png"):
#     file_path = os.path.join(monster_folder, filename)
#     animation = SpritesAnimation(pixels, speed=0.4, image_path=file_path, num_columns=2, num_rows=1, sprite_ini=0, sprite_end=1)
#     animations.append(animation)

# while True:
#   for animation in animations:
#     animation.animate()
#     import time
#     time.sleep(0.5)

animation = SpritesAnimation(pixels, speed=0.4, image_path="monsters/monster_02.png", num_columns=2, num_rows=1, sprite_ini=0, sprite_end=1)

while True:
  animation.animate()
