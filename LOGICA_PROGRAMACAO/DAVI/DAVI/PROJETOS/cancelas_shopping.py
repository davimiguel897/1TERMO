valorCancela = 0
print("Bem-vindo ao Shopping Center, o valor da tarifa é de R$ 2,00 por hora. Escolha uma das opções!")

opcao = input("Escolha entre: Sem Parar (botão 1), Ticket (botão 2) e Interfone (botão 3)")
Sem_Parar = "1"
Ticket = "2"
Interfone = "3"

if opcao == "1":
    while True:
        Tag = input("Você está com sua Tag do Sem Parar? (Y) se sim, (N) se não")
        Sim = "Y"
        Não = "N"
        if Tag == "Y":
            print("Bem-vindo ao Estacionamento! Sua Tag foi identificada com sucesso!")
            print("Aproveite! \n")
            horasPermanecidas = int(input("Digite a quantidade de horas que o veículo passou estacionado \n"))
            valorCancela = horasPermanecidas * 2
            fichaFinal = [f"Quantidade de Horas Permanecidas: {horasPermanecidas} \n"
                          f"Valor de Estacionamento: {valorCancela} \n"]
            for item in fichaFinal:
                print(item)
            print("O valor foi adicionado à sua mensalidade, volte sempre!")
            break
        elif Tag == "N":
            print("Você não possui uma Tag Sem Parar, escolha a opção de Ticket")
            break


elif opcao == "2":
    while True:
        print("Bem-vindo ao Estacionamento! Para cada hora: R$ 2,00. Pressione o botão na Cancela para adquirir seu Ticket!")
        nomeCliente = input("Digite o seu nome: \n")
        veiculoCliente = input("Digite o modelo do veículo: \n")
        print("Por favor, retire o seu Ticket e aproveite!")
        horasPermanecidas = int(input("Digite a quantidade de horas que o veículo passou estacionado \n"))
        valorCancela = horasPermanecidas * 2
        fichaFinal = [f"Nome: {nomeCliente} \n"
                      f"Veículo: {veiculoCliente} \n"
                      f"Quantidade de Horas Permanecidas: {horasPermanecidas} \n"
                      f"Valor de Estacionamento: {valorCancela} \n"]
        for item in fichaFinal:
            print(item)
        print("Volte sempre!")
        break

elif opcao == "3":
    while True:
        print("Boa tarde, senhor(a), a cancela apresentou instabilidade na leitura do ticket. Por gentileza, aproxime o veículo e aguarde um instante enquanto realizo a liberação manual.")
        nomeCliente = input("Poderia me dizer o seu nome, por favor?")
        veiculoCliente = input("Poderia me dizer qual é o seu veículo, por favor? \n")
        print("Pronto, senhor(a), o seu ticket está liberado, aproveite sua estadia e perdoe-nos pelo inconveniente!")
        horasPermanecidas = int(input("Digite a quantidade de horas que o veículo passou estacionado \n"))
        valorCancela = horasPermanecidas * 2
        fichaFinal = [f"Nome: {nomeCliente} \n"
                      f"Veículo: {veiculoCliente} \n"
                      f"Quantidade de Horas Permanecidas: {horasPermanecidas} \n"
                      f"Valor de Estacionamento: {valorCancela} \n"]
        for item in fichaFinal:
            print(item)
        print("Volte sempre!")
        break