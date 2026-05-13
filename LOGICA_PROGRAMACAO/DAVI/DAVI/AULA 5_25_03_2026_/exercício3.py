consumot = 0
for maquina in range(1, 6):
    consumo = float(input("Quantos kWh cada máquina consumiu?"))
    consumot += consumo
print(f"O total de consumo da fábrica foi de {consumot}")