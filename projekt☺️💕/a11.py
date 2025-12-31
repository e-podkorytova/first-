def porownanie():
    print("hejka, porownamy dwa teksty🥰")
    tekst1 = input("podaj pierwszy tekst prosze")
    tekst2 = input("podaj drugi tekst prosze")
    if tekst1 == tekst2:
        print("sa identyczne, gratulacje💖!!")
    else:
        print("teksty sie roznia🤥")
    if tekst1 > tekst2:
        print(f" i pierwszy tekst {tekst1} jest wiekszy niz drugi, xixi))")
    elif tekst1 < tekst2:
        print(f" i pierwszy tekst {tekst1} jest mniejszy niż drugi :((")

if __name__ == "__main__":
    porownanie()