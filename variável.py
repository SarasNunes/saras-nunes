# Inicialização da variável opção
opção = -1 # começa com valor diferente de 0 para entrar no loop

# Laço principal
opção = int(input("Escolha uma opção: "))

if opção == 1 or opção == 2 or opção == 3 or opção == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opção == 1:
        resultado = num1 + num2 
        print(f"Resultado da soma : {resultado}")
    elif opção ==2:
        resultado = num1 - num2 
        print(f"Resultado da subtração: {resultado}")
    elif opção ==3:
        resultado = num1 * num2 
        print(f"Resultado da multipplicação: {resultado}")
    elif opção ==4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida. ")
elif opção == 0:
    print("Calculadora encerrada.")
else:
    print("Opção inválida. Tente novamente.")