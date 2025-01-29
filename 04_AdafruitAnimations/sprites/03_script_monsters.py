import board
import neopixel

# from neopixel_mock.neopixel_mock import NeoPixelMock
# from neopixel_mock.board_mock import BoardMock

import os
import time

from sprites_animation import SpritesAnimation



# Update to match the pin connected to your NeoPixels
pixel_pin = board.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=1, auto_write=False)

animations = []
monster_folder = "./monsters"

for filename in os.listdir(monster_folder):
  if filename.endswith(".png"):
    file_path = os.path.join(monster_folder, filename)
    animation = SpritesAnimation(
      pixels,
      speed=0.4,
      image_path=file_path,
      num_columns=2,
      num_rows=1,
      sprite_ini=0,
      sprite_end=1,
      alternating=False
    )
    animations.append(animation)

while True:
  for animation in animations:
    start_time = time.time()
    while time.time() - start_time < 2:
      animation.animate()


# animation = SpritesAnimation(
#   pixels,
#   speed=1000,
#   image_path="monsters/monster_02.png",
#   num_columns=2,
#   num_rows=1,
#   sprite_ini=0,
#   sprite_end=0,
#   alternating=False
# )

# while True:
#   animation.animate()
