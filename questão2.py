# Exigência de Código 1 de 7: Print com meu nome completo
print("""   
Bem-vindos à Madeireira do Lenhador Ryan Lopes!
""")

# Exigência de Código 2 de 7: Função para escolher o tipo de madeira
def escolha_tipo():
    while True:
        tipo = input("""
---------------------------------------------------------------------
Tora de Pinho (PIN) R$ 150,40 
Tora de Peroba (PER) R$ 170,20 
Tora de Mogno (MOG) R$ 190,90
Tora de Ipê (IPE) R$ 210,10
Tora de Imbuia (IMB) R$ 220,70
---------------------------------------------------------------------    
                      """).upper()
        if tipo == "PIN":
            return 150.40  # Valor para Tora de Pinho
        elif tipo == "PER":
            return 170.20  # Valor para Tora de Peroba
        elif tipo == "MOG":
            return 190.90  # Valor para Tora de Mogno
        elif tipo == "IPE":
            return 210.10  # Valor para Tora de Ipê
        elif tipo == "IMB":
            return 220.70  # Valor para Tora de Imbuia
        else:
            print("Tipo de madeira inválido. Tente novamente.")  # Exigência de Saída 2 de 4

# Exigência de Código 3 de 7: Função para quantidade de toras
def qtd_toras():
    while True:
        try:
            qtd = float(input("Digite a quantidade de toras (em m³): "))
            if qtd > 2000:
                print("Quantidade máxima de toras aceita é 2000. Tente novamente.")  # Exigência de Saída 3 de 4
                continue
            elif qtd < 100:
                desconto = 0
            elif qtd < 500:
                desconto = 0.04
            elif qtd < 1000:
                desconto = 0.09
            elif qtd <= 2000:
                desconto = 0.16
            return qtd, desconto
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

# Exigência de Código 4 de 7: Função para escolher o tipo de transporte
def transporte():
    while True:
        tipo_transporte = input("Escolha o tipo de transporte (1: Rodoviário, 2: Ferroviário, 3: Hidroviário): ")
        if tipo_transporte == "1":
            return 1000  # Transporte rodoviário
        elif tipo_transporte == "2":
            return 2000  # Transporte ferroviário
        elif tipo_transporte == "3":
            return 2500  # Transporte hidroviário
        else:
            print("Opção de transporte inválida. Tente novamente.")

# Exigência de Código 5 de 7: Cálculo total a pagar
# Chamando as funções e calculando o total
tipo_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
custo_transporte = transporte()

# Cálculo total com as regras do enunciado
total = ((tipo_madeira * quantidade) * (1 - desconto)) + custo_transporte

# Exigência de Código 6 de 7: Implementação de try/except já realizada na função qtd_toras

# Exigência de Código 7 de 7: Comentários relevantes já inseridos

# Exigência de Saída de Console 1 de 4: Mensagem com meu nome
print("Bem-vindos à Madeireira do Lenhador Ryan Lopes")

# Exigência de Saída de Console 4 de 4: Mostrar total a pagar
print(f"O total a pagar é: R$ {total:.2f}")
