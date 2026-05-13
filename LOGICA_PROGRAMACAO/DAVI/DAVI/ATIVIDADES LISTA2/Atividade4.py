print("Média de Entrega")

rota1 = int(input("Tempo da primeira rota em horas: \n"))
rota2 = int(input("Tempo da segunda rota em horas: \n"))
rota3 = int(input("Tempo da terceira rota em horas: \n"))

tempototal = rota1 + rota2 + rota3 / 3
print(f"A média de tempo de entregas é {tempototal:.2f}")
