print("---")
print("Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).", "\n", "Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.", "\n", "Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.", "\n", "Затем пользователь вводит сами элементы множеств.")
list_1 = set()
list_2 = set()
n = ""
m = ""
while n.isdigit()==False or m.isdigit()==False :
    n = input("Введите число n, кол-во элементов первого множества: ")
    m = input("Введите число m, кол-во элементов второго множества: ")
print("Элементы первого множества :")   
for i in range (int(n)):
    a=input()
    list_1.add(a)
print("Элементы второго множества :")  
for i in range (int(m)):
    b=input()
    list_2.add(b)
u1 = list(list_1.intersection(list_2))
a = (sorted(u1, reverse=False))
print("Элементы, встречающиеся в обоих наборах без повторений, в порядке возрастания :", *a) 
print("---")      
