class Porquinho:
    def __init__(self):
        self.arq = "porquinho.csv"
        self.items = self.ler_do_csv()
        self.tamanho_items = 0

    def criar_porquinho(self):
        nome = input("Digite o nome do porquinho: ")
        if nome in self.items:
            print("Porquinho existente")
        else:
            self.items[nome] = 0
            self.salvar_em_csv()
    def update_valor(self, nome):
        if nome in self.items:
            v = float(input(f"Deseja adicionar qual valor para {nome}? Se quiser remover, digite com o "-" na frente do valor. "))
            self.items[nome] += v
            self.salvar_em_csv()
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
            self.salvar_em_csv()
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
