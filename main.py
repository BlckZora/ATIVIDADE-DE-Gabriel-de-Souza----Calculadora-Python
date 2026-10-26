from calculadora import adicao, subtrair, multiplicacao, divisao
from time import sleep

print("="*30)
print("    CALCULADORA EM PYTHON     ")
print("="*30)

while True:
    print('''1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair ''')
    
    escolha = int(input("Escolha a sua opção: "))
    if escolha == 0:
        break

    try:
        n1 = int(input("Escolha o primeiro número: "))
        n2 = int(input("Escolha o segundo número: "))
    except ValueError:
        print("Erro: Os valores inseridos não são números. Tente novamente:")

        sleep(1)
        continue

    match escolha:
        case 1:
            print(f"Equação: {n1} + {n2} = {adicao(n1, n2)}")
    
        case 2:
            print(f"Equação: {n1} + {n2} = {subtrair(n1, n2)}")

        case 3:
            print(f"Equação: {n1} + {n2} = {multiplicacao(n1, n2)}")

        case 4:
            try:
                resultado = divisao(n1, n2)
            except ZeroDivisionError:
                print("ERRO: A DIVISÃO NÃO PODE SER FEITA COM 0. TENTE NOVAMENTE: ")
                sleep(1)
                continue

            print(f"Equação: {n1} + {n2} = {resultado}")

        case _:
            print("Opção inválida. Tente novamente.")

    outro = input("Deseja fazer outro cálculo? (s/n): ")
    if outro == 's':
        continue
    elif outro == 'n':
        break
    else:
        print("Escolha entre 's' ou 'n' ")
        outro = input("Deseja fazer outro cálculo? (s/n): ")