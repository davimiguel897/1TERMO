# Tratamento de Erros e Exceções

# Exemplo 1
# valor1 = int(input("Digite o primeiro valor. \n"))
# valor2 = int(input("Digite o segundo valor. \n"))
# resultado = valor1 / valor2
# print(f"O resultado da divisão é {resultado}")
# # O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:

# # Exemplo 2
# try:
#     valor1 = int(input("Digite o primeiro valor. \n"))
#     valor2 = int(input("Digite o segundo valor. \n"))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um número inteiro válido")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero")

# # Exemplo 3: Tratamento de múltiplas exceções
# try:
#     valor1 = int(input("Digite o primeiro valor. \n"))
#     valor2 = int(input("Digite o segundo valor. \n"))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Ocorreu um erro: {e}")

# # Exemplo 4: Uso do bloco finally
# try:
#     valor1 = int(input("Digite o primeiro valor. \n"))
#     valor2 = int(input("Digite o segundo valor. \n"))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de valor: Por favor, digite um número inteiro válido. {e} ou Erro: não é possível dividir por zero")
# finally:
#     print("Bloco finally executado")

# Exercício 1

# try:
#     nome_usuario = str(input("Digite o seu nome \n"))
#     print(f"Bem-vindo, {nome_usuario}!")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# Exemplo 5: TypeError
try:
    resultado = "5" + 10
except TypeError as e:
    print(f"Erro de tipo: {e}")