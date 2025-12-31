def fib_iteracyjnie(): 
    a, b = 0, 1 
    lista = [] 
    print("hejka!! tu mozesz przeliczyc ciag fibonacciego^^") 
    try: 
        n = int(input("ile elementow bedzie zawieral twoj ciag🤔? ")) 
    except ValueError: 
        print("nie jest to liczba😭😭😭") 
        return [] 
    if n <= 0: 
        print("lista nie moze sie skladac z ujemnych elementow/zera sorkii😓") 
        return [] 
    if n>0:
        for _ in range(n): 
            lista.append(a) 
            a, b = b, a + b 
        print(f"no to masz swoja liste - {lista} 🤗") 
        return lista

        
if __name__ == "__main__": 
    fib_iteracyjnie()

