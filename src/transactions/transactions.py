class Transactions:
  def __init__(self) -> None:
    self.items = {}
    self.sizeItems = 0

  def add(self, category, transaction):
    if (self.items.get(category)):
      self.items[category].append(transaction)
    else:
      self.items[category] = [transaction]

  def removeByName(self, name):
    for key in self.items.keys():
      for i, value in enumerate(self.items[key]):
        if (value['name'] == name):
          self.items[key].pop(i)

  def size(self):
    for key in self.items.keys():
      self.sizeItems += len(self.items[key])

    return self.sizeItems
  
  def get_items(self):
    return self.items
