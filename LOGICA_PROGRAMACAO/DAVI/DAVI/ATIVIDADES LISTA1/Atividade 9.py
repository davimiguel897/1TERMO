custo_hotel = float(input("Digite o custo do hotel por noite: \n"))
quantidade_noites = int(input("Digite a quantidade de noites \n"))
valor_passagem = float(input("Digite o valor da passagem \n"))
total = custo_hotel * quantidade_noites + valor_passagem
print("O custo total de tudo foi: \n", total)