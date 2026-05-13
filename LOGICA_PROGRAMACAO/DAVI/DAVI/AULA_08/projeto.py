valorCancela = 0

opcao = input("Escolha entre: Sem Parar (botão 1) e Ticket (botão 2)")
Sem_Parar = "1"
Ticket = "2"

if opcao == "1":
    while True:
        Tag = input("Você está com sua Tag do Sem Parar? (Y) se sim, (N) se não")
        Sim = "Y"
        Não = "N"
        if Tag == "Y":
            print("Bem-vindo ao Estacionamento! Sua Tag foi identificada com sucesso!")
            nome = input("Digite o seu nome: \n")
            veiculo = input("Digite o modelo do veículo: \n")
            print("Aproveite! \n")
            horas = int(input("Digite a quantidade de horas que o veículo passou estacionado \n"))
            valorCancela = horas * 2
            fichaFinal = [f"Nome: {nome} \n"
                          f"Veículo: {veiculo} \n"
                          f"Quantidade de Horas: {horas} \n"
                          f"Valor de Estacionamento: {valorCancela} \n"]
            for item in fichaFinal:
                print(item)
            print("O valor foi adicionado à sua mensalidade, volte sempre!")
        elif Tag == "2":
            print("Você não possui uma Tag Sem Parar, escolha a opção de Ticket")


elif opcao == "2":
    while True:
        print("Bem-vindo ao Estacionamento! Para cada hora: R$ 2,00. Pressione o botão na Cancela para adquirir seu Ticket!")
        nome = input("Digite o seu nome: \n")
        veiculo = input("Digite o modelo do veículo: \n")
        print("Por favor, retire o seu Ticket e aproveite!")
        horas = int(input("Digite a quantidade de horas que o veículo passou estacionado \n"))
        valorCancela = horas * 2
        fichaFinal = [f"Nome: {nome}"
                      f"Veículo: {veiculo} \n"
                      f"Quantidade de Horas: {horas} \n"
                      f"Valor de Estacionamento: {valorCancela} \n"]
        for item in fichaFinal:
            print(item)
        print("Volte sempre!")
