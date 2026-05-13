# # 1. O Laço 'for' (Repetições Determinadas)
# # Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
# # Exemplo: Relatório de Produção Diária
# # Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# # Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# # Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# # Exemplo 3
# # Imagine o seguinte cenário, iremos produzir 20 discos de vinil
# for vinil in range (1,21):
#     print(f"Produção de {vinil}, diária")

# # Exemplo 4
# pecas = [ "Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda", "Alicate"]
# itempecas = ["Cilindrica", "Duplo", "Cônica", "Prego", "Orelha", "Redondo", "Phillips", "Universal"]

# for item in pecas:
#     print(f"Item em estoque: {item}")

# Exemplo 5
# Comida = ["Strogonoff", "Feijoada", "Baião de Dois", "Escondidinho", "Macarronada", "Fritas", "Barca de Carnes"]
# Bebida = ["Coca Cola", "Pepsi", "Sprite", "Água", "Água com Gás" "Tubaina", "Água Tônica"]

# print("Menu")
# print("Escolha uma das opções")
# print("Comida ou Bebiba?")

# escolha = input("Digite uma opção \n")

# if escolha == "Comida":
#     print("Cardápio de Comidas:")
#     for item in Comida:
#         print(f"{item}")

# elif escolha == "Bebida":
#     print("Cardápio de Bebidas:")
#     for item in Bebida:
#         print(f"{item}")

# else:
#     print("Adeus")