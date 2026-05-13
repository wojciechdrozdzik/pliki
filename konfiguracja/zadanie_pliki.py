
#parametry do zapisu
separator_csv = ","
file_in = "dane.csv"
file_out = "obliczenia_pojazdow.csv"


file = open (file_in, "rt", encoding="utf8")
next(file)  #przeskakuje nagłówek

zestawienie = {}  #unikatowe marki i obliczenia

for wiersz in file:


    wiersz = wiersz.strip().split(";")
    print(wiersz)

    marka = wiersz[1]
    cena = float(wiersz[2])
    przebieg = float(wiersz[8])

    if marka not in zestawienie:
        zestawienie[marka] = [cena, przebieg, 1]
    else:
        zestawienie[marka][0] += cena
        zestawienie[marka][1] += przebieg
        zestawienie[marka][2] += 1

    #print(f"{marka} cena: {cena} przebieg: {przebieg}")
    # print(wiersz)

file.close()

for i in zestawienie.keys():
    zestawienie[i][0] /= zestawienie[i][2]
    zestawienie[i][1] /= zestawienie[i][2]
    print(f"Marka {i}, średnia cena {zestawienie[i][0]:,.0f} zł, średni przebieg: {zestawienie[i][1]:,.0f} km")



print(3 * "*\n")
naglowki_list = ['LP', 'Marka', 'Srednia cena', 'Sredni przebieg', 'Ilosc pojazdow']
naglowki_tekst = separator_csv.join(naglowki_list)

zapis = []
zapis.append(naglowki_tekst)

lp = 1
for marka, dane in zestawienie.items():
    ceny = str(round(dane[0],2))
    przebieg = str(round(dane[1],2))
    ile = str(dane[2])

    pomocnicza_list = [str(lp), marka, ceny, przebieg, ile]
    pomocniczy_tekst = separator_csv.join(pomocnicza_list)


    zapis.append(pomocniczy_tekst)
    lp += 1

do_zapisu = '\n'.join(zapis)
print(do_zapisu)

file = open(file_out,"w",encoding="utf8")

file.write(do_zapisu)

file.close()