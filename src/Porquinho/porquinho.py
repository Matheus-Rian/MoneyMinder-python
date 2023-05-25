class Porquinho:
	def __init__(self):
		self.arq = "porquinho.csv"
		self.items = self.ler_do_csv()
	def criar_porquinho(self):
		nome = input("Digite o nome do porquinho: ")
		if nome in self.items:
			return "Porquinho já existe"
		else:
			self.items[nome] = 0
			self.salvar_em_csv()
			return "Porquinho adicionado com sucesso"
	def update_valor(self):
		nome = input("Digite o nome do porquinho: ")
		if nome in self.items:
			valor = float(
				input(f"Deseja adicionar qual valor para {nome}? Se quiser remover, digite com o '-' na frente do valor. ")
				)
			self.items[nome] += valor
			self.salvar_em_csv()
			return (f'O valor atual do porquinho é: {self.items[nome]}')
		else:
			return (f"Porquinho '{nome}' não encontrado.")
	def visualizar_nomes(self):
		nomes=[]
		self.salvar_em_csv()
		for nome in self.items.keys():
			nomes.append(nome)
		return nomes
	def remover_nome(self):
		remove= input("Voce deseja remover qual porquinho? ")
		if remove in self.items:
			del self.items[remove]
			self.salvar_em_csv()		
			return "Nome removido com sucesso."
		else:
			return ("Nome não encontrado.")
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