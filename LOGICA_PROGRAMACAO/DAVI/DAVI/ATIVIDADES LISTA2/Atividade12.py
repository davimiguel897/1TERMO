veiculo = [26, 25, 29, 22, 34]

for km in veiculo:
    print(f"A quilometragem do veiculo é {km} ")
    if km >= 30:
        print(f"O veículo com maior quilometragem é o de {km} ")

print("Monitoramento de Frota")
maior_km = 0
for frota in range(1, 6):
    km = float(input(f"Digite a quilometragem do veículo {frota}:"))
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada é: {maior_km} km.")