
print("słowniki, definiuje się w klamrach")

dict = {"brand":"Ford", "model":"Mondeo","year":2018, "color":"biały"}
print(dict)

#nie ma indeksow, sa nazwy kluczy
print(dict["model"])

#wartosc ze slownika przy pomocy get()
#get daje furtke bezpieczenstwa w przypadku pomylenia nazwy klucza
print(dict.get("model_auta","nie ma takiego klucza"))


#w słowniku możemy zmienić wartość klucza ale nie sam klucz
dict["year"] = 2023
dict["color"] = "czarny"
print(dict)

#krotka moze byc kluczem:

mapa = {
    (52.2,21.0):"Warszawa",
    (50.0,19.9):"Kraków"
}

print(mapa)
print(mapa[(50.0,19.9)])

#metody
klucze = dict.keys()
print(f"\nKlucze: {klucze}")
print(f"Typ zmiennej klucze: {type(klucze)}")

wartosci = dict.values()
print(f"\nWartosci: {wartosci}")
print(f"Typ zmiennej klucze: {type(wartosci)}")

itemy = dict.items()
print(f"\nItemy: {itemy}")
print(f"Typ zmiennej itemy: {type(itemy)}")
