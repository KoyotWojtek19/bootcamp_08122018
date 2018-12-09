znalezione_maksimum = None
znalezione_minimum = None
liczba = None

while True:
    komenda = input("podaj liczbe lub k by zakonczyc: ")
    if komenda == 'k':
        break
    if len(komenda) > 0 and komenda[0] == '-' and komenda [1:].isdigit ():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("nie podales liczby")
    if liczba or liczba == 0:
        if znalezione_maksimum is None or liczba > znalezione_maksimum:
            znalezione_maksimum = liczba
        if znalezione_minimum is None or liczba < znalezione_minimum:
            znalezione_minimum = liczba

print("znalezione maksimum to: ", znalezione_maksimum)
print("znalezione minimum to: ", znalezione_minimum)



