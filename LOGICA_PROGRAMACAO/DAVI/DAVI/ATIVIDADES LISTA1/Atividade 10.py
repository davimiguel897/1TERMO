print("Qual o nome do produto? \n")
produto = input("PRODUTO: \n")
print("Qual foi a quantidade vendida? \n")
quantidade = float(input("QUANTIDADE: \n"))
print("Qual é o preço do produto? \n")
preço = float(input("PREÇO: \n"))
total = quantidade * preço
print("==========================")
print("Relatório de Vendas")
print("==========================") 
RP = ["Produto:", produto,
      "Quantidade vendida:", quantidade,
      "Preço unitário:", preço,
      "Total de vendas:", total]

for item in RP:
    print(item)
print("==========================")