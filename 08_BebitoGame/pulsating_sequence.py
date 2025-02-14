from config import pins_buttons
from pulsating import Pulsating

class PulsatingSequence():
  def __init__(self, color, canvas, engine, on_completed=None):
    self.color = color
    self.canvas = canvas
    self.engine = engine
    self.on_completed = on_completed
    self.actual_pulsating_index = -1

    self._next_pulsating()

  def _next_pulsating(self):
    self.actual_pulsating_index += 1
    name = list(pins_buttons)[self.actual_pulsating_index]
    pulsating = Pulsating(name, self.canvas)
    pulsating.set_on_completed(lambda p=pulsating: self._pulsating_completed(p))

  def _pulsating_completed(self, pulsating):
    self.engine.init_wander(pulsating.name)

    if self.actual_pulsating_index >= len(pins_buttons) - 1:
      self._sequence_completed()
      return

    self._next_pulsating()

  def _sequence_completed(self):
    if self.on_completed:
      self.on_completed()
