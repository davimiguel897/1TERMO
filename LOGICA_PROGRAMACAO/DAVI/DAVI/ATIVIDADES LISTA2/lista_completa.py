# Atividade 1

# Modelo = input("Diga o nome do veículo: \n")
# Placa = input("Diga a placa do veículo: \n")

# print(f"Veículo {Modelo} de placa {Placa} registrado no sistema. Boa viagem!")

# Atividade 2

# capacidade = int(input("Insira a capacidade de gasolina do caminhão \n"))
# consumo = int(input("Insira a quantidade de consumo de gasolina do caminhão \n"))
# distancia = capacidade / consumo
# print(f"O caminhão pode percorrer: {distancia:.2f}km/l")

# Atividade 3

# print("Conversor de Real para Dolar")

# real = float(input("Digite o seu dinheiro em real \n"))
# dolar = real * 5
# total = round (dolar,2)

# print(f"A quantidade convertida é {total}")

# Atividade 4

# print("Média de Entrega")

# rota1 = int(input("Tempo da primeira rota em horas: \n"))
# rota2 = int(input("Tempo da segunda rota em horas: \n"))
# rota3 = int(input("Tempo da terceira rota em horas: \n"))

# tempototal = rota1 + rota2 + rota3 / 3
# print(f"A média de tempo de entregas é {tempototal:.2f}")

# Atividade 5

# pesoC = int(input("Insira o peso do caminhão \n"))

# if pesoC < 10:
#     print("Carga leve")

# elif 10 < pesoC < 25:
#     print("Carga Padrão")

# elif 25 < pesoC:
#     print("ALERTA: Excesso de Peso!")

# else:

# Atividade 6

# codigo_carga = input("N ou S \n")

# if codigo_carga == "N":
#     print("Região Norte")

# elif codigo_carga == "S":
#     print("Região Sul")

# else:
#     print("Região Internacional")

# Atividade 7

# print("Checklist de Motorista")
# motorista_identificado = input("O Checklist foi concluído: [sim] ou [não]: \n")
# checklist = "concluído"

# if motorista_identificado == "sim":
#     checklist == "concluído"
#     print("O checklist foi concluído")

# else:
#     print("O checklist é invalido")

# Atividade 8

# EntregasAgendadas = int(input("Inserir quantidade de entregas agendadas \n"))
# EntregasAtrasadas = int(input("Inserir quantidade de entregas atrasadas \n"))
# EntregasTotais = EntregasAgendadas + EntregasAtrasadas
# comparacao = EntregasTotais * 0.1 

# if EntregasAtrasadas > comparacao:
#     print("Necessário Otimizar Rotas")
# else:
#     print("Logística Eficiente")

# Atividade 9

# pneu = int(input("Insira o PSI do pneu \n"))

# if 100 <= pneu <= 110:
#     print("O pneu está com a pressão certa")
# else:
#     print("O pneu está com a pressão incorreta")

# Atividade 10

# import time

# for item in range(5,0, -1):
#     print(f"{item}")
#     time.sleep(1)
#     if item == 1:
#         print("Portão trancado!")

# Atividade 11

# frete = 0
# print("Somador de Fretes, digite o valor para somar, e 0 para parar")
# while True:
#     vf = int(input(f"Insira o valor do frete \n "))
#     frete += vf
#     if vf == 0:
#         break
# print(f"{frete}")

# Atividade 12

# veiculo = [26, 25, 29, 22, 34]

# for km in veiculo:
#     print(f"A quilometragem do veiculo é {km} ")
#     if km >= 30:
#         print(f"O veículo com maior quilometragem é o de {km} ")