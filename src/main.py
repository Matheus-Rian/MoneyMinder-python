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

  transacoes = t.Transacoes()
  porquinho = p.Porquinho()

  opcoes = {
    'Transações': {
      '1': transacoes.pegar_transacoes,
      '2': transacoes.adicionar,
      '3': transacoes.atualizar_pelo_nome,
      '4': transacoes.remover_pelo_nome,
    },
    'Filtrar': {
      '1': transacoes.filtrar
    },
    'Porquinho': {
      '1': porquinho.criar_porquinho,
      '2': porquinho.atualizar_valor,
      '3': porquinho.visualizar_nomes,
      '4': porquinho.remover_nome
    }
  }

  opcoes[tipo][operacao]()