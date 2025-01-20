import time
import board
import neopixel
import colorsys
import random

from frame_to_neopixel_sequence import extract_frames
from frame_to_neopixel_sequence import frame_to_neopixel_sequence

image_path = "heart.png"
pixels_per_column = 8
pixels_per_row = 8

frames = extract_frames(image_path, pixels_per_column, pixels_per_row)
neopixel_sequence = frame_to_neopixel_sequence(frames[0], pixels_per_row, pixels_per_column)



def show_frame(pixel_sequence):
  leds = neopixel.NeoPixel(board.D10, 64, brightness=0.2, auto_write=False)
  n = leds.n
  print("Leds num: ", n)

  for i in range(n):
    leds[i] = pixel_sequence[i]

  leds.show()


show_frame(neopixel_sequence)
