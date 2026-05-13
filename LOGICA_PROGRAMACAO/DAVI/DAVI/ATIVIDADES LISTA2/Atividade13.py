codigo_correto = "track99"
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    codigo_input = input("Código de acesso para o rastreador: :")
    if codigo_input == codigo_correto:
        print("Acesso permitido. Inicianto rastreamento...")
        break
    else:
        tentativas += 1
        print("Acesso negado")
        if tentativas < max_tentativas:
            print(f"Tentativas restantes: {max_tentativas-tentativas}")
else:
    print("Rastreamento bloqueado")
