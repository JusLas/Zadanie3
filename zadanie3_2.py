lista_zakupow={
    "warzywaniak": ["cebula","zieminaki", "buraki"],
    "piekarnia":["bułka","chleb","paczek"]
}
for sklep in lista_zakupow:
    print(f"Idę do {sklep.capitalize()}, kupuję tam astępujące rzeczy {[item.capitalize() for item in lista_zakupow[sklep]]}")  