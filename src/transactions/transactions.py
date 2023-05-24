class Transactions:
  def __init__(self) -> None:
    self.sizeItems = 0
    self.arq2 = "dados.csv"
    self.items = self.readFromFile()

  def add(self):
    category = self.captureCategory()
    transaction = self.captureNewTransaction()

    if (not(self.items.get(category))):
      self.items[category] = [transaction]
      self.writeToFile()
      return 'Adicionada com sucesso'

    else:
      if (not(self.transactionNameAlreadyExists(category, transaction))):
        self.items[category].append(transaction)
        self.writeToFile()
        return 'Adicionada com sucesso'


  def removeByName(self):
    category = self.captureCategory()
    name = self.captureName()

    index = self.findIndexTransactionByName(category, name)
    if (index != False):
      self.items[category].pop(index)
      self.writeToFile()
      return
    print('Nome não existe!')

  def updateByName(self):
    category = self.captureCategory()
    name = self.captureName()
    transaction = self.captureNewTransaction()

    index = self.findIndexTransactionByName(category, name)
    if (index != False):
      self.items[category][index] = transaction
      return
    print('Nome não existe!')

  def filter(self):
    try:
      category = self.captureCategory()
      return self.items[category]
    except:
      print('Categoria não existe!')

  def size(self):
    for key in self.items.keys():
      self.sizeItems += len(self.items[key])
    return self.sizeItems

  def get_items(self):
    self.readFromFile()
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

  def captureCategory(self):
    return input('Digite a categoria: ')

  def captureName(self):
    return input('Digite o nome: ')

  def captureNewTransaction(self):
    name = input('Digite um novo nome: ')
    value = float(input('Digite um novo valor: '))
    return { 'name': name, 'value': value }

  def writeToFile(self):
    with open(self.arq2, 'w') as file:
        for category in self.items:
            for transaction in self.items[category]:
                file.write(f"{category},{transaction['name']},{transaction['value']}\n")

  def readFromFile(self):
        try:
            items = {}
            with open(self.arq2, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    category, name, value = line.strip().split(',')
                    if not items.get(category):
                        items[category] = [{'name': name, 'value': float(value)}]
                    else:
                        items[category].append({'name': name, 'value': float(value)})
            return items
        except FileNotFoundError:
            pass
