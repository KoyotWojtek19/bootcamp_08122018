x = int(input("Podaj X: "))
y = int(input("Podaj Y: "))
if x < 0 or x > 100 or y < 0 or y >100:
     print ("Jestes poza plansza")
elif x > 90 and y > 90:
     print("Jestes w gornym prawym rogu")
elif x > 90 and y < 10:
     print("jestes w dolnym prawym rogu")
elif x < 10 and y <10:
     print("jestes w dolnym lewym rogu")
elif x <10 and y >90:
     print("jestes w gornym lewym rogu")
elif x < 10:
     print("jestes na lewej krawedzi")
elif x > 90:
     print ("jestes na dolnej krawedzi")
elif y > 90:
     print (" jestes na gornej krawedzi")
else:
     print("jestes w centrum")



