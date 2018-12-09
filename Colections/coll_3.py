lista = [100, -120, -14, -160, 2, 99, 11, 91, -81, 22, 0]

licznik_dodatnich = 0
licznik_ujemnych = 0

for liczba in lista:
    if liczba > 0:
        licznik_dodatnich += 1
    elif liczba < 0:
        licznik_ujemnych += 1

#licznik_dodatnich = len({x for x in lista if x > 0})
#licznik_ujemnych = len({x for x in lista if x<  0})
print(f"liczba dodatnich: {licznik_dodatnich}, liczb ujemnych {licznik_ujemnych}")