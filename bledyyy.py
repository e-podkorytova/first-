#syntax eroor = cos zle troche napisalam
#ZeroDivision rerror = nie da sie zrobic
#logiczny blad

try:
    x=int(input("podaj liczbe "))
    print(10/x)
except ZeroDivisionError:
    print("Nie mozna dzielic przez 0 debilu!!")
except ValueError:
    print("nie jest to liczba")