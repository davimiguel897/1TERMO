# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

# 1.1
# idade = int(input("Digite a sua idade"))
# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")
# # O "input" do código deveria possuir o "int" para identificar apenas números, além de apenas possuir uma consequência caso o usuário for menor de idade

# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# 2.1
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")
# # Por ser uma variável, é necessário que ela fique dentro de chaves({}) no print, e que o comando possua o "f" antes da frase


# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# 3.1
# numero = int(input("Digite o número"))
# if numero >= 5:
#     print("O número é maior que 5")
# else:
#     print("O número é menor ou igual a cinco")
# O código

# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# 4.1
# usuario = input("Digite o nome de usuário \n")
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# else:
#     print("Login incorreto, tente novamente.")

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#5.1
# clima = input("Diga se o clima está ensolarado ou chuvoso")
# if clima == "ensolarado":
#     print("O clima está ensolarado")
# elif clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

#6.1
# pontos = 50
# print("Parabéns, você fez", pontos, "pontos!")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

#7.1
# nota = int(input("Digite a sua nota"))
# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado!")


# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# 8.1
# for item in range(1, 6):
#     print(item)

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

#9.1
# tentativas = 0
# while tentativas <= 3:
#     tentativa = input("Digite a senha")
#     tentativa_correta = "123"
#     if tentativa == tentativa_correta:
#         print("Conectado!")
#         break
#     else:
#         print("Tentando conectar...")
#         tentativas += 1
#         if tentativas >= 3:
#             print("Não conectado.")
#             break
            
    
# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

#10.1
# senha = "python123"
# while True:
#     senha = input("Digite a senha secreta")
#     if senha == "python123":
#         print("Acesso concedido!")
#         break
#     else:
#         print("Acesso negado")
#         continue

