def silnia_r():
    n = int(input("podaj liczbe całkowita do licznia silni prosze^^"))  
    print(f"silnia dla {n} wynosi {rekurencja(n)} xixi!!!")
def rekurencja(n):
    if n > 1:
        return n * rekurencja(n - 1)  
    else:
        return 1 

if __name__ == "__main__":
    silnia_r()



