class Updatable():
  all = []

  def __init__(self):
    Updatable.all.append(self)

  def update(self, delta):
    pass

  def destroy(self):
    Updatable.all.remove(self)
