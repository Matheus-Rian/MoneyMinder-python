def menu1escolha (escolha_de_funcao):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t\t           Menu --> " + menu0[int(escolha_de_funcao) -1])
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
def menu2escolha (escolha_de_funcao, escolha_de_funcao1):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t        Menu --> " + menu0[int(escolha_de_funcao) -1] + menu1[int(escolha_de_funcao1) - 1])
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
def menu3escolha (escolha_de_funcao, escolha_de_funcao1, escolha_de_funcao2):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Menu --> " + menu0[int(escolha_de_funcao) -1] + menu1[int(escolha_de_funcao1) - 1] + menu2[int(escolha_de_funcao2) -1])
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


menu0 = ["Transações", "Filtrar Por Categoria", "Porquinho"]
print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\t\t\t         Menu")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
print("Digite o número da ação que deseja realizar: \n[1]Transações \n[2]Filtrar Por Categoria \n[3]Porquinho \n")
escolha_de_funcao = input()

if (escolha_de_funcao == "1"):
    menu1 = [" --> Ler todas as transações", " --> Adicionar uma transação", " --> Atualizar transação existente", " --> Deletar uma transação"]
    menu1escolha(escolha_de_funcao)
    print("Digite o número da ação que deseja realizar: \n[1]Ler todas as transações \n[2]Adicionar uma transação \n[3]Atualizar transação existente \n[4]Deletar uma transação \n")
    escolha_de_funcao1 = input()
    menu2escolha(escolha_de_funcao, escolha_de_funcao1)

if (escolha_de_funcao == "2"):
    menu1 = [" "]
    menu1escolha(escolha_de_funcao)
if(escolha_de_funcao == "3"):
    menu1 = [" --> Criar porquinho", " --> Visualizar porquinho", " --> Deletar porquinho"]
    menu1escolha(escolha_de_funcao)
    print("Digite o número da ação que deseja realizar: \n[1]Criar porquinho \n[2]Visualizar porquinho \n[3]Deletar porquinho \n")
    escolha_de_funcao1 = input()
    if(escolha_de_funcao1 == "2"):
        menu2 = [" --> Adicionar dinheiro", " --> Remover dinheiro", " --> Visualizar valor total"]
        menu2escolha(escolha_de_funcao, escolha_de_funcao1)
        print("Digite o número da ação que deseja realizar: \n[1]Adicionar dinheiro \n[2]Remover dinheiro \n[3]Visualizar valor total \n")
        escolha_de_funcao2 = input()
        menu3escolha(escolha_de_funcao, escolha_de_funcao1, escolha_de_funcao2)
    else:
        menu2escolha(escolha_de_funcao, escolha_de_funcao1)