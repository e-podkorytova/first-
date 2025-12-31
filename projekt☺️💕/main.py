import a1
import a2
import a3
import a4
import a5
import a6
import a7
import a8
import a9
import a10
import a11
import a12
import a13
import a14

def main():
    print("Program started!")
    while True:
        print("--- BIBLIOTEKA PROGRAMÓW W PYTHONIE😘 ---")
        print("1 NWW")
        print("2 Sito eratostenesa")
        print("3 Generowanie wyrazów ciągu Fibonacciego iteracyjne")
        print("4 Generowanie wyrazów ciągu Fibonacciego rekurencyjnie")
        print("5 Obliczanie silni iteracyjnie")
        print("6 Obliczanie silni rekurencyjnie")
        print("7 Rozkład na czynniki pierwsze")
        print("8 Zamiana liczby dziesiętnej na binarną")
        print("9 Zamiana liczby binarnej na dziesiętną")
        print("10 Szukanie najmniejszego lub największego elementu w liście")
        print("11 Porównywanie tekstów")
        print("12 Odwracanie kolejności liter w podanym wyrazie")
        print("13 Zliczanie wystąpień podanego znaku w tekście")
        print("14 Szukanie wzorca w tekście")
        print("0 Wyjście z programu")
        try:
            wybor=int(input("Wybierz opcję: "))
        except ValueError:
            print("Podaj poprawny numer!")
            continue
        if wybor == 1:
            a1.NWD()
        elif wybor == 2:
            a2.sito_er()
        elif wybor == 3:
            a3.fib_iteracyjnie()
        elif wybor == 4:
            a4.fib_rekurencyjnie()
        elif wybor == 5:
            a5.silnia_it()
        elif wybor == 6:
            a6.silnia_r()
        elif wybor == 7:
            a7.czynniki_pierwsze()
        elif wybor == 8:
            a8.dw_na_b()
        elif wybor == 9:
            a9.bin_na_dziesietna()
        elif wybor == 10:
            a10.nm_nw_el()
        elif wybor == 11:
            a11.porownanie()
        elif wybor == 12:
            a12.odwracanie_wyrazu()
        elif wybor == 13:
            a13.wystapienie()
        elif wybor == 14:
            a14.szukanie_wzorca()

        elif wybor == 0:      
            print("nic nie wybrales takze komputerek sie wylacza xixii😈😈💥💥")
            break
        else:
            print("Nie ma takiej opcji!")

if __name__ == "__main__":
    main()