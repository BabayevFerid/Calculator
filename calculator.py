def kalkulyator():
    emeliyyat = input("Əməliyyat növünü seç (+, -, *, /): ")
    a = float(input("Birinci ədədi daxil et: "))
    b = float(input("İkinci ədədi daxil et: "))

    if emeliyyat == '+':
        print(f"Nəticə: {a + b}")
    elif emeliyyat == '-':
        print(f"Nəticə: {a - b}")
    elif emeliyyat == '*':
        print(f"Nəticə: {a * b}")
    elif emeliyyat == '/':
        if b != 0:
            print(f"Nəticə: {a / b}")
        else:
            print("Sıfıra bölmək olmaz!")
    else:
        print("Yanlış əməliyyat seçildi.")

kalkulyator()
