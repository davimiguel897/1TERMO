tab = int(input("Qual tabuada você quer?"))
for numero in range(1, 11):
    resultado = tab * numero 
    print(f"{tab} x {numero} =", resultado )
