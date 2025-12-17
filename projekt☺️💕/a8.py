def dw_na_b():
    print("hejkaa!! " \
    "jest to program przeliczajacy liczby z systemu dziesietmego na dwojkowy!")
    
    liczba=int(input("podaj prosze liczbe dodatnia calkowita w sysytemie dziesietnym wieksza od zera: "))
    lista=[]
    
    if liczba==0:
        print("jak tak mozna😡😡😡")
        return
    else:
        while liczba>0:
            reszta=liczba%2
            lista.append(reszta)
            liczba=liczba//2
        print(lista)

if __name__ == "__main__":
    dw_na_b()
