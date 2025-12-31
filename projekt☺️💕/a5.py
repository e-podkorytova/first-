def silnia_it():
    try:
        n = int(input("jest to program liczacy silnie iteracyjniee😘🤞!! Podaj prosze liczbe do liczenia silni!!"))
    except ValueError:
        print("to nie jest liczba🤥")
        return None  
    if n < 0:
        print("sorki, ale silnia nie da sie obliczyc z liczb ujemnych🤒")
        return None
    elif n == 0:
        print("silnia dla liczby 0 wynosi 1🤯🤯!!")
        return 1
    else:
        m = 1
        for i in range(1, n + 1):
            m *= i  
        print(f"silnia dla {n} wynosi {m}!")
        return m  

if __name__ == "__main__":
    silnia_it()


