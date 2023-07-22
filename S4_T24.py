print("")
print("Задача 24")
N = c1 = ""
while N.isdigit()==False or c1.isdigit()==False :
    try:
        N = input("Введите количество кустов :")
        c1 = input("Введите номер куста :")        
    except ValueError:
        print("Ошибка ввода. Введите число.")
from random import randint
list_1 = list()
c = int(c1) 
for i in range(int(N)): 
    n = randint(0, 1000) 
    list_1.append(n) 
if c+1 == len(list_1):
    q = list_1[0]
else:
    q = list_1[c+1]
print(list_1[c-1]+list_1[c]+q)
# Проверка rjkbxtcndf zuujl yf recnf[]
# print(list_1)
# print(list_1[c-1],list_1[c] ,q,(list_1[c-1]+list_1[c]+q))
