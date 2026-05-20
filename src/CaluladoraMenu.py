from src.Calculadora import soma, subtracao, multiplicacao, divisao

def menu():
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", soma(a, b))
    elif escolha == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", subtracao(a, b))
    elif escolha == "3":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", multiplicacao(a, b))
    elif escolha == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", divisao(a, b))
    elif escolha == "0":
        print("Saindo...")
    else:
        print("Opção inválida!")

