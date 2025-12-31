def nm_nw_el():
    print("hejka!! ten piekny program poda ci jaka wartosc z listy jest najwieksza, a jaka najmniejsza^^")
    nml = input("podaj prosze liczby oddzielone przecinkami, oki🥺🥺??")
    lista = [int(x.strip()) for x in nml.split(',')]
    n = min(lista)
    m = max(lista)
    print(f"najmniejszy element w liscie to {n}, natomiast najwiekszy to {m}🥰")

if __name__ == "__main__":
    nm_nw_el()