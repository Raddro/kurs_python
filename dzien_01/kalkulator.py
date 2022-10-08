pierwsza_liczba = int(input("podaj pierwszą liczbę: "))
druga_liczba = int(input("podaj drugą liczbę: "))
rodzaj_operacji = input("podaj rodzaj operacji: " )
if rodzaj_operacji == "+":
    result = pierwsza_liczba + druga_liczba
elif rodzaj_operacji == "-":
    result = pierwsza_liczba - druga_liczba
elif rodzaj_operacji == "*":
    result = pierwsza_liczba * druga_liczba
elif rodzaj_operacji == "/":
    if druga_liczba == 0:
        result = "dzielone przez zero"
    else:
        result = pierwsza_liczba / druga_liczba
elif rodzaj_operacji == "**":
    result = pierwsza_liczba ** druga_liczba
    
print(f"wynik to: (result)")
