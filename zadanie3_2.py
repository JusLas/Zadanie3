lista_zakupow={
    "warzywaniak": ["cebula","zieminaki", "buraki"],
    "piekarnia":["bułka","chleb","paczek"]
}
for sklep in lista_zakupow:
    print(f"Idę do {sklep.capitalize()}, kupuję tam astępujące rzeczy {[item.capitalize() for item in lista_zakupow[sklep]]}") 

liczba_produktow = 0
for sklep in lista_zakupow:
    liczba_produktow = liczba_produktow + len(lista_zakupow[sklep])   
print(f"W sumie kupuję {liczba_produktow} produktow")

zakupy = lista_zakupow["warzywaniak"]
print(zakupy)