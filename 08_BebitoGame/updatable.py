class Updatable():
  all = []

  def __init__(self):
    Updatable.all.append(self)

    super().__init__()

  def update(self, delta):
    pass
