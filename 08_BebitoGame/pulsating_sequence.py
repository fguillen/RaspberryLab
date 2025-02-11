from config import pins_buttons
from pulsating import Pulsating

class PulsatingSequence():
  def __init__(self, color, canvas, on_completed=None):
    self.color = color
    self.canvas = canvas
    self.on_completed = on_completed
    self.actual_pulsating_index = -1

    self._next_pulsating()

  def _next_pulsating(self):
    self.actual_pulsating_index += 1
    print(">>>>>>>>>>>>>>>>>>>>>> next pulsating: ", self.actual_pulsating_index)
    if self.actual_pulsating_index >= len(pins_buttons):
      self._completed()
      return

    name = list(pins_buttons)[self.actual_pulsating_index]
    pulsating = Pulsating(name, self.canvas, bcm_pin_num=pins_buttons[name])
    pulsating.set_on_completed(lambda: self._next_pulsating())


  def _completed(self):
    print(">>>>>>>>>>>>>>>>>>>>>> PulsatingSequence.completed")
    if self.on_completed:
      self.on_completed()
