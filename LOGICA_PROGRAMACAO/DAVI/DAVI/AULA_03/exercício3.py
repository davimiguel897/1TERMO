print("Calculadora")
valor1 = float(input("Insira o primeiro valor \n"))
valor2 = float(input("Insira o segundo valor \n"))
operador = input("Insira o operador \n")

if operador == "+":
    resultado = valor1 + valor2
    print("O resultado é:", resultado)

elif operador == "-":
    resultado = valor1 - valor2
    print("O resultado é:", resultado)

elif operador == "*":
    resultado = valor1 * valor2
    print("O resultado é:", resultado)

elif operador == "/":
    resultado = valor1 / valor2
    print("O resultado é:", resultado)

elif operador == "%":
    resultado = valor1 * valor2 / 100
    print("O resultado é:", resultado)

else:
    print("ERRO DE SINTAXE")
