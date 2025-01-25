import time
import board
import neopixel
# import colorsys
# import random

from image_to_frames import extract_frames
from frame_to_neopixel_sequence import frame_to_neopixel_sequence

image_path = "heart.png"
pixels_per_column = 8
pixels_per_row = 8

frames = extract_frames(image_path, pixels_per_column, pixels_per_row)
neopixel_frame_1 = frame_to_neopixel_sequence(frames[0], pixels_per_row, pixels_per_column)
neopixel_frame_2 = frame_to_neopixel_sequence(frames[1], pixels_per_row, pixels_per_column)



def show_frame(pixel_sequence):
  leds = neopixel.NeoPixel(board.D10, 64, brightness=0.1, auto_write=False)
  n = leds.n
  print("Leds num: ", n)

  for i in range(n):
    leds[i] = pixel_sequence[i]

  leds.show()


while True:
  show_frame(neopixel_frame_1)
  time.sleep(0.5)
  show_frame(neopixel_frame_2)
  time.sleep(0.5)
