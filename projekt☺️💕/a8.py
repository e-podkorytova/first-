def dw_na_b():
    lista = []
    print("hejkaa!! jest to program przeliczajacy liczby z systemu dziesietnego na dwojkowy🥳!")
    try:
        liczba = int(input("podaj prosze liczbe dodatnia calkowita w sysytemie dziesietnym wieksza od zera: "))
    except ValueError:
        print("nie jest to liczba")
        exit()
    if liczba<=0:
        print("jak tak mozna😡😡😡, przeciez mowilam!!")
        return
    elif liczba>0:
        while liczba > 0:
            reszta = liczba % 2
            lista.append(reszta)
            liczba = liczba // 2
        
        lista.reverse()  
        print(f"xixi, tu masz twoja liczbe - {lista}")

if __name__ == "__main__":
    dw_na_b()