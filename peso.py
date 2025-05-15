# Solicita os dados do usuário
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (em kg:) "))
altura = float(input("Digite sua altura (em metros): "))

# Calcule do IMC
imc = peso / (altura * altura)

# Exibe o resultado do IMC
print(f"\n{nome}, seu IMC é: {imc:.2f}")

# Classificação com base no valor do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Classificação: Peso normal.")
elif imc >= 25.0 and imc <= 29.9:
    print("Classificação: Sobrepeso.")
else: #IMC >= 30.0 
    print("Classificação: obesidade.")