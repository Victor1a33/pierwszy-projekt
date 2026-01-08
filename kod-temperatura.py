temp = input("Podaj temperaturę w Celcjuszach (C) lub w Farenheitach (F): ")
if temp[-1].upper() == "C":
    c = float(temp[:-1])
    f = (9*c + (32 * 5)) / 5
    print("%.0f C po przeliczeniu to %.0f F" %(c,f))
elif temp[-1].upper() == "F":
    f = float(temp[:-1])
    c = (5*(f-32)) / 9
    print("%.0f F po przeliczeniu to %.0f C" %(f,c))
else :
    print("Nieprawidłowy zapis")