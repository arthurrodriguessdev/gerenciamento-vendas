clientes = {}
vendas = {}

def cadastrar_cliente():
    email_novo_cliente = input("\nDigite o e-mail do cliente: ")

    if email_novo_cliente in clientes:
        print("\nCliente já cadastrado!")

    else:
        nome_novo_cliente = input("\nDigite o nome do cliente: ")
        idade_novo_cliente = input("Informe a idade do cliente: ")

        try:
            idade_novo_cliente = int(idade_novo_cliente)
            clientes[email_novo_cliente] = {'Nome': nome_novo_cliente, 'Idade': idade_novo_cliente}

            print("\nCliente cadastrado com sucesso!\n")
        except ValueError:
            print("\nSomente números!\n")

def registrar_compra():
    if len(clientes) > 0:
        i = 1
        for email in clientes:
            print("\n", i, "-", email, "\n")
            i += 1

        cliente_selecionar = input("Informe o e-mail do cliente que deseja realizar a compra: ").strip().lower()

        if cliente_selecionar in clientes:
            nome_produto = input("Digite o nome do produto: ")
            valor_produto = input("Digite o valor do produto: ")

            try:
                valor_produto = float(valor_produto)
                vendas[cliente_selecionar] = {'Produto': nome_produto, 'Valor': valor_produto}
                print("\nCompra registrada com sucesso!\n")

            except ValueError:
                print("\nSomente números!\n")
        else:
            print("\nNome inválido!\n")

    else:
        print("\nSem clientes cadastrados!")

def listar_clientes():
    if clientes:
        print("\n=== LISTA DE CLIENTES ===\n")

        i = 1
        for nome, dd in clientes.items():
            print(f"{i} - {clientes['Nome']}")
            i += 1
    else:
        print("\nLista de clientes vazia!\n")
        
menu_principal = True
while menu_principal:
    print("1 - Cadastrar novo cliente")
    print("2 - Registrar nova compra")
    print("3 - Listar todos os clientes")
    print("4 - Listar compras de um cliente")
    print("5 - Buscar cliente por nome")
    print("6 - Relatório geral de vendas")
    print("7 - Gerar relatório personalizado")
    print("8 - Sair\n")

    selecionar_opcao = input("Digite o número referente a opção desejada: ")

    try:
        selecionar_opcao = int(selecionar_opcao)
    except ValueError:
        print("\nSomente números!")

    if selecionar_opcao == 1:
        cadastrar_cliente()

    elif selecionar_opcao == 2:
        registrar_compra()

    elif selecionar_opcao == 3:
        listar_clientes()

    elif selecionar_opcao == 8:
        menu_principal= False
        print("\nSaída realizada com sucesso!")