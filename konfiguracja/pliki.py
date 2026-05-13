


file = open("plik.txt")
#to samo co: file = open("plik.txt", "rt")
#to samo co: file = open("plik.txt", "rt", encoding="utf8")

#plik może być ze ścieżką "dane\plik.txt"
#r(read) - otwiera plik tylko do odczytu
#t(text) - otwiera plik w trybie tekstowym

# zawartosc = file.read()
# print(zawartosc)


# print("Czytamy linijka po linijce:")
# wiersz = file.readline()
# while wiersz:
#     print(wiersz.strip())
#     #strip - usuwa białe znaki z początku i końca linii, w tym znak \n przejścia do nowej linii
#     wiersz = file.readline()


# for wiersz in file:
#     print(wiersz.strip())


# file.close()

file = open("plik2.txt", "w")
file.write("Lew ma grzeywe\n")
file.close()

file = open("plik2.txt", "a", encoding="utf8")
file.write("Krzyś ma auto i rower")
file.close()
