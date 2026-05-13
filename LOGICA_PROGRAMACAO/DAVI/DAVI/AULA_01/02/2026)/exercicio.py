print("Algoritmo de Perguntas")

print("Qual é o seu nome? \n")
pg1 = input("NOME: \n")
print("Qual é a sua idade? \n")
pg2 = int(input("IDADE: \n"))
print("Qual é o seu curso? \n")
pg3 = input("CURSO: \n")
print("Qual é o seu hoobie? \n")
pg4 = input("HOOBIE: \n")
RP = ["Seu nome:", pg1,
      "Sua idade:", pg2,
      "Seu curso:", pg3,
      "Seu hobbie:", pg4]
print("Suas respostas são:" , RP)

for item in RP:
    print(item)