# Exercício em CleanCode

def registrar_veiculo():
    """Coordena o fluxo de registro de um veículo."""
    modelo, placa = coletar_dados_veiculo()
    exibir_confirmacao_registro(modelo, placa)

def coletar_dados_veiculo():
    modelo = input("Digite o modelo do veículo: ")
    placa = input("Digite a placa do veículo: ")
    return modelo, placa

def exibir_confirmacao_registro(modelo, placa):
    print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

if __name__ == "__main__":
    registrar_veiculo()