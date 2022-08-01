#1
# a = float(input("Введите длинну:"))
# b = float(input("Введите ширину:"))
# s = a * b
# print(f"Площадь комнаты : {s}")

# 2
# a = float(input("Введите уол-во бутылок > 1л:"))
# b = float(input("Введите уол-во бутылок < 1л:"))
# a1 = a * 0.10
# b1 = b * 0.25
# s = a1 + b1
# print(f"Сумма:{s}$")

# 3
# a = float(input("Введите сумму заказа:"))
# pr = a * 0.15
# ch = a * 0.18
# print(f'сумма заказа:{a}, налог:{pr}, чаевые:{ch}')

# 4
# a = int(input("Введите сувениры по 75г:"))
# b = int(input("Введите сувениры по 112г:"))
# a1 = a * 75
# b1 = b * 112
# s = a1 + b1
# print(f"Общий вес посылки: {s}г")

# 5
# f = float(input("Футов в росте:"))
# d = float(input("Дюймов в росте:"))
# sf = f * 30.48
# sd = d * 2.54
# sm = sf + sd
# print(f"Рост равен:{sm}см")

# 6
# a = float(input("Введите расстояние в футах:"))
# d = a * 12
# y = a / 3
# m = a / 5280
# k = a / 3281
# print(f'В дюймах:{d} , в ярдах:{y} , в мидях:{m} , в километрах:{k}')

# 7
# days = int(input('days'))
# hours = int(input('hours:'))
# mins = int(input('mins'))
# secs = int(input('secs'))
# s1 = days * 86400
# s2 = hours * 3600
# s3 = mins * 60
# s4 = s1 + s2 + s3 + secs
# print(f'Секунды в данном промежутке равны:{s4}')

# 8
# c = float(input('Введите градусы по цельсию:'))
# f = (c * 9 / 5) + 32
# k = c + 273,15
# print(f'В кельвинах:{k} , по фарингейту:{f}')

# 9
# bread = 3.49
# sbread = bread * 0.6
# print(f'Цена сегоднешнего хлеба - {bread}$\nЦена вчерашнего хлеба - {sbread}$')
# b = int(input('Кол-во купленого хлеба без скидки:'))
# sb = int(input('Кол-во купленого хлеба со скидкой:'))
# b1 = b * bread
# sb1 = sb * sbread
# s = b1 + sb1
# print(f'Сумма покупки - {s}$')

# 10
# a = int(input('Введите число'))
# if a // 2 != 0:
#     print(f'Это четное число')
# else:
#     print(f'Это не четное число')

# 11
# list_1 = ['a', 'e', 'i', 'o', 'u']
# a = input("Введите букву:")
# if a in list_1:
#     print("Буква гласная")
# elif a == 'y':
#     print("Буква модет быть гласной и согласной")
# else:
#     print("Буква согласная")

# 12
# a = int(input("Введите кол-во углов:"))
# list_1 = ["Треугульник", "Четырехугольник", "Пятиугольник", "Шестиугольник"]
# print(list_1[a-3])

# 13
# while True:
#     command = int(input(
#         "Выберите номинал:\n1 : 1$\n2 : 2$\n3 : 5$\n4 : 10$\n5 : 20$\n6 : 50$\n7 : 100$"
#     ))
#     if command == 1:
#         print('Джордж Вашингтон')
#     elif command == 2:
#         print('Томас Джефферсон')
#     elif command == 3:
#         print('Авраам Линкольн')
#     elif command == 4:
#         print('Александр Гамильтон')
#     elif command == 5:
#         print('Эндрю Джексон')
#     elif command == 6:
#         print('Улисс Грант')
#     elif command == 7:
#         print('Бенджамин франклин')
#     else:
#         print('Такого номинала нет')

# 14
# list_1 = [4.95, 9.95, 14.95, 19.95, 24.95]
# for num in list_1:
#     print(f"{num}$ - {num * 0.6}$")
