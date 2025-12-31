#Obliczanie silni iteracyjnie

def silnia_it():
    print("hejkaa!!jest to program liczacy silnie iteracyjniee<3")
    try:
        n=int(input("podaj prosze liczbe do liczenia silni!!"))
    except ValueError:
        print("nie jest to liczba")
    if n<0:
        print("sorki, ale silnie nie da sie obliczyc z liczb ujemnych🤒")
        exit()
    elif n==0:
        print("silnia dla liczby 0 wynosi 1🤯🤯!!")
    else:
        m=1
        for i in range(1, n+1):
            m *= i
            n=n-1
            print(f"Silnia z {n} wynosi {m}🤩")
        return m
print(silnia_it())
