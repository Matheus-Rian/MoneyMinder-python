from transactions import Transactions

transaction = { 'category': 'Casa', 'name': 'Fogão', 'value': 1500 }
transaction2 = { 'category': 'Casa', 'name': 'TV', 'value': 2500 }

def makeSut():
  transactions = Transactions()
  transactions.add(transaction)
  transactions.add(transaction2)
  return transactions

def test_add_transaction():
  transactions = makeSut()
  assert transactions.size() == 2

def test_get_transactions():
  transactions = makeSut()
  assert transaction in transactions.get_items()

def test_remove_by_name():
  transactions = makeSut()
  transactions.removeByName('TV')
  assert transactions.size() == 1
