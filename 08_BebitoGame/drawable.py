class Drawable():
  all = []

  def __init__(self):
    Drawable.all.append(self)

    super().__init__()

  def draw(self):
    pass
