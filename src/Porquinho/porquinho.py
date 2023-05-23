class Porquinho:
    def __init__(self):
        self.items = {}
        self.tamanho_items = 0
    def criar_porquinho(self, nome):
        if nome in self.items:
            print("Porquinho existente")
        else:
            self.items[nome] = 0
    def update_valor(self, nome):
        if nome in self.items:
            v = float(input(f"Deseja adicionar qual valor para {nome}? Se quiser remover, digite com o "-" na frente do valor. "))
            self.items[nome] += v
            print(f'O valor atual do porquinho é: {self.items[nome]}')
    def tamanho(self):
        self.tamanho_items = len(self.items)
        return self.tamanho_items
    def visualizar_nomes(self):
        for nome in self.items.keys():
            print(nome)
    def remover_nome(self, nome):
        if nome in self.items:
            del self.items[nome]
            print("Nome removido com sucesso.")
        else:
            print("Nome não encontrado.")

