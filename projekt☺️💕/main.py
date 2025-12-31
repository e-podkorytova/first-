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
    print("program sie zaczyna xixi🤗🤗")
    while True:
        print("~~~ 🌸biblioteka programow w pythonie🌸 ~~~")
        print("1 ~ nwd🌸")
        print("2 ~ sito eratostenesa🌸")
        print("3 ~ generowanie wyrazow ciagu fibonacciego iteracyjne🌸")
        print("4 ~ generowanie wyrazow ciagu fibonacciego rekurencyjnie🌸")
        print("5 ~ obliczanie silni iteracyjnie🌸")
        print("6 ~ obliczanie silni rekurencyjnie🌸")
        print("7 ~ rozklad na czynniki pierwsze🌸")
        print("8 ~ zamiana liczby dziesietnej na binarna🌸")
        print("9 ~ zamiana liczby binarnej na dziesiętna🌸")
        print("10 ~ szukanie najmniejszego lub najwiekszego elementu w liscie🌸")
        print("11 ~ porownywanie tekstow🌸")
        print("12 ~ odwracanie kolejnosci liter w podanym wyrazie🌸")
        print("13 ~ zliczanie wystapien podanego znaku w tekscie🌸")
        print("14 ~ szukanie wzorca w tekscie🌸")
        print("0 ~ wyjście z programu🌸")
        try:
            wybor=int(input("Wybierz opcję: "))
        except ValueError:
            print("podaj poprawny numer proszee🤧")
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
            print("nie ma takiej opcji, przepraszam🥺")

if __name__ == "__main__":
    main()