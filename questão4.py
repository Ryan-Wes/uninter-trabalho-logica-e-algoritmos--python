# Exigência de Código 1 de 8: Print com meu nome completo
print("""
      Bem-vindos ao sistema de gerenciamento de contatos do Wesley Ryan Lopes da Rocha
      """)

# Exigência de Código 2 de 8: Lista de contatos e id_global
lista_contatos = []
id_global = 123456  # Coloque aqui seu RU

# Exigência de Código 3 de 8: Função para cadastrar contato
def cadastrar_contato(id):
    print(f"Cadastro de Contato - ID: {id}")  # Exibe o ID do contato
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")
    
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }
    
    lista_contatos.append(contato.copy())  # Armazena o dicionário na lista
    print(f"\nContato {nome} cadastrado com sucesso!\n")

# Exigência de Código 4 de 8: Função para consultar contatos
def consultar_contatos():
    while True:
        opcao = input("""
---------------------------------------------------------------------
Escolha uma opção:
1. Consultar Todos
2. Consultar por Id
3. Consultar por Atividade
4. Retornar ao menu
---------------------------------------------------------------------
""")
        
        if opcao == "1":
            print("\n---------------------- Contatos Cadastrados ----------------------")
            for contato in lista_contatos:
                print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")
            print("-------------------------------------------------------------------\n")
        elif opcao == "2":
            id = int(input("Informe o Id do contato: "))
            for contato in lista_contatos:
                if contato['id'] == id:
                    print("\n-------------------- Contato Encontrado ---------------------")
                    print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")
                    print("-------------------------------------------------------------\n")
                    break
            else:
                print("Contato não encontrado.\n")
        elif opcao == "3":
            atividade = input("Informe a atividade: ")
            print("\n--------------------- Contatos por Atividade ---------------------")
            found = False
            for contato in lista_contatos:
                if contato['atividade'].lower() == atividade.lower():
                    print(f"ID: {contato['id']} | Nome: {contato['nome']} | Telefone: {contato['telefone']}")
                    found = True
            if not found:
                print("Nenhum contato encontrado para essa atividade.")
            print("-------------------------------------------------------------------\n")
        elif opcao == "4":
            return
        else:
            print("Opção inválida.\n")

# Exigência de Código 5 de 8: Função para remover contato
def remover_contato():
    while True:
        id = int(input("Informe o Id do contato a ser removido: "))
        for contato in lista_contatos:
            if contato['id'] == id:
                lista_contatos.remove(contato)
                print("Contato removido com sucesso.\n")
                return
        print("Id inválido. Tente novamente.\n")

# Exigência de Código 6 de 8: Menu no código principal
while True:
    opcao = input("""
---------------------------------------------------------------------
Escolha uma opção:
1. Cadastrar Contato
2. Consultar Contato
3. Remover Contato
4. Encerrar Programa
---------------------------------------------------------------------
""")
    
    if opcao == "1":
        id_global += 1  # Incrementa o id global
        cadastrar_contato(id_global)
    elif opcao == "2":
        consultar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.\n")

# Exigência de Código 7 de 8: Lista de dicionários já implementada com lista_contatos
# Exigência de Código 8 de 8: Comentários relevantes já inseridos

# Exigência de Saída de Console 1 de 6: Cadastro do meu contato
cadastrar_contato(id_global)  # Nome: Ryan Lopes, Atividade: Estudante, Telefone: RU

# Exigência de Saída de Console 2 de 6: Cadastro de mais 2 contatos
id_global += 1
cadastrar_contato(id_global)  # Nome: João Silva, Atividade: Marceneiro, Telefone: 987654321
id_global += 1
cadastrar_contato(id_global)  # Nome: Maria Souza, Atividade: Marceneira, Telefone: 123456789

# Exigência de Saída de Console 3 de 6: Consulta de todos os contatos
print("Consulta de todos os contatos:")
consultar_contatos()

# Exigência de Saída de Console 4 de 6: Consulta por código (id)
print("Consulta por código (id):")
id = 123456  # Troque pelo ID que deseja consultar
for contato in lista_contatos:
    if contato['id'] == id:
        print("\n-------------------- Contato Encontrado ---------------------")
        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")
        print("-------------------------------------------------------------\n")

# Exigência de Saída de Console 5 de 6: Consulta por atividade
print("Consulta por atividade (Marceneiro):")
for contato in lista_contatos:
    if contato['atividade'].lower() == "marceneiro":
        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Telefone: {contato['telefone']}")

# Exigência de Saída de Console 6 de 6: Remoção de um dos contatos
remover_contato()  # Remova um contato pelo id
print("Consulta após remoção:")
consultar_contatos()
