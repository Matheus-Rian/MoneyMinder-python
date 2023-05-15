class Transactions:
  def __init__(self) -> None:
    self.items = []

  def add(self, transaction):
    self.items.append(transaction)

  def removeByName(self, name):
    for i, value in enumerate(self.get_items()):
      if (value['name'] == name):
        self.items.pop(i)

  def size(self):
    return len(self.items)
  
  def get_items(self):
    return self.items
