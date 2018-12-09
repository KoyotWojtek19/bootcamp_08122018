from random import randint
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

min_1_krokow_po_wyl = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
liczb_krokow = 0
DEBUG = False
while True:
    min+1_krokow_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    print(f"twoja pozycja to: {gracz_x}, {gracz_y}")
    print(f"pozycja skarbu to: {skarb_x}, {skarb_y}")
    if DEBUG:
        print(f"pozycja skarbu to: {skarb_x}, {skarb_y}")
    kierunek = input("podaj kierunek w-gora, s-dol, a-lewo, d-prawo")
    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1

    liczba_krokow += 1
    min_1_krokow_po_ruchu = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)

    if gracz_x < 1 or gracz_y < 1 or gracz_x > 10 or gracz_y > 10:
        print("wyszedles poza plansze. koniec gry")

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("wygrales!!")
        print(f"minimalna liczka krokow po wylosowaniu wynosila: {min_1_krokow_po_wyl}")
        print(f"zrobiles krokow: {liczb_krokow}")
        break

    if min_1_krokow_po_ruchu < min_krokow_przed_ruchem:
        print("cieplo")
    else:
        print("zimno")

    if liczb_krokow >= min_1_krokow_po_wyl * 2:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        min_1_krokow_po_wyl = abs(ska)

