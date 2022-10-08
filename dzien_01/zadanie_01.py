produkt_1 = "pomidory"
waga_1 = 10
cena_1 = 12.5

produkt_2 = "jablka"
waga_2 = 2
cena_2 = 9.90

produkt_3 = "kasza"
waga_3 = 1
cena_3 = 8.50

suma= cena_1 + cena_2 + cena_3

raport = f"""
{produkt_1:30} {waga_1:5.2f} kg {cena_1:5.2f} PLN
{produkt_2:30} {waga_2:5.2f} kg {cena_2:5.2f} PLN
{produkt_3:30} {waga_3:5.2f} kg {cena_3:5.2f} PLN
{"-"*50}
{"suma:":30} {"":8} {suma:5.2f} PLN
"""

print(raport)
