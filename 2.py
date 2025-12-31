import time as Talha

print("Python hesap makinesine hoş geldin")
Talha.sleep(1)

while True:
    a = float(input("1. sayıyı gir: "))
    b = float(input("2. sayıyı gir: "))
    isaret = input("İşareti gir (+, -, *, /): ")

    if isaret == "+":
        print(a + b)

    elif isaret == "-":
        print(a - b)

    elif isaret == "*":
        print(a * b)

    elif isaret == "/":
        if b == 0:
            print("0'a mı bölcen yine? Matematik ağlıyor şu an. Tekrar dene.")
            continue  # sor artı
    
        else:
            print(a / b)

    else:
        print("Bu ne biçim işaret? Tekrar dene.")
        continue

    break  # kır
