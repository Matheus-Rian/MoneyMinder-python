escolha_de_funcao = 0
while (escolha_de_funcao != '4'):
                                                                                                          #Escolha da função primária
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("=\t\t\t         Menu\t\t\t              =")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Digite o número da ação que deseja realizar: \n[1]Transações \n[2]Filtrar Por Categoria \n[3]Porquinho \n[4]Sair\n")
    escolha_de_funcao = input()
    
    #Função no.1 escolhida
    if(escolha_de_funcao == '1'):
        #Escolha da função secundária (função primária = Transações)
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("=\t\t\t   Menu --> Transações\t\t\t      =")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("Digite o número da ação que deseja realizar: \n[1]Ler Todas As Transações \n[2]Adicionar Transação \n[3]Atualizar Transação Existente \n[4]Deletar Transação\n")
        escolha_de_funcao_transacoes = input()
        
        #Função secundária escolhida:'Ler Todas As Transações'
        if(escolha_de_funcao_transacoes == '1'):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("=\t   Menu --> Transações --> Ler Todas As Transações\t      =")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        
        #Função secundária escolhida:'Adicionar Transação'
        if(escolha_de_funcao_transacoes == '2'):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("=\t     Menu --> Transações --> Adicionar Transação\t      =")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        #Função secundária escolhida:'Atualizar Transação'
        if(escolha_de_funcao_transacoes == '3'):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("=\t     Menu --> Transações --> Atualizar Transação\t      =")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        #Função secundária escolhida:'Deletar Transação'
        if(escolha_de_funcao_transacoes == '4'):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("=\t        Menu --> Transações --> Deletar Transação\t      =")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


    #Função no.2 escolhida
    if(escolha_de_funcao == '2'):
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("=\t\t   Menu --> Filtrar por Categoria\t\t      =")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

    #Função no.3 escolhida
    if(escolha_de_funcao == '3'):
        #Escolha da função secundária (função primária = Porquinho)
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("=\t\t\t   Menu --> Porquinho\t\t\t      =")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("Digite o número da ação que deseja realizar: \n[1]Criar Um Porquinho \n[2]Visualizar um Porquinho existente \n[3]Deletar Um Porquinho\n")
        escolha_de_funcao_porquinho = input()

        #Função secundária escolhida:'Criar um Porquinho'
        if(escolha_de_funcao_porquinho == '1'):
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("=\t       Menu --> Porquinho --> Criar Um Porquinho\t      =")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

        

    #Caso o valor seja <1 ou >4 o programa vai mostrar essa frase e rodar novamente
    if(escolha_de_funcao < 1 or escolha_de_funcao > 4):
        print("Valor de escolha inválido! Por favor, digite um valor válido dessa vez.")

print("Programa Encerrado\n")
