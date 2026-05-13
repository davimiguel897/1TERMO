print("Cálculo de Notas - Senai (2.0)")
print("Somativas do primeiro semestre")
somativa1 = float(input("Nota da primeira Somativa: \n"))
somativa2 = float(input("Nota da segunda Somativa: \n"))
notafinal = (somativa1+somativa2)/2

if notafinal >= 50:
    print(notafinal, "APROVADO")
else:
    print(notafinal, "REPROVADO")

