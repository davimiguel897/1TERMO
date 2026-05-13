print("Locadora")

print("Insira o nome do cliente \n")
nome = input("Nome do cliente: \n")

print("Escolha se quer alugar um Filme ou Série: \n")
escolha = input("Escolha: \n")

if escolha == "Filme":
    print("Você escolheu um filme, digite o nome do filme: \n")
elif escolha == "Série":
    print("Você escolheu uma série, digite o nome da série \n")
else:
    print("Cancelar locação")

if escolha == "Filme":
    Filme = input("Digite o nome do Filme \n")
elif escolha == "Série":
    Série = input("Digite o nome da Série \n")
else:
    print("Cancelar locação")

if escolha == "Filme":
    valorFilme = 5
elif escolha == "Série":
    valorSérie = 10

Quantidade = int(input("Qual quantidade você deseja? \n"))

if escolha == "Filme":
    Total = Quantidade * valorFilme
elif escolha == "Série":
    Total = Quantidade * valorSérie
else:
    print("Cancelar locação")

print("Parabéns pela locação \n", nome)

if escolha == "Filme":
    print("O filme que você escolheu foi \n", Filme)
elif escolha == "Série":
    print("A série que você escolheu foi:\n", Série)
else:
    print("Cancelar locação")

print("Quantidade de vezes que pode assistir \n", Quantidade)
print("O valor da locação foi: \n")

if escolha == "Filme":
    print(valorFilme)
elif escolha == "Série":
    print(valorSérie)
else:
    print("Cancelar locação")

print("O total da sua locação foi:", Total)

