class Transacoes:
  def __init__(self) -> None:
    self.tamanho_itens = 0
    self.arquivoCSV = "dados.csv"
    self.itens = self.ler_no_arquivo()

  def adicionar(self):
    categoria = self.input_categoria()
    transacao = self.input_nova_transacao()

    if (not(self.itens.get(categoria))):
      self.itens[categoria] = [transacao]
      self.escrever_no_arquivo()
      print('Adicionada com sucesso')
    else:
      if (not(self.nome_ja_existe(categoria, transacao))):
        self.itens[categoria].append(transacao)
        self.escrever_no_arquivo()
        print('Adicionada com sucesso')
        return
      print('Falha na adição. Tente novamente!')

  def remover_pelo_nome(self):
    categoria = self.input_categoria()
    nome = self.input_nome()

    try: 
      index = self.encontrar_index_pelo_nome(categoria, nome)
      self.itens[categoria].pop(index)
      self.escrever_no_arquivo()
    except:
      print('Nome não encontrado...')

  def atualizar_pelo_nome(self):
    categoria = self.input_categoria()
    nome = self.input_nome()
    transacao = self.input_nova_transacao()

    try: 
      index = self.encontrar_index_pelo_nome(categoria, nome)
      self.itens[categoria][index] = transacao
      self.escrever_no_arquivo()
    except:
      print('Nome não encontrado...')

  def filtrar(self):
    try:
      categoria = self.input_categoria()
      for item in self.itens[categoria]:
        print(f'Categoria: {categoria}')
        print('(Nome - Valor) \n')
        print(f"{item['nome']} - R$ {item['valor']} \n")
    except:
      print('Categoria não existe!')

  def size(self):
    for chave in self.itens.keys():
      self.tamanho_itens += len(self.itens[chave])
    return self.tamanho_itens

  def pegar_transacoes(self):
    self.formatar_itens()

  def nome_ja_existe(self, categoria, transacao):
    for valor in self.itens[categoria]:
      if (valor['nome'] == transacao.get('nome')):
        return True
    return False

  def encontrar_index_pelo_nome(self, categoria, nome):
    for i, valor in enumerate(self.itens[categoria]):
      if (valor['nome'] == nome):
        return i
    raise Exception('Nome não encontrado...')

  def input_categoria(self):
    return input('Digite a categoria: ')

  def input_nome(self):
    return input('Digite o nome: ')

  def input_nova_transacao(self):
    nome = input('Digite um novo nome: ')
    valor = float(input('Digite um novo valor: '))
    return { 'nome': nome, 'valor': valor }
    
  def formatar_itens(self):
    for chave in self.itens.keys():
      print(f'Categoria: {chave}')
      print('(Nome - Valor) \n')
      for item in self.itens[chave]:
        print(f"{item['nome']} - R$ {item['valor']} \n")
      print('---------- \n')
    
  def escrever_no_arquivo(self):
    with open(self.arquivoCSV, 'w') as file:
      for categoria in self.itens:
        for transacao in self.itens[categoria]:
          file.write(f"{categoria},{transacao['nome']},{transacao['valor']}\n")

  def ler_no_arquivo(self):
    try:
      itens = {}
      with open(self.arquivoCSV, 'r') as file:
        lines = file.readlines()
        for line in lines:
          categoria, nome, valor = line.strip().split(',')
          if not itens.get(categoria):
            itens[categoria] = [{'nome': nome, 'valor': float(valor)}]
          else:
            itens[categoria].append({'nome': nome, 'valor': float(valor)})
      return itens
    except FileNotFoundError:
        pass    
