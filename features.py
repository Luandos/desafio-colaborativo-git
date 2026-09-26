
def subtrair (a , b):
    sub = a-b
def soma (a,b):
    s=a+b
    print(f"A soma é {s}")
    return s

def divisao (a, b):
    d = a / b
    print(f"A divisão é {d}")
    return d

def multiplicacao(a, b):
    m = a * b
    print(f"A multiplicação é {m}")
    return m

def menu():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")
        if opcao == "0":
            print("Encerrando a calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            soma(num1, num2)
        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == "3":
            multiplicacao(num1, num2)
        elif opcao == "4":
            if num2 == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                divisao(num1, num2)
