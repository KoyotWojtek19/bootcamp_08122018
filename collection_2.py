i = 0
while i < 10:
    liczba = input("podaj liczbe lub k by zakonczyc")
    if liczba == 'k':
        break
    liczba = int(liczba)
    liczby.append(liczba)
    i += 1

#print("srednia wynosi: ", sum(liczba/len(liczba))

# alternatywne 2
dane = input("podaj liczby, rozdziel je spacjami")
dane = dane.split()
dane2 = []
for d in dane:
    dane2.append(int(d))

#2 inne mozliwosci zamiast for d in
# dane = [int(d) for d in dane]
# dane = map(int,dane)
print (dane)
print (dane2)