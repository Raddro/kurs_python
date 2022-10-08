

actual_year = 2022
rok_urodzenia = int(input("rok urodzenia:"))
wiek = actual_year - rok_urodzenia
if wiek >= 18:
    print("pelnoletni")
 elif wiek < 18:
    print("niepelnoletni")