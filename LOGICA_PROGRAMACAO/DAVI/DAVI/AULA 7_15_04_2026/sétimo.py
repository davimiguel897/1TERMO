# Clean Code - Aula 7
# Para que usar?
# Como usar?
# print("Clean Code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de Clean Code")

# # Manipulação de arquivos e texto
# manipular_texto ="  Python é Muito Legal!  "
# print(manipular_texto.strip().upper()) # "PYTHON"
# print(manipular_texto.strip().lower()) # "python"
# print(manipular_texto.strip().startswith("A")) # "Começar com letra inicial"
# print(manipular_texto.strip().capitalize()) # "Apenas a primeira letra da frase fica maiúscula"
# print(manipular_texto.strip().title()) # Título
# print(manipular_texto.strip().replace(" "," ")) # Preencher vazios
# print(manipular_texto.strip().split()) # "Separar palavras"

# Exercício 1

# manipular_texto = input("Insira o texto a ser manipulado")
# print(manipular_texto.strip().lower())

# Manipular Arquivos:
# escrevendo
# with open("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estamos evoluindo.")

# # Lendo
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# Exercício 2
# print("Contagem de palavras do arquivo")
# with open("exercicio.txt", "w", encoding="utf-8") as texto:
#     texto.write("Python é muito legal!")
#     texto.write("\nPython é bacana!")
#     texto.write("\nEstamos estudando Python!")
#     texto.write("\nPython é vida!!")

# with open("exercicio.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") # Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     print(conteudo)
#     print(f"A palavra Python foi dita {contagem}vezes")

# Interação com o sistema operacional
import os # Importa o módulo os para interagir com o sistema operacional

# Onde estou?
print(os.getcwd())

print(os.listdir())
print(os.listdir("C:/Users"))

# Criar pastas

os.mkdir("Davi")
#Criar arquivos

#Renomear pastas
os.rename("Davi", "Minha_Pasta")

#Apagar pastas
os.rmdir("Minha_Pasta")
os.remove("notas.txt") #Excluir arquivos