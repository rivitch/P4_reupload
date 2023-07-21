print("")
print("Задача 24")

N = int(input("Введите количество кустов :")) 
c = int(input("Введите номер куста :"))-1
from random import randint
list_1 = list() 
for i in range(N): 
    n = randint(0, 1000) 
    list_1.append(n) 
if c+1 == len(list_1):
    q = list_1[0]
else:
    q = list_1[c+1]
print(list_1[c-1]+list_1[c]+q)
# print(list_1)
# print(list_1[c-1],list_1[c] ,q,(list_1[c-1]+list_1[c]+q))