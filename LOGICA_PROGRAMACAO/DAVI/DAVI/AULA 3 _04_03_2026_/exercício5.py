print("Cálculo de Viagens")
print("Escolhe entre viagem de")
print("1 - Carro")
print("2 - Ônibus")
print("3 - Avião")
viagem = input("Escolher tipo de viagem: \n")

if viagem == "1":
    valorPedagio = float(input("Insira o valor do pedágio \n" ))
    qtddePedagio = int(input("Insira a quantidade de pedágios \n"))
    valorLGas = float(input("Insira o valor do litro de gasolina \n"))
    qtddeGas = int(input("Insira a quantidade de litros preenchidos \n"))
    totalPedagio = qtddePedagio * valorPedagio
    totalGas = valorLGas * qtddeGas
    total = totalGas +  totalPedagio
    print("O valor total da viagem foi: \n", total)

elif viagem == "2":
    valorPassagem = float(input("Insira o valor da passagem \n"))
    valorSeguro = 3.88
    total = valorPassagem + valorSeguro
    print("O valor total da viagem foi: \n", total)

elif viagem == "3":
    valorViagem = float(input("Insira o valor da viagem: \n"))
    valorTaxa = 55.20
    total = valorViagem + valorTaxa
    print("O valor total da viagem foi: \n", total)

else:
    print("Viagem não identificada")
