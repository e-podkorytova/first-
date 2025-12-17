n=int(input("podaj prosze liczbe do dzialania"))
cz=[]
dz=2
while n !=1:
    while n % dz ==0:
        cz.append(dz)
        n //= dz
    dz += 1
print(cz)