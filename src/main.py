import menu as mn
import transactions.transactions as _
import Porquinho.porquinho as p

[type, option] = mn.menu_principal()

transactions = _.Transactions()
porquinho = p.Porquinho()

opcoes = {
  'Transações': {
    '1': transactions.get_items,
    '2': transactions.add,
    '3': transactions.updateByName,
    '4': transactions.removeByName,
  },
  'Filtrar': {
    '1': transactions.filter
  },'Porquinho':{
      '1': porquinho.criar_porquinho,
  }
}
        #print("Digite o número da ação que deseja realizar: \n[1]Criar porquinho \n[2]Visualizar porquinho \n[3]Deletar porquinho \n")

print(opcoes[type][option]())