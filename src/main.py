import menu as m
import Porquinho.porquinho as p
import Transacoes.transacoes as t

while True:
  try:
    [tipo, operacao] = m.menu_principal()
  except ValueError:
    continue
  except:
    break

  transactions = t.Transacoes()
  porquinho = p.Porquinho()

  opcoes = {
    'Transações': {
      '1': transactions.pegar_transacoes,
      '2': transactions.adicionar,
      '3': transactions.atualizar_pelo_nome,
      '4': transactions.remover_pelo_nome,
    },
    'Filtrar': {
      '1': transactions.filtrar
    },
    'Porquinho': {
      '1': porquinho.criar_porquinho,
      '2': porquinho.update_valor,
      '3': porquinho.visualizar_nomes,
      '4': porquinho.remover_nome
    }
  }

  print(opcoes[tipo][operacao]())