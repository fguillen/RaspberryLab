class Drawable():
  all = []

  def __init__(self):
    Drawable.all.append(self)

  def draw(self):
    pass

  def destroy(self):
    if self in Drawable.all:
      print(">>>> Drawable.remove:", id(self), self.__class__, self)
      Drawable.all.remove(self)
    else:
      print(">>>> Drawable.remove (not found):", id(self), self.__class__, self)
