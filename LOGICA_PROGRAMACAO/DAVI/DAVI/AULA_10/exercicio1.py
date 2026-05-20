try:
    primeiro_numero = float(input("Digite o primeiro valor"))
    segundo_numero = float(input("Digite o segundo valor"))
    terceiro_numero = float(input("Digite o terceiro valor"))
    media = primeiro_numero + segundo_numero + terceiro_numero / 3

except ValueError:
    print("Erro: Digite um valor válido")

except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero.")