print("="*30)
print("    CALCULADORA EM PYTHON     ")
print("="*30)

while True:
    print('''1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair ''')
    
    escolha = int(input("Escolha uma opção: "))
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    
    if escolha == 1:
        resultado = n1 + n2
        print(f"Resultado: {n1} + {n2} = {resultado}")

    elif escolha == 2:
        resultado = n1 - n2
        print(f"Resultado: {n1} - {n2} = {resultado}")

    elif escolha == 3:
        resultado = n1 * n2
        print(f"Resultado: {n1} x {n2} = {resultado}")

    elif escolha == 4:
        try:
            resultado = n1 / n2
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida")
        print(f"Resultado: {n1} / {n2} = {resultado}")

    elif escolha == 0:
        break

    outro = input("Outro cálculo? (s/n): ")
    if outro == 's':
        continue
    elif outro == 'n':
        break
    else:
        print("Por favor, escolha entre 's' ou 'n' ")
        outro = input("Outro cálculo? (s/n): ")