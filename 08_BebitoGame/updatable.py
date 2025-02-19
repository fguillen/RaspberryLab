class Updatable():
  all = []

  def __init__(self):
    # print("Initialize", id(self))
    Updatable.all.append(self)

  def update(self, delta):
    pass

  def destroy(self):
    # print("Destroy", id(self), self.__class__)
    # for e in Updatable.all:
    #   print(id(e), e.__class__)
    if self in Updatable.all:
      Updatable.all.remove(self)
