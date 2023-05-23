from porquinho import Porquinho
# Exemplo de uso da classe Porquinho
porquinho = Porquinho()

porquinho.criar_porquinho("Porquinho1")  # Criar um porquinho com o nome "Porquinho1"
porquinho.criar_porquinho("Porquinho2")  # Criar outro porquinho com o nome "Porquinho2"

porquinho.visualizar_nomes()  # Exibir os nomes dos porquinhos presentes

porquinho.add()  # Solicitar e adicionar valores aos porquinhos

porquinho.visualizar_nomes()  # Exibir os nomes dos porquinhos presentes
print(f"Tamanho dos itens: {porquinho.tamanho()}")  # Exibir o tamanho dos itens

porquinho.remover_nome("Porquinho1")  # Remover o porquinho "Porquinho1"

porquinho.visualizar_nomes()  # Exibir os nomes dos porquinhos presentes
print(f"Tamanho dos itens: {porquinho.tamanho()}")  # Exibir o tamanho dos itens

