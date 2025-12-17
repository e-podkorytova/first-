# #liniowa
# import time

# # def lin_search(lst, val):
# #     for i in range(len(lst)):
# #         if lst[i]==val:
# #             return i

# # lst=[1,2,3,4,5,6,7,8,9,10]
# # print(lin_search(lst,9))

# # start =time.time()
# # print(lin_search(lst,9))
# # end = time.time()
# # print(end - start)



# n=int(input("podaj liczbe calkowita kochanko!!  "))
# suma=0
# i=1

# start =time.time()

# while i<=n:
#     suma+=1
#     i+=1
# print(suma)

# end = time.time()
# print(end - start)
import time 

n=int(input("podaj liczbe calkowita kochanko!!  "))
start = time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
end = time.time()
print(end-start)