import random

def losowanie():
    return [random.randint(1, 6) for _ in range(5)]

def uklad(oczka):
    oczka = sorted(oczka)

    if oczka == [1,2,3,4,5]:
        return 4, "Mały strit"
    if oczka == [2,3,4,5,6]:
        return 5, "Duży strit"

    a, b, c, d, e = oczka

    if a == b == c == d == e:
        return 8, "Poker"
    if a == b == c == d or b == c == d == e:
        return 7, "Kareta"
    if (a == b == c and d == e) or (a == b and c == d == e):
        return 6, "Full"
    if a == b == c or b == c == d or c == d == e:
        return 3, "Trójka"
    if (a == b and c == d) or (b == c and d == e) or (a == b and d == e):
        return 2, "Dwie pary"
    if a == b or b == c or c == d or d == e:
        return 1, "Para"

    return 0, "Nic"

def rozgrywka():
    czlowiek = losowanie()
    komputer = losowanie()

    wynik_czlowiek, uklad_czlowiek = uklad(czlowiek)
    wynik_komputer, uklad_komputer = uklad(komputer)

    print(f"\nTwój rzut: {czlowiek}")
    print(f"Twój układ: {uklad_czlowiek}")
    print(f"\nRzut komputera:{komputer}")
    print(f"Układ komputera: {uklad_komputer}\n")

    if wynik_czlowiek > wynik_komputer:
        print("Wygrana!")
    elif wynik_czlowiek < wynik_komputer:
        print("Przegrana")
    else:
        print("Remis")
    nowa_gra()

def nowa_gra():
    odp1 = input("\nRozpocząć grę w kości? (tak/nie): ")
    if odp1.lower() == "tak":
        odp2 = input("Wyświetlić mozliwe kombinacje? (tak/nie): ")
        if odp2.lower() == "tak":
            print("Kombinacje:")
            print("1. Nic – pięć nie tworzących żadnego układu oczek. Punkty = 0")
            print("2. Para – dwie kości o tej samej liczbie oczek. Punkty = 1")
            print("3. Dwie Pary – dwie pary kości, o tej samej liczbie oczek. Punkty = 2")
            print("4. Trójka – trzy kości o tej samej liczbie oczek. Punkty = 3")
            print("5. Mały Strit – kości pokazujące wartości od 1 do 5, po kolei. Punkty = 4")
            print("6. Duży Strit – kości pokazujące wartości od 2 do 6, po kolei. Punkty = 5")
            print("7. Full – jedna para i trójka. Punkty = 6")
            print("8. Kareta – cztery kości o tej samej liczbie oczek. Punkty = 7")
            print("9. Poker – pięć kości o tej samej liczbie oczek. Punkty = 8")
            odp3 = input("\nPrzejść do gry? (tak/nie): ")
            if odp3.lower() == "tak":
                rozgrywka()
            else:
                return
        else:
            rozgrywka()
    else:
        print("Koniec gry")

nowa_gra()