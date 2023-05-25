def menu_principal():
    try:
        #Função do menu após a primeira escolha do usuário
        def segundo_menu (primeira_escolha_do_usuario):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\t\t           Menu --> " + opcoes_do_primeiro_menu[primeira_escolha_do_usuario -1])
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        #Função do menu após a segunda escolha do usuário
        def terceiro_menu (primeira_escolha_do_usuario, segunda_escolha_do_usuario):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\t        Menu --> " + opcoes_do_primeiro_menu[primeira_escolha_do_usuario -1] + opcoes_do_segundo_menu[segunda_escolha_do_usuario - 1])
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        #Primeiro menu, onde o usuário ainda não escolheu nada
        #A partir do número que o usuário inserir na variável "primeira_escolha_do_usuário", será correspondentemente acessado no vetor "opções_do_primeiro_menu" 
        opcoes_do_primeiro_menu = ["Transações", "Filtrar Por Categoria", "Porquinho"]
        print('[CTRL + D] - FINALIZAR O PROGRAMA')
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t\t\t         Menu")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("Digite o número da ação que deseja realizar: \n[1]Transações \n[2]Filtrar Por Categoria \n[3]Porquinho \n")
        primeira_escolha_do_usuario = int(input())

        #Caso o usuário opte por digitar 1 (Transações), o codigo seguirá esse rumo, onde segue a mesma lógica do primeiro menu
        if (primeira_escolha_do_usuario == 1):
            opcoes_do_segundo_menu = [" --> Ler todas as transações", " --> Adicionar uma transação", " --> Atualizar transação existente", " --> Deletar uma transação"]
            segundo_menu(primeira_escolha_do_usuario)
            print("Digite o número da ação que deseja realizar: \n[1]Ler todas as transações \n[2]Adicionar uma transação \n[3]Atualizar transação existente \n[4]Deletar uma transação \n")
            segunda_escolha_do_usuario = int(input())
            terceiro_menu(primeira_escolha_do_usuario, segunda_escolha_do_usuario)
            return ['Transações', str(segunda_escolha_do_usuario)]

        #Caso o usuário opte por digitar 2 (Filtrar por categoria), o codigo seguirá esse rumo, onde segue a mesma lógica do primeiro menu
        if (primeira_escolha_do_usuario == 2):
            segundo_menu(primeira_escolha_do_usuario)
            return ['Filtrar', '1']
            
        #Caso o usuário opte por digitar 3 (Porquinho), o codigo seguirá esse rumo, onde segue a mesma lógica do primeiro menu
        if(primeira_escolha_do_usuario == 3):
            opcoes_do_segundo_menu = [" --> Criar porquinho", " --> Atualizar porquinho", " --> Visualizar porquinhos", " --> Deletar porquinho"]
            segundo_menu(primeira_escolha_do_usuario)
            print("Digite o número da ação que deseja realizar: \n[1]Criar porquinho \n[2]Atualizar porquinho \n[3]Visualizar porquinhos \n[4]Deletar porquinho \n")
            segunda_escolha_do_usuario = int(input())
            terceiro_menu(primeira_escolha_do_usuario, segunda_escolha_do_usuario)
            return ['Porquinho', str(segunda_escolha_do_usuario)]
    except ValueError:
        print("Você digitou um valor inválido, tente novamente apresentando um valor válido.")
        raise ValueError()
    except:
        raise Exception()