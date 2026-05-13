print("Loja de Comidas e Doces")
print("Escolha entre:")
print("1 - Comida")
print("2 - Bebida")
print("3 - Doce")
escolha = input("Escolha uma opção \n")

if escolha == "Comida":
    print("Você escolheu uma comida, insira o nome dela e o valor: \n")
    Comida = input("Insira o nome da comida: \n" )
    valorComida = int(input("Insira o valor da comida: \n"))
    desconto = valorComida * 10 / 100
    total = valorComida - desconto
    print("A comida escolhida foi: \n", Comida)
    print("O valor da comida foi: \n", valorComida)
    print("O total com o desconto foi: \n", total)
elif escolha == "Bebida":
    print("Você escolheu uma bebida, insira o nome dela e o valor \n")  
    Bebida = input("Insira o nome da bebida: \n")
    valorBebida = int(input("Insira o valor da bebida: \n"))
    desconto = valorBebida * 5 / 100
    total = valorBebida - desconto
    print("A bebida escolhida foi: \n", Bebida)
    print("O valor da bebida foi: \n", valorBebida)
    print("O total com o desconto foi: \n", total)
elif escolha == "Doce":
    print("Você escolheu um doce, insira o nome dele e o valor \n")  
    Doce = input("Insira o nome do doce: \n")
    valorDoce = int(input("Insira o valor do doce: \n"))
    desconto = valorDoce * 2 / 100
    total = valorDoce - desconto
    print("O doce escolhido foi: \n", Doce)
    print("O valor do doce foi: \n", valorDoce)
    print("O total com o desconto foi: \n", total)



