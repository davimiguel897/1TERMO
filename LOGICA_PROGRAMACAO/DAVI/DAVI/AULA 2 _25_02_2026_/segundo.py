# def saudacao(nome):
#     return f"Olá, meu nome é {nome}!"

# mensagem = saudacao("Davi")
# print(mensagem)

# def age(idade):
#     return f"Tenho {idade} anos!"
# mensagem = age("16")
# print(mensagem)

# Funções são blocos de código reutilizáveis.
# O "f" no Python, usado antes das aspas de uma string (como f"texto {variável}"), indica que se trata de uma f-string (ou formatted string literal). Ele informa ao Python que a string contém expressões entre chaves {} que devem ser avaliadas em tempo de execução e substituidas pelos seus valores reais.

def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Você é o novo {cargo}.")

boas_vindas("Davi", "Resenhador")

# Conversões
nome = input("Seu nome: ")   
idade = int(input("Sua idade: ")) # Converte texto para inteiro
print(f"{nome} tem {idade} anos.") 

