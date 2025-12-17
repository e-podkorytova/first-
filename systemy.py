print("hejkaa kochanie, dzisiaj bedziemy przeliczac z systemu dwojkowego na dziesietny!!")
print("DISCLAIMER!! dziala tylko ten program na 5ciocyfrowe liczby")
m= int(input("powiedz ile dziesiatek tysiecy zawiera podana przez ciebie liczba: "))
n= int(input("powiedz ile jednosci tysiecy zawiera podana przez ciebie liczba: "))
l= int(input("powiedz ile setek zawiera podana przez ciebie liczba: "))
k= int(input("powiedz ile dziesiatek zawiera podana przez ciebie liczba: "))
o= int(input("powiedz ile jednosci zawiera podana przez ciebie liczba: "))
liczba=o*1+k*4+l*8+(n*16)+m*32
print("twoj wynik to", liczba)