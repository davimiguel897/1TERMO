# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

import time


andar_destino = int(input("Digite o andar de destino (0-10): "))
andar_elevador = 0
total_pessoas = 0

while andar_elevador < andar_destino:
    try:
        
        quantidade_pessoas = int(input("\nQuantas pessoas estão entrando no elevador? "))
        if total_pessoas + quantidade_pessoas > 5:
            print("O elevador vai passar da capacidade máxima de 5 pessoas. Aguardem o próximo.")
            continue
        else:
            total_pessoas += quantidade_pessoas
            print(f"O número total de pessoas no elevador é: {total_pessoas}")
        if total_pessoas == 5:
            print("Elevador lotado! Aguardem o próximo.")
            break


        andar_elevador = int(input("\nDiga o próximo andar que o elevador irá subir ou descer "))
        if andar_elevador == 0:
            print("O elevador está no térreo.")
        elif andar_elevador > 0:
            print(f"O elevador está indo para o andar {andar_elevador}.")
            time.sleep(1)
        elif andar_elevador > 10:
            print("O elevador não pode subir acima do 10º andar.")
            time.sleep(1)

        if andar_elevador < andar_destino:
            print(f"O elevador está subindo para o andar {andar_destino}.")
            for andar_elevador in range(andar_elevador, andar_destino-1, -1):
                print(f"O elevador está descendo para o andar {andar_destino}.")
                time.sleep(1)
        
        quantidade_pessoas_fora = int(input("\nQuantas pessoas saíram do elevador? "))
        if quantidade_pessoas_fora > total_pessoas:
            print("Número de pessoas saindo do elevador excede o número de pessoas dentro do elevador.")
            break
        else:
            total_pessoas -= quantidade_pessoas_fora
            print(f"O número de pessoas restantes no elevador é: {total_pessoas}")
        
        if andar_elevador == andar_destino:
            print(f"O elevador chegou ao andar de destino: {andar_destino}.")
            break

    
    
    except ValueError:
        print("Digite um número válido")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        print("Encerrando o programa.")
        break