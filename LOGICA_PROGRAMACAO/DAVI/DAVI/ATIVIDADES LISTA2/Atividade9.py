pneu = int(input("Insira o PSI do pneu \n"))

if 100 <= pneu <= 110:
    print("O pneu está com a pressão certa")
else:
    print("O pneu está com a pressão incorreta")

print("Validação de Calibragem")
pressao = float(input("Digite a pressão do pneu em PSI:..."))
if 100 <= pressao <= 110:
    print("Dentro do padrão")
elif pressao < 100:
    print("Abaixo do recomendado")
else:
    print("Acima do recomendado")