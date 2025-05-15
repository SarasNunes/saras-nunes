#Ssolicita os dados do vendodor
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = int(input("Digite o total de vendas efetuadas: "))

# Verifica  se a meta foi atingida
if total_vendas >= 20:
    bonus = salario_fixo * 0.15
    salario_recebido = salario_fixo + bonus
    
    # Exibe os resultados 
    print("\n--- Resultado ---")
    print(f"Meta atingida! Parabéns, {nome}!")
    print(f"Salário final: R$ {salario_recebido:.2f}")
    print(f"Comissão (15%): R$ {bonus:.2f}")
else:
    print("\n--- rsultado ---")
    print(f"Meta atingida não antigida. Continue se esforçando, {nome}!")