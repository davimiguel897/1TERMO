peçasboas = int(input("Insira a quantidade de peças boas:"))
peçasruins = int(input("Insira a quantidade de peças ruins"))
total = peçasboas + peçasruins
taxadeaproveitamento = peçasboas / total

print("O total de peças é:", total)
print("A taxa de aproveitamento é:", round(taxadeaproveitamento), 2)