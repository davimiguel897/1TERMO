import time

for item in range(5,0, -1):
    print(f"{item}")
    time.sleep(1)
    if item == 1:
        print("Portão trancado!")

