class Transactions:
  def __init__(self) -> None:
    self.items = {}
    self.sizeItems = 0

  def add(self, category, transaction):
    if (not(self.items.get(category))):
      self.items[category] = [transaction]
    else:
      if (not(self.transactionAlreadyExists(category, transaction))):
        self.items[category].append(transaction)

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
  
  def transactionAlreadyExists(self, category, transaction):
    for value in self.items[category]:
      if (value['name'] == transaction.get('name')):
        return True
    return False
