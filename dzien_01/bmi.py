zmienna = "napis"

dana_1 = input("Podaj wzrost w metrach ")
dana_1 = float(dana_1)
print("Twój wzrost to", dana_1, "m", type(dana_1))

dana_2 = input("Podaj wagę w kilogramach ")
dana_2 = float(dana_2)
print("Twoja waga to", dana_2, "kg", type(dana_2))

dana_3 = (dana_2) / (dana_1**2)
print("Twój BMI wynosi", round (dana_3)) 