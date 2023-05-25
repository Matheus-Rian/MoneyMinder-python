from transactions import Transactions

objMock = {
  'Casa': [
    {'name': 'Fogão', 'value': 1500}, 
    {'name': 'TV', 'value': 2500}
  ]
}

objMockUpdated = {
  'Casa': [
    {'name': 'Fogão', 'value': 1500}, 
    {'name': 'TV', 'value': 1500}
  ]
}

category = 'Casa'
transaction = { 'name': 'Fogão', 'value': 1500 }
transaction2 = { 'name': 'TV', 'value': 2500 }
transaction3 = { 'name': 'TV', 'value': 2500 }

def makeSut():
  transactions = Transactions()
  transactions.add(category, transaction)
  transactions.add(category, transaction2)
  return transactions

def test_add_transaction():
  transactions = makeSut()
  assert transactions.size() == 2

def test_not_allow_add_transaction_with_existing_name():
  transactions = makeSut()
  transactions.add(category, transaction3)
  assert transactions.size() == 2

def test_get_transactions():
  transactions = makeSut()
  assert objMock == transactions.pegar_transacoes()

def test_remove_by_name():
  transactions = makeSut()
  transactions.remover_pelo_nome(category, 'TV')
  assert transactions.size() == 1

def test_remove_by_name_not_exists():
  transactions = makeSut()
  v = transactions.remover_pelo_nome(category, 'TV2')
  assert v == 'Nome não existe!'

def test_update_by_name():
  transactions = makeSut()
  transactions.atualizar_pelo_nome(category, 'TV', {'name': 'TV', 'value': 1500})
  assert objMockUpdated == transactions.pegar_transacoes()

def test_update_by_name_not_exists():
  transactions = makeSut()
  v = transactions.atualizar_pelo_nome(category, 'TV2', {'name': 'TV2', 'value': 1500})
  assert v == 'Nome não existe!'