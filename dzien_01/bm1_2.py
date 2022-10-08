# Program do obliczania współczynnika BMI

"""
Program do obliczania współczynnika BMI
"""

wzrost = int(input ("podaj zrost ww centymetrach"))/ 100
waga = int(input("Podaj wagę w kg:"))

bmi = waga / (wzrost **2)

print(f"Twój współczynnik BMI wynosi: {bmi:.0f)"))
