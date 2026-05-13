codigo_carga = input("N ou S \n")

if codigo_carga == "N":
    print("Região Norte")

elif codigo_carga == "S":
    print("Região Sul")

else:
    print("Região Internacional")

print("Classificador de Destino")
print("Regiões = N - Região Norte, S - Região Sul, Qualquer Outra - Internacional")
regiao = input("Inserir o código da Região").lower()
if regiao == "N".upper() or regiao == "n".lower():
    print("Região Norte")
elif regiao == "S":
    print("Região Sul")
else:
    print("Região Internacional")