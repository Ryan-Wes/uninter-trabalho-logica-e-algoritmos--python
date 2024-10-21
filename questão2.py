# Exigência de Código 1 de 8: Nome completo e menu inicial
print("""      
---------------------Bem-vindos à Pizzaria do Ryan!--------------------
      """)
print("""
------------------------------Cardápio:--------------------------------
-----------------------------------------------------------------------
-| Tamanho P: Pizza Salgada (PS) R$ 30,00 | Pizza Doce (PD) R$ 34,00 |-
-| Tamanho M: Pizza Salgada (PS) R$ 45,00 | Pizza Doce (PD) R$ 48,00 |-
-| Tamanho G: Pizza Salgada (PS) R$ 60,00 | Pizza Doce (PD) R$ 66,00 |-
-----------------------------------------------------------------------
""")

# Exigência de Código 5 de 8: Acumulador para somar os valores dos pedidos
valor_total = 0

# Exigência de Código 7 de 8: Estrutura de loop while para repetir pedidos
while True:
    # Exigência de Código 2 de 8: Input do sabor e tratamento de erro
    sabor = input("Escolha o sabor (PS - Pizza Salgada / PD - Pizza Doce): ").upper()
    if sabor not in ['PS', 'PD']:
        print("Sabor inválido. Tente novamente.")
        continue  # Exigência de Código 7 de 8: continue para reiniciar o loop em caso de erro

    # Exigência de Código 3 de 8: Input do tamanho e tratamento de erro
    tamanho = input("Escolha o tamanho (P / M / G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  # Exigência de Código 7 de 8: continue para reiniciar o loop em caso de erro

    # Exigência de Código 4 de 8: Estruturas if, elif, else aninhadas para combinar sabor e tamanho
    if sabor == 'PS':  # Pizza Salgada
        if tamanho == 'P':
            valor_pizza = 30
        elif tamanho == 'M':
            valor_pizza = 45
        elif tamanho == 'G':
            valor_pizza = 60
    elif sabor == 'PD':  # Pizza Doce
        if tamanho == 'P':
            valor_pizza = 34
        elif tamanho == 'M':
            valor_pizza = 48
        elif tamanho == 'G':
            valor_pizza = 66

    # Adicionando o valor da pizza ao total
    valor_total += valor_pizza
    print(f"Você pediu uma pizza {sabor} de tamanho {tamanho}. Valor: R$ {valor_pizza:.2f}")

    # Exigência de Código 6 de 8: Pergunta se o cliente deseja fazer mais pedidos
    mais_pedido = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais_pedido == 'N':
        # Exigência de Código 7 de 8: Break para sair do loop
        break

# Exigência de Saída de Console 1 de 4: Mostrar o valor total ao encerrar os pedidos
print(f"\nO valor total do pedido é: R$ {valor_total:.2f}")

# Exigência de Código 8 de 8: Comentários
