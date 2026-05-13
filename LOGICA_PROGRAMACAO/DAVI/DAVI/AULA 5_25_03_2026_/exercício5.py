for saco in range(1, 7):
    s = float(input("Quanto pesa o saco?"))
    if 48 <= s <= 52:
        print(f"O saco de peso {s} está dentro do limite")
    else:
        print("O saco está fora do limite")