from button import Button
import keyboard

class ButtonMock(Button):
  def __init__(self, name, key, on_button_pressed=None):
    self.key = key
    super().__init__(name, bcm_pin_num=0, on_button_pressed=on_button_pressed)

  def on_destroy(self):
    pass

  def __str__(self):
    return f"Button[{self.name}]:{self.value}"

  def _load_value(self):
    value = keyboard.is_pressed(self.key)
    # print(f"load_value.${self.key}:", value)
    return value

  def _setup_gpio(self):
    pass
