#Sistema de saque de notas
while True:
    try:
        valor = int(input("Digite o valor do saque (min 10, max 1000): "))
        
        # Validação: entre 10 e 1000 e múltiplo de 10
        if 10 <= valor <= 1000 and valor % 10 == 0:
            print(f"\nValor do saque: R$ {valor}")
            
            # Cálculo da melhor distribuição de notas
            n100 = valor // 100
            resto = valor % 100
            
            n50 = resto // 50
            resto = resto % 50
            
            n10 = resto // 10
            
            print("Sugestão de notas:")
            if n100 > 0: print(f"- {n100} nota(s) de R$ 100")
            if n50 > 0:  print(f"- {n50} nota(s) de R$ 50")
            if n10 > 0:  print(f"- {n10} nota(s) de R$ 10")
            break       
        else:
            print("Valor inválido! O valor deve ser entre 10 e 1000 e múltiplo de 10.")

    except ValueError:
        print("Erro: Digite apenas números inteiros.")