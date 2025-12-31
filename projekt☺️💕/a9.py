def bin_na_dziesietna():
    print("to program do zamiany liczby binarnej na dziesietna, witam serdecznie<3")
    try:
        n = input("podaj prosze dowolna liczbe binarna😇")
    except ValueError:
        print("sorki, ale nie jest to liczba😔")
    m = int(n, 2)
    print(f"twoja liczba {n} w systemie dziesietnym to: {m}!!")
    
if __name__ == "__main__":
    bin_na_dziesietna()