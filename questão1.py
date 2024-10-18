# Exigência de Saída de Console 1 de 2: Nome completo
print("Bem vindo ao Sistema do Ryan")

# Exigência de Código 2 de 6: Input do valorBase do plano e da idade do cliente
valor_base = input("Informe o valor base do plano: R$ ")
valor_base = float(valor_base.replace(',', '.'))  # Substitui a vírgula por ponto para evitar erros de conversão
idade = int(input("Informe a idade do cliente: "))

# Exigência de Código 3 de 6: Implementação das regras de valores com base na idade
if idade < 0:  # Verificação de idade inválida
    print("Idade inválida.")
    porcentagem = 0  # Não calcula valor para idade inválida
else:
    if idade >= 0 and idade < 19:
        porcentagem = 100 / 100  # 100%
    elif idade >= 19 and idade < 29:
        porcentagem = 150 / 100  # 150%
    elif idade >= 29 and idade < 39:
        porcentagem = 225 / 100  # 225%
    elif idade >= 39 and idade < 49:
        porcentagem = 240 / 100  # 240%
    elif idade >= 49 and idade < 59:
        porcentagem = 350 / 100  # 350%
    elif idade >= 59:
        porcentagem = 600 / 100  # 600%

    # Exigência de Código 4 de 6: Cálculo do valor mensal
    valor_mensal = valor_base * porcentagem

    # Exigência de Código 5 de 6: Uso das estruturas if, elif, else já implementado

    # Exigência de Código 6 de 6: Comentários relevantes
    # O valor mensal do plano é calculado com base no valor base e na porcentagem correspondente à idade do cliente

    # Exigência de Saída de Console 2 de 2: Apresentação do valor mensal se idade for >= 29 anos
    if idade >= 29:
        print(f"O valor mensal do plano para um cliente de {idade} anos é: R$ {valor_mensal:.2f}")
