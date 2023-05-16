from transactions import Transactions

objMock = {
  'Casa': [
    {'name': 'Fogão', 'value': 1500}, 
    {'name': 'TV', 'value': 2500}
  ]
}

category = 'Casa'
transaction = { 'name': 'Fogão', 'value': 1500 }
transaction2 = { 'name': 'TV', 'value': 2500 }

def makeSut():
  transactions = Transactions()
  transactions.add(category, transaction)
  transactions.add(category, transaction2)
  return transactions

def test_add_transaction():
  transactions = makeSut()
  assert transactions.size() == 2

def test_get_transactions():
  transactions = makeSut()
  assert objMock == transactions.get_items()

def test_remove_by_name():
  transactions = makeSut()
  transactions.removeByName('TV')
  assert transactions.size() == 1
