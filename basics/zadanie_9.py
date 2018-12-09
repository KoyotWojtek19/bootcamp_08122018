import datetime
dat_urodzenia = int(input("podaj date urodzenia: "))

current_year = datetime.datetime.now().year
if dat_urodzenia + 18 <= current_year:
    print("Jestes Pelnoletni! IDZ SIE NAPIJ")
else:
    print("Spadaj Gowniarzu")


