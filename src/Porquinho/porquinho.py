class Porquinho:
    def __init__(self):
        self.itens = {}
        self.tamanho_itens = 0
    def criar_porquinho(self, nome):
        if nome in self.itens:
            print("Porquinho existente")
        else:
            self.itens[nome] = 0
    def update_valor(self, nome):
        if nome in self.items:
            v = float(input(f"Deseja adicionar qual valor para {nome}? Se quiser remover, digite com o "-" na frente do valor. "))
            self.items[nome] += v
            print(f'O valor atual do porquinho é: {self.items[nome]}')
    def tamanho(self):
        self.tamanho_itens = len(self.itens)
        return self.tamanho_itens
    def visualizar_nomes(self):
        for nome in self.itens.keys():
            print(nome)
    def remover_nome(self, nome):
        if nome in self.itens:
            del self.itens[nome]
            print("Nome removido com sucesso.")
        else:
            print("Nome não encontrado.")

