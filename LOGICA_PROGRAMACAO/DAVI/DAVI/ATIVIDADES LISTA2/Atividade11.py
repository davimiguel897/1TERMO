frete = 0
print("Somador de Fretes, digite o valor para somar, e 0 para parar")
while True:
    vf = int(input(f"Insira o valor do frete \n "))
    frete += vf
    if vf == 0:
        break
print(f"{frete}")