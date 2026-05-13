pesoC = int(input("Insira o peso do caminhão \n"))

if pesoC < 10:
    print("Carga leve")

elif 10 < pesoC < 25:
    print("Carga Padrão")

elif 25 < pesoC:
    print("ALERTA: Excesso de Peso!")

else:
    print("Carga Inválida")