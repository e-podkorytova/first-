#Stwórz program, który wypisze liczby od 1 do n rosnąco. 
print("hejka!! jest to program, ktory wypisze liczby od 1 do n)")
try:
    n=int(input("podaj prosze liczbe do ktorej chcesz zebys wypisalam elementy "))
except ValueError:
    print("nie jest to liczba")
    exit()
i = 1
while i<=n:
    print(i)
    i += 1
print(f"")