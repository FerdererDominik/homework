#1
# a = int(input("Введите число:"))
# b = int(input("Введите число:"))
# c = int(input("Введите число:"))
# if a > b and a > c:
#     print(f"Наибольшое число:{a}")
# elif b > a and b > c:
#     print(f"Наибольшое число:{b}")
# elif c > a and c > b:
#     print(f"Наибольшое число:{c}")
# else:
#     print(f"Одного наибольшего числа нет")

# 2
# def sm (lst):
#     s = 0
#     for num in lst:
#         s += num
#     print(s)
#     return s
# list_1 = [8, 2, 3, 0, 7]
# sm(list_1)

# 3
# def umn (lst):
#     sm = 1
#     for num in lst:
#         sm *= num
#     print(sm)
#     return sm
# list_1 = [8, 2, 3, -1, 7]
# umn(list_1)

# 4
# a = "1234abcd"
# print(a[::-1])

# 5
# def fact (num):
#     i = 0
#     f = 1
#     while i < num:
#         i += 1
#         f *= i
#     print(f)
#     return f
# a = int(input("Введите число для факториала:"))
# fact(a)

# 6
# def str(z):
#     up = 0
#     low = 0
#     for i in z:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             low += 1
#         else:
#             continue
#     print(f"Кол-во символов верхнего регистра:{up}")
#     print(f"Кол-во символов нижнеего регистра:{low}")
#
# a = input()
# str(a)


# 7
# def plmdr(str):
#     ltr = str[::-1]
#     if str == ltr:
#         print("Это слово является палиндромом")
#     else:
#         print("Это слово не является палиндромом")
# word = input()
# plmdr(word)

#
# 8
# def bank(year, money):
#     i = 0
#     while i < year:
#         i += 1
#         money += money / 10
#     print(money)
#     return money
# y = int(input("Введите кол-во лет:"))
# m = int(input("Введите кол-во денег:"))
# bank(y, m)
#
# # 9
# def dl(lst):
#     for num in lst:
#         if num % 15 == 0:
#             print(num)
#     return num
# list_1 = [45, 55, 60, 37, 105, 220]
# dl(list_1)