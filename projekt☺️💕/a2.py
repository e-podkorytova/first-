def sito_er():
    print("hejka!! jest to program robiacy sito eratostenesa🥹")
    try:
        n = int(input("ile elementow bedzie zawieralo to sito🤔??"))
    except ValueError:
        print("nie jest to liczba😤😤")
        return None
    if n < 2:
        print("Niestety sito ma zawierac wiecej niż dwa elementy🫣")
        return None 
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False 
    for i in range(2, int(n**0.5) + 1): 
        if sito[i]:
            j = i + i
            while j <= n:
                sito[j] = False
                j += i
    return sito

if __name__ == "__main__":
    sito = sito_er()  
    if sito is not None:
        print(f"oto masz to sito - {sito}!!")
    else:
        print("niestety nie udalo sie to zrobic😔")
