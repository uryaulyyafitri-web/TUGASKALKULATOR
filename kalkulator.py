bil1 = int(input("bil 1 = "))
opr = input("opr (+ - * / % sin cos tan cosec sec cot) = ")

if opr == "sin":
    if bil1 == 0:
        print("0")
    elif bil1 == 30:
        print("1/2")
    elif bil1 == 45:
        print("√2/2")
    elif bil1 == 60:
        print("√3/2")
    elif bil1 == 90:
        print("1")

elif opr == "cos":
    if bil1 == 0:
        print("1")
    elif bil1 == 30:
        print("√3/2")
    elif bil1 == 45:
        print("√2/2")
    elif bil1 == 60:
        print("1/2")
    elif bil1 == 90:
        print("0")

elif opr == "tan":
    if bil1 == 0:
        print("0")
    elif bil1 == 30:
        print("√3/3")
    elif bil1 == 45:
        print("1")
    elif bil1 == 60:
        print("√3")
    elif bil1 == 90:
        print("Tidak terdefinisi")

elif opr == "cosec":
    if bil1 == 0:
        print("Tidak terdefinisi")
    elif bil1 == 30:
        print("2")
    elif bil1 == 45:
        print("√2")
    elif bil1 == 60:
        print("2√3/3")
    elif bil1 == 90:
        print("1")

elif opr == "sec":
    if bil1 == 0:
        print("1")
    elif bil1 == 30:
        print("2√3/3")
    elif bil1 == 45:
        print("√2")
    elif bil1 == 60:
        print("2")
    elif bil1 == 90:
        print("Tidak terdefinisi")

elif opr == "cot":
    if bil1 == 0:
        print("Tidak terdefinisi")
    elif bil1 == 30:
        print("√3")
    elif bil1 == 45:
        print("1")
    elif bil1 == 60:
        print("√3/3")
    elif bil1 == 90:
        print("0")

else:
    bil2 = int(input("bil 2 = "))

    if opr == "+":
        print(bil1 + bil2)
    elif opr == "-":
        print(bil1 - bil2)
    elif opr == "*":
        print(bil1 * bil2)
    elif opr == "/":
        print(bil1 / bil2)
    elif opr == "%":
        print(bil1 % bil2)
    else:
        print("Error pilih operator")