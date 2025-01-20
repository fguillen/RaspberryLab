import time
import board
import neopixel
import colorsys
import random

pixels = neopixel.NeoPixel(board.D10, 64, brightness=0.2, auto_write=False)
# pixels[0] = (10, 0, 0)
# pixels[9] = (0, 10, 0)
# pixels.show()

def floats_to_ints(array):
  return ( int(array[0] * 255), int(array[1] * 255), int(array[2] * 255))

def demo(np):
  n = np.n
  print("Leds num: ", n)
  # color = colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
  # print(int(color[0] * 255))
  # print(colorsys.rgb_to_hsv(100, 100, 100))

  # cycle
  # color = (0, 0, 0)
  for x in range(100):
    for i in range(n):
      np[i] = floats_to_ints(colorsys.hsv_to_rgb(random.uniform(0, 1), 1, 0.4))
    np.show()
    time.sleep(0.025)

  # # bounce
  # for i in range(4 * n):
  #   for j in range(n):
  #     np[j] = (0, 0, 128)
  #   if (i // n) % 2 == 0:
  #     np[i % n] = (0, 0, 0)
  #   else:
  #     np[n - 1 - (i % n)] = (0, 0, 0)
  #   np.write()
  #   time.sleep(0.060)

  # # fade in/out
  # for i in range(0, 4 * 256, 8):
  #   for j in range(n):
  #     if (i // 256) % 2 == 0:
  #       val = i & 0xff
  #     else:
  #       val = 255 - (i & 0xff)
  #     np[j] = (val, 0, 0)
  #   np.write()

  # clear
  # for i in range(n):
  #   np[i] = (0, 0, 0)
  # np.write()

demo(pixels)
