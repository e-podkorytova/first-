
def wystapienie():
    n = input("podaj prosze tekst oki?? ")  
    m = input("jaki znak chcesz policzyc??")
    wynik = n.count(m)
    print(f"znak {m} występuje {wynik} razy w podanym tekście(-_-)")

if __name__ == "__main__":
    wystapienie()
