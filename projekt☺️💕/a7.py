import math

def czynniki_pierwsze():
    print("hejka, to program do rozkładu liczby na czynniki pierwsze!!")
    try:
        n = int(input("podaj prosze liczbe, ktora chcesz rozlozyc na czynniki"))
    except ValueError:
        print("nie jest to liczba🥸!!")
        return  
    if n <= 0:
        print("podaj liczbe wiekszą niz zero, oki??)")
        return  
    lista = []
    dzielnik = 2
    while dzielnik <= math.sqrt(n):  
        while n % dzielnik == 0:  
            lista.append(dzielnik)
            n //= dzielnik
        dzielnik += 1  
    if n > 1: 
        lista.append(n)
    
    print(f"Oto rozkład na czynniki pierwsze: {lista}!!")

if __name__ == "__main__":
    czynniki_pierwsze()
