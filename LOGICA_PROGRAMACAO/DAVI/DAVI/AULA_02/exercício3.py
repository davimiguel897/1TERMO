print("Mercado do Senai")

print("Insira o Nome do Produto: \n")
pg1 = input("NOME: \n")
print("Insira a Quantidade Comprada do Produto: \n")
pg2 = float(input("QUANTIDADE: \n"))
print("Insira o Valor do Produto: \n")
pg3 = float(input("Valor: \n"))
pg4 = (pg2*pg3)
RP = ["NOME:", pg1,
      "QUANTIDADE:", pg2,
      "VALOR:", pg3,
      "PREÇO TOTAL:", pg4]
print("\n Relatório de Compra:")
for item in RP:
    print(item)