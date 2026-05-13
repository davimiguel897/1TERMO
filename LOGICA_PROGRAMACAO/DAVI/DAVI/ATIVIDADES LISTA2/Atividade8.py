EntregasAgendadas = int(input("Inserir quantidade de entregas agendadas \n"))
EntregasAtrasadas = int(input("Inserir quantidade de entregas atrasadas \n"))
EntregasTotais = EntregasAgendadas + EntregasAtrasadas
comparacao = EntregasTotais * 0.1 

if EntregasAtrasadas > comparacao:
    print("Necessário Otimizar Rotas")
else:
    print("Logística Eficiente")


print("Cálculo de Atrasos")
total_entregas = int(input("Total de Entregas Agendadas:..."))
total_atrasos = int(input("Total de Entregas em Atrasos:..."))
if total_atrasos > total_entregas * 0.1:
    print("Necessário otimizar rotas")
else:
    print("Logística Eficiente")