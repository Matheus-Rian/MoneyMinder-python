class Porquinho:
	def __init__(self):
		self.arq = "porquinho.csv"
		self.items = self.ler_do_csv()

	def criar_porquinho(self):
		nome = input("Digite o nome do porquinho: ")
		if nome in self.items:
			print("Porquinho já existe")
		else:
			self.items[nome] = 0
			self.salvar_em_csv()
			print("Porquinho adicionado com sucesso")

	def atualizar_valor(self):
		nome = input("Digite o nome do porquinho: ")
		try:
			if nome in self.items:
				valor = float(
					input(f"Deseja adicionar qual valor para {nome}? Se quiser remover, digite com o '-' na frente do valor. ")
				)
				self.items[nome] += valor
				self.salvar_em_csv()
				print (f'O valor atual do porquinho é: {self.items[nome]}')
			else:
				print (f"Porquinho '{nome}' não encontrado.")
		except:
			print('Algo inesperado aconteceu. Tente novamente \n')

	def visualizar_nomes(self):
		porquinhos = []
		for chave in self.items.keys():
			porquinhos.append(chave)
		print(porquinhos)

	def remover_nome(self):
		remove = input("Voce deseja remover qual porquinho? ")
		if remove in self.items:
			del self.items[remove]
			self.salvar_em_csv()		
			print("Nome removido com sucesso.")
		else:
			print("Nome não encontrado.")

	def salvar_em_csv(self):
		with open(self.arq, 'w') as file:
			for nome, valor in self.items.items():
				file.write(f"{nome},{valor}\n")

	def ler_do_csv(self):
		items = {}
		try:
			with open(self.arq, 'r') as file:
				lines = file.readlines()
				for line in lines:
					nome, valor = line.strip().split(',')
					items[nome] = float(valor)
			return items
		except FileNotFoundError:
			pass