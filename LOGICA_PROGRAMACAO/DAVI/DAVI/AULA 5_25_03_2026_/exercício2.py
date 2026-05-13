cores = ["Verde", "Amarelo", "Vermelho"]

import time

for cor in cores:
    if cor == "Amarelo":
        print(f"A cor {cor} está com defeito!")
        continue
    print(f"A cor está {cor}, aguarde 5 segundos")
    time.sleep(5)


