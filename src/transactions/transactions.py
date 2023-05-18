class Transactions:
  def __init__(self) -> None:
    self.items = {}
    self.sizeItems = 0

  def add(self, category, transaction):
    if (not(self.items.get(category))):
      self.items[category] = [transaction]
    else:
      if (not(self.transactionNameAlreadyExists(category, transaction))):
        self.items[category].append(transaction)

  def removeByName(self, category, name):
    index = self.findIndexTransactionByName(category, name)
    if (not(index)):
      return 'Nome não existe'

    self.items[category].pop(index)

  def updateByName(self, category, name, transaction):
    index = self.findIndexTransactionByName(category, name)
    if (not(index)):
      return 'Nome não existe'

    self.items[category][index] = transaction 

  def size(self):
    for key in self.items.keys():
      self.sizeItems += len(self.items[key])
    return self.sizeItems
  
  def get_items(self):
    return self.items
  
  def transactionNameAlreadyExists(self, category, transaction):
    for value in self.items[category]:
      if (value['name'] == transaction.get('name')):
        return True
    return False
  
  def findIndexTransactionByName(self, category, name):
    for i, value in enumerate(self.items[category]):
      if (value['name'] == name):
        return i
    return False
