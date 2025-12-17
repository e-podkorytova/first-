try:
    liczba=int(input("podaj prosze liczbe do obliczania silni "))
except ValueError:
    print("nie jest to liczba")
    exit()
if liczba==0:
    print("silnia jest rowna 1")
elif liczba<0:
    print("niestety silnie sie liczy dla liczb ujemnych()")
    exit()
elif liczba>1:
    silnia =1
    i=1
    while i<=liczba:
        silnia *= i
        i += 1
print(f"silnia wynosi {silnia}")    
