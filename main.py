# 1
# products_list = []
# while True:
#     command = input(
#         "Введите команду:\n\t1.add: Добавить продукт в список\n\t2.delete: Удалить продукт из списка"
#         "\n\t3.show: Вывод списка продуктов\n\t4.clear: Очистить список\n\t5.search: Наличие продукта в списке"
#         "\n\t6.break: Остановить программу\nВаша команда:").lower()
#     if command == "1":
#         product_name = input("Введите название продукта: ")
#         products_list.append(product_name)
#     elif command == "2":
#         product_name = input("Введите название продукта: ")
#         if product_name not in products_list:
#             print("Такого продукта нет в списке")
#             continue
#         products_list.remove(product_name)
#     elif command == "3":
#         print(products_list)
#     elif command == "4":
#         products_list.clear()
#     elif command == "5":
#         name = input("Введите название продукта:")
#         if name not in products_list:
#             print("Такого продукта нет в списке")
#             continue
#         print("Продукт есть в списке")
#     elif command == "6":
#         print("Остановка работы")
#         break
#     else:
#         print("Такой команды нет\n")

# 2
# money = int(input("Введите кол-во денег для вклада:"))
# year = int(input("Введите срок вклада в годах:"))
# i = 0
# percent = 0
# while i <= year:
#     i += 1
#     percent = money / 10
#     money += percent
# print(money)

# 3
# rows = int(input("Введите кол-во строк:"))
# for i in range(rows + 1):
#     for num in range(i):
#         print(num + 1, end=" ")
#     print("")

# 4
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers:
#     if num % 5 == 0 and num <= 150:
#         print(num)
#     elif num > 500:
#         print("Число больше 500")
#         break

# 5
# a = 0
# b = 1
# c = int(input("Введите кол-во раз:"))
# i = 0
# print(a, b, end=" ")
# while i <= (c // 2):
#     i += 1
#     a += b
#     print(a, end=" ")
#     b += a
#     print(b, end=" ")