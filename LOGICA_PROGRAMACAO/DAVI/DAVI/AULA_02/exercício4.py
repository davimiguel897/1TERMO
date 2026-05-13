print("Livraria")

print("Insira o Nome do Livro: \n")
pg1 = input("NOME: \n")
print("Insira a Quantidade Comprada do Livro: \n")
pg2 = float(input("QUANTIDADE: \n"))
print("Insira o Valor do Livro: \n")
pg3 = float(input("Valor: \n"))
print("Insira o Desconto Aplicado: \n")
pg4 = float(input("DESCONTO: \n"))
pg5 = (pg2*pg3)
pg6 = pg5*pg4 / 100
pg7 = pg5-pg6
print("\n Relatório de Compra:")
RP = ["NOME:", pg1,
      "QUANTIDADE:", pg2,
      "VALOR:", pg3,
      "DESCONTO:", pg4,
      "VALOR SEM DESCONTO:", pg5,
      "VALOR COM DESCONTO:", pg7,]
for item in RP:
    print(item)