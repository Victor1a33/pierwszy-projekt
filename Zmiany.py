lista1 = []
lista2 = []
wybor = input("Wpisz dowolne słowo: ")
samogloski_lista = [ 'a' , 'ą', 'e', 'ę', 'i', 'o', 'u' 'ó', 'y']
liczba_samoglosek = 0
liczba_spolglosek = 0
for litera in wybor.lower():
    if litera.isalpha():
        if litera in samogloski_lista:
            liczba_samoglosek += 1
        else:
            liczba_spolglosek += 1

print("Liczba samogłosek: ", liczba_samoglosek)
print("Liczba spółgłosek: ", liczba_spolglosek)
print("Jakakolwiek zmiana")