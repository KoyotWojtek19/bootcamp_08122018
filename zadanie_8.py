wys = int(input("podaj wysokosc: "))
szer = int(input("podaj szerokosc: "))
dlug = int(input("podaj dlugosc: "))
objetosc = wys*szer*dlug
print ("objetosc =", objetosc)
print ("Wieksza od 1000: ", objetosc > 1000)
if objetosc > 1000:
    print ("OBJETOSC WIEKSZA NIZ 1 LITR")
else:
    print ("Objetosc jest mniejsza niz 1 litr")

print("KONIEC")


