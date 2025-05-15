# Exibe o menu de conversão
print("\n--- Conversor de temperatura ---")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")

# Solicita a opção do usuário
opção = int(input("Escolha um opção (1 ou 2): "))

# Verifica a opção escolhida
if opção == 1:
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (temp_celsius * 9 / 5) + 32
    print(f"Resultado: {temp_celsius}°C = {fahrenheit:.2f}°F")
elif opção == 2:
     temp_celsius = float(input("Digite a temperatura em Celsius: "))
     Kelvin = temp_celsius + 273.15 # Correção da fórmula: 273.15 é o valor padrão
     print(f"resultado: {temp_celsius}°C = {Kelvin:.2f}K")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")