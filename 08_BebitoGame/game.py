import time

from engine import Engine

delay = 0.01
engine = Engine()

try:
  while True:
    engine.update()
    engine.draw()
    time.sleep(delay)

except KeyboardInterrupt:
  print("bye!")
