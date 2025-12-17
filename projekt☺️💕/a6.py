def silnia_r():
        try:
            liczba=int(input("podaj prosze liczbe do obliczania silni "))
        except ValueError:
            print("nie jest to liczba😡")
            return
        if liczba==0:
            print("silnia jest rowna 1")
        elif liczba<0:
            print("niestety silnie sie liczy dla liczb ujemnych kochanie😭😭")
            return
        elif liczba>1:
            silnia_r =1
            i=1
            while i<=liczba:
                silnia *= i
                i += 1
print(f"silnia wynosi {silnia_r}")  

if __name__ == "__main__":
    silnia_r()