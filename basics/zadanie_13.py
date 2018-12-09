ILE_DNI = 7

temp = 0
i = 0
while i <= ILE_DNI:
    temp_i = float(input(f"Podaj temperature w dniu {i}"))
    temp += temp_i
    i += 1

print("Srednia temp wynosila: ", temp/ILE_DNI)