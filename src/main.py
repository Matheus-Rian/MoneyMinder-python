import menu as mn
import transactions.transactions as tr

v = mn.menu_principal()

transactions = tr.Transactions()
opcoes = {
  'Transações': {
    '1': transactions.get_items,
    '2': transactions.add,
    '3': transactions.updateByName,
    '4': transactions.removeByName,
  }
}

print(opcoes[v[0]][v[1]]())
print(v)
print(transactions.get_items())