# Solicita ao usuário a quantidade de quilômetros percorridos
km = float(input("Digite a quantidade de KM percorridos: "))
# Solicita ao usuário a quantidade de litros comsumidos 
litros = float(input("Digite a quantidade de litros de combustível comsumidos: "))
# Calcula o comsumo mèdio
if litros != 0:
    consumo = km / litros
    print(f"O comsumo médio do carro é de{consumo:.2f}KM/L.")
else:
    print("Não é possível calcular o consumo com 0 litros.")
    print("Por favor, digite valores numéricos válidos. ")

    