peca = 0

while peca < 5:
    temp = int(input(f"Peça {peca + 1} - Digite a temperatura atual em Celsius: \n"))
    if temp < 0:
        print("ERRO DE LEITURA NO SENSOR")
        continue
    if temp > 150:
        print("ALERTA DE EXPLOSÃO")
        break
    print(f"Temperatura {temp} registrada com sucesso")
    peca += 1
print("Operação finalizada")