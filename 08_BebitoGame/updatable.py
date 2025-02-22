class Updatable():
  all = []

  def __init__(self):
    print(">>>> Updatable.append", id(self), self.__class__, self)
    Updatable.all.append(self)

  def update(self, delta):
    pass

  def destroy(self):
    # print("Destroy", id(self), self.__class__)
    # for e in Updatable.all:
    #   print(id(e), e.__class__)
    if self in Updatable.all:
      print(">>>> Updatable.remove:", id(self), self.__class__, self)
      Updatable.all.remove(self)
    else:
      print(">>>> Updatable.remove (not found):", id(self), self.__class__, self)
