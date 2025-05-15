# Solicita ao usuário o valor total da compra 
valor_total = float(input("Digite o valor total a compra; R$ "))

# Calcula o valor de cada uma das 5 prestações (sem juros)
pretacao = valor_total / 5

# Exibe os resuldos 
print("\nresumo da Compra: ")
print(f"valor total da compra: R$ {valor_total:.2f}")
print("valor de cada prestações: R$ {prestacao:.2f}")
