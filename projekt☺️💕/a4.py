def fib_rekurencyjnie():
    print("hejka!! tu mozesz przeliczyc ciag fibonacciego^^") 
    try: 
        n = int(input("ile elementow bedzie zawieral twoj ciag🤔? "))
    except ValueError: 
        print("nie jest to liczba😭😭😭") 
        return [] 
    print((f"no to masz swoja liste - {fib(n)} 🤗") )  

def fib(n):
    if n <= 1:
        return n  
    else:
        return fib(n - 1) + fib(n - 2)  
