capacidade = int(input("Insira a capacidade de gasolina do caminhão \n"))
consumo = int(input("Insira a quantidade de consumo de gasolina do caminhão \n"))
distancia = capacidade / consumo
print(f"O caminhão pode percorrer: {distancia:.2f}km/l")