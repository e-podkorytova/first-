def NWD():
    print("heja, jest to program liczacy nwd dwóch liczb dodatnich!!")
    try:
        a = int(input("podaj prosze pierwszą liczbę do liczenia nwd"))
        b = int(input("podaj druga liczbę do liczenia nwd"))
    except ValueError:
        print("nie jest to liczba🤧🌚")
        return 
    mini = min(a, b)
    for i in range(mini, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"nwd wynosi {i} xixi🤗🤗")
            return 

if __name__ == "__main__":
    NWD()
