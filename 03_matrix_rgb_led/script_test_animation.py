# import os
from time import sleep
# import keyboard

from animation import Animation

animations = [
  Animation("creatures.png", 10, 15, 0, 9),
  Animation("creatures.png", 10, 15, 17, 18),
  Animation("creatures.png", 10, 15, 20, 27),
  Animation("creatures.png", 10, 15, 28, 31),
  Animation("creatures.png", 10, 15, 32, 40),
  Animation("creatures.png", 10, 15, 41, 55),
  Animation("creatures.png", 10, 15, 56, 60),
  Animation("creatures.png", 10, 15, 61, 65),
  # Animation("creatures.png", 10, 15, , ),
  # Animation("creatures.png", 10, 15, , ),
  # Animation("creatures.png", 10, 15, , ),
  # Animation("creatures.png", 10, 15, , ),
]

animation_index = -1

def animation_index_up():
  global animation_index
  animation_index = (animation_index + 1) % len(animations)
  return animation_index


if __name__ == "__main__":
  while True:
    animation = animations[animation_index_up()]

    for i in range(animation.num_sprites):
      sprite = animation.get_sprite(i)
      sprite.print()
      sleep(0.2)
      print(f"\r\033[{sprite.height}A", end="")
