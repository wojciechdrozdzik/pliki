from tkinter import messagebox


firmy = {}
firmy["Nazwa firmy"] = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
firmy["Kurs akcji wczoraj"] = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
firmy["Kurs akcji dzisiaj"] = [ 16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11  ]
firmy["Wzrost/Spadek"]=[None,None,None,None,None,None,None]
firmy["Wartosci"]=[None,None,None,None,None,None,None]

firmy["Nazwa firmy"].append("Polskie Browary")
firmy["Kurs akcji wczoraj"].append(103.20)
firmy["Kurs akcji dzisiaj"].append(101.73)
firmy["Wzrost/Spadek"].append(None)
firmy["Wartosci"].append(None)

ile_firm = len(firmy["Nazwa firmy"])
print(f"Ilość firm: {ile_firm}")

for i in range(ile_firm):
    firmy["Wartosci"][i]=round(firmy["Kurs akcji dzisiaj"][i]-firmy["Kurs akcji wczoraj"][i],2)
    if firmy["Kurs akcji dzisiaj"][i] > firmy["Kurs akcji wczoraj"][i]:
        firmy["Wzrost/Spadek"][i]="wzrósł"
    else:
        firmy["Wzrost/Spadek"][i]="spadł"

for klucz, wartosc in firmy.items():
    print(f"Klucz {klucz}, wartość: {wartosc}")

komunikat_lista = []
for i in range(ile_firm):
    komunikat_lista.append(f"Firma: {firmy["Nazwa firmy"][i]}, kurs od wczoraj {firmy["Wzrost/Spadek"][i]} o {firmy["Wartosci"][i]:.2f}\n")
    #print(komunikat_lista[-1])



messagebox.showinfo("Wiadomości z giełdy", "".join(komunikat_lista))
