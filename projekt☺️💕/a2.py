def sito_er(n):
    if n < 2:
        return []

    sito=[True]*(n+1)
    sito[0]=sito[1]=False

    for i in range(2, n+1):
        if sito[i]:
            j=i+i
            while j<=n:
                sito[j]=False
                j+=i
    return sito
if __name__ == "__main__":
    sito=sito_er(30)
print(sito)