#importou a biblioteca random
import random
#Declarar variáveis 
numero_secreto = random.randint (1,10)
tentativas =0
contagem_tentativas = 0 
#Introdução ao jogo
print ("Bem-vindo ao jogo do Número Secreto")
print ("Tente adivinhar o número entre 1 a 10.")
# Laço de repetição
while tentativas != numero_secreto:
    numero = int(input("Digite um número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto.")
        print (f"Você precisa de {contagem_tentativas }")
        break 
    elif numero < numero_secreto:
        print ("O número secreto é maior.")
    else:
        print ("O número secreto é menor.")
    
''