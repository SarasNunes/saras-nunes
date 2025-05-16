def sistema_vendas():
    # Declarar variáveis
    opcao = 0
    frances = 0
    integral = 0
    doce_liso = 0
    doce_farofa = 0
    forma = 0
    
    valor_frances = 1.04
    valor_integral = 1.04
    valor_doce_liso = 1.08
    valor_doce_farofa = 1.11
    valor_forma = 0.95
    valor_total = 0
    
    while opcao != 6:
        # Menu da padaria
        print("-- PADARIA --")
        print("[1] Pão Francês")
        print("[2] Pão Integral")
        print("[3] Pão Doce Liso")
        print("[4] Pão Doce Farofa")
        print("[5] Pão de Forma")
        print("[6] Fim da Compra.")
        opcao = int(input("Escolha sua opção"))
        
        # Casos do sistema
        if opcao ==1:
            Frances = int(input("Digite a quantidadede pão francês que você quer: "))
            valor_total += frances * valor_frances
        elif opcao == 2:   
            integral= int(input("Digite a quantidadede pão integral que você quer: "))
            valor_total += integral * valor_integral
        elif opcao == 3:   
            doce_liso= int(input("Digite a quantidadede pão doce liso que você quer: "))
            valor_total += doce_liso * valor_doce_liso
        elif opcao == 4:   
            doce_farofa= int(input("Digite a quantidadede pão doce farofa que você quer: "))
            valor_total += doce_farofa * valor_doce_farofa
        elif opcao == 5:   
            forma= int(input("Digite a quantidadede pão de forma que você quer: "))
            valor_total += forma * valor_forma
        elif opcao != 6:
            print("Opção inválida. Por favor, tente novamente.")
            
    # Recibo
    print("\n-- RECIBO --")
    if frances > 0:
        print(f"Pão Francês: {frances} unidade x R${valor_frances:.2f} = R${frances * valor_frances:.2f}")
    if integral > 0:
        print(f"Pão Integral: {integral} unidade x R${valor_integral:.2f} = R${integral * valor_integral:.2f}")
    if doce_liso > 0:
        print(f"Pão Doce Liso: {doce_liso} unidade x R${valor_doce_liso:.2f} = R${doce_liso * valor_doce_liso:.2f}")
    if doce_farofa > 0:
        print(f"Pão Doce Farofa: {doce_farofa} unidade x R${valor_doce_farofa:.2f} = R${doce_farofa * valor_doce_farofa:.2f}")
    if forma > 0:
        print(f"Pão Forma: {forma} unidade x R${valor_forma:.2f} = R${forma * valor_forma:.2f}")
    print(f"Valor total: R${valor_total:.2f}")
# Execute o sistema
sistema_vendas()
        
         
    
     
     
    