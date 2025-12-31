def szukanie_wzorca():
    n = input("podaj prosze tekst, w którym chcesz szukać wzorca🙈")
    m = input("podaj wzorzec do znalezienia >@_@> ")
    pozycja = n.find(m)
    if pozycja != -1:
        print(f"wzorzec {m} znaleziono na pozycji {pozycja}!!")
    else:
        print(f"Wzorzec {m} nie zostal znaleziony w tekscie :(")

if __name__ == "__main__":
    szukanie_wzorca()