x = int(input("podaj x: "))
y = int(input("podaj y: "))
 
if x > 100 or x < 0 or y> 100 or y< 0:
    print("jestes poza plansza")
elif 0 <= x < 10 and 0< y < 10:
    print("LDR")
elif 10 < x < 90 and 0 < y < 10:
    print("LK")
elif 90 < x < 100 and 0 < y < 10:
    print("LGR")
elif 10 < x < 90 and 0 < y <10:
    print = "DK"
elif 10 < 90 and 10 < y < 90:
    print("C")
elif 10 < 90 and 90 < y < 100:
    print("GK")
elif 90 < x < 100 and 0 < y <10:
    print("PDR")
elif 90 < x < 100 and 10 < y <90:
    print("PK")
elif 90 < x < 100 and 90 < y <100:
    print("GPR")

