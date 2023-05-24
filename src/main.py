import menu as mn
import transactions.transactions as _

[type, option] = mn.menu_principal()

transactions = _.Transactions()
opcoes = {
  'Transações': {
    '1': transactions.get_items,
    '2': transactions.add,
    '3': transactions.updateByName,
    '4': transactions.removeByName,
  },
  'Filtrar': {
    '1': transactions.filter
  }
}

print(opcoes[type][option]())