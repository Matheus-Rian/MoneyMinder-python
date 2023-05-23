def menu_principal():
    def segundo_menu (primeira_escolha_de_funcao):
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t\t           Menu --> " + opcoes_do_primeiro_menu[int(primeira_escolha_de_funcao) -1])
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    def terceiro_menu (primeira_escolha_de_funcao, segunda_escolha_de_funcao):
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t        Menu --> " + opcoes_do_primeiro_menu[int(primeira_escolha_de_funcao) -1] + opcoes_do_segundo_menu[int(segunda_escolha_de_funcao) - 1])
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    def quarto_menu (primeira_escolha_de_funcao, segunda_escolha_de_funcao, terceira_escolha_de_funcao):
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Menu --> " + opcoes_do_primeiro_menu[int(primeira_escolha_de_funcao) -1] + opcoes_do_segundo_menu[int(segunda_escolha_de_funcao) - 1] + opcoes_do_terceiro_menu[int(terceira_escolha_de_funcao) -1])
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

    opcoes_do_primeiro_menu = ["Transações", "Filtrar Por Categoria", "Porquinho"]
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t\t\t         Menu")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Digite o número da ação que deseja realizar: \n[1]Transações \n[2]Filtrar Por Categoria \n[3]Porquinho \n")
    primeira_escolha_de_funcao = input()

    if (primeira_escolha_de_funcao == "1"):
        opcoes_do_segundo_menu = [" --> Ler todas as transações", " --> Adicionar uma transação", " --> Atualizar transação existente", " --> Deletar uma transação"]
        segundo_menu(primeira_escolha_de_funcao)
        print("Digite o número da ação que deseja realizar: \n[1]Ler todas as transações \n[2]Adicionar uma transação \n[3]Atualizar transação existente \n[4]Deletar uma transação \n")
        segunda_escolha_de_funcao = input()
        terceiro_menu(primeira_escolha_de_funcao, segunda_escolha_de_funcao)
        return ['Transações', segunda_escolha_de_funcao]

    if (primeira_escolha_de_funcao == "2"):
        opcoes_do_segundo_menu = [" "]
        segundo_menu(primeira_escolha_de_funcao)
        
    if(primeira_escolha_de_funcao == "3"):
        opcoes_do_segundo_menu = [" --> Criar porquinho", " --> Visualizar porquinho", " --> Deletar porquinho"]
        segundo_menu(primeira_escolha_de_funcao)
        print("Digite o número da ação que deseja realizar: \n[1]Criar porquinho \n[2]Visualizar porquinho \n[3]Deletar porquinho \n")
        segunda_escolha_de_funcao = input()
        if(segunda_escolha_de_funcao == "2"):
            opcoes_do_terceiro_menu = [" --> Adicionar dinheiro", " --> Remover dinheiro", " --> Visualizar valor total"]
            terceiro_menu(primeira_escolha_de_funcao, segunda_escolha_de_funcao)
            print("Digite o número da ação que deseja realizar: \n[1]Adicionar dinheiro \n[2]Remover dinheiro \n[3]Visualizar valor total \n")
            terceira_escolha_de_funcao = input()
            quarto_menu(primeira_escolha_de_funcao, segunda_escolha_de_funcao, terceira_escolha_de_funcao)
        else:
            terceiro_menu(primeira_escolha_de_funcao, segunda_escolha_de_funcao)