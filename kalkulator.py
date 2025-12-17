print("hejkaa!<3")
print("jest to piekny kalkulator ktory wam chce pomoc")
print("mamy do zaoferowanie dodawanie, odejmowanie, mnozenie, dzielenie, dzielenie z reszta i potegowanie")

l1=float(input("podaj pierwsza liczbe do dzialania! "))
l2=float(input("podaj teraz druga liczbe do dzialania! "))
dz=input("jakie dzialanie chcesz wykonac?) ")
if dz=="+":
    wynik=l1+l2
elif dz=="-":
    wynik=l1-l2
elif dz=="*":
    wynik=l1*l2
elif dz=="/":
    if l2==0:
        wynik="dzielenie nie moze byc wykonane"
    elif l2>0:
        wynik=l1/l2
elif dz=="%":
    if l2==0:
        wynik="dzielenie nie moze byc wykonane"
    elif l2>0:
        wynik=l1%l2
elif dz=="**":
    wynik=l1**l2

print("oto masz", wynik)


