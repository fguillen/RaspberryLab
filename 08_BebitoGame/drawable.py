class Drawable():
  all = []

  def __init__(self):
    Drawable.all.append(self)

  def draw(self):
    pass

  def destroy(self):
    Drawable.all.remove(self)
