# 1
# dict_1 = {}
# i = 0
# while i < 5:
#     i += 1
#     num = int(input("Введите число"))
#     dict_1[num] = num * num
#     # print(dict_1)
# print(dict_1)

# 2
# sm = 0
# dict_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# for i, j in dict_1.items():
#     sm = sm + dict_1[i]
#     print(sm)
# sr = sm / len(dict_1)
# print(sr)

# 3
# list_1 = [1, 3, 5, 7, 9]
# list_2 = [2, 4, 6, 8, 10]
# print(dict(zip(list_1, list_2)))

# 4
# dict_1 = {"Moscow": (550, 370), "London": (510, 510), "Paris": (480, 480)}
# dist = {}
# ML = ((550 - 370) ** 2 + (510 - 510) ** 2) ** 0,5
# dist["Msc => London"] = ML
# MP = ((550 - 370) ** 2 + (480 - 480) ** 2) ** 0,5
# dist["Msc => Paris"] = MP
# LP = ((510 - 510) ** 2 + (480 - 480) ** 2) ** 0,5
# dist["London => Paris"] = LP
# print(dist)
# Я слегка не понял как выполнять это задание

# 5
# goods = {"Лампа": '12345', "Стол": '23456', "Диван": '34567', "Стул": '45678'}
# store = {'12345': [{'quanity': 27, 'price': 42}],
#          '23456': [{'quanity': 22, 'price': 510}, {'quanity': 31, 'price': 520}],
#          '34567': [{'quanity': 2, 'price': 1200}, {'quanity': 1, 'price': 1150}],
#          '45678': [{'quanity': 50, 'price': 100}, {'quanity': 12, 'price': 95}, {'quanity': 43, 'price': 97}]}
# print(store[goods["Лампа"]])
# while True:
#     command = int(input(
#         'Введите команду:\n\t1-"Лампа"\n\t2-"Стол"'
#         '\n\t3-"Диван"\n\t4-"Стул"\nВаша команда'))
#     if command == 1:
#         # for i, j in store[goods["Лампа"]]:
#         print(f"Стоимость всех стульев:{27 * 42}")
#     elif command == 2:
#         print(f"Стоимость всех столов:{(22 * 510) + (31 * 520)}")
#     elif command == 3:
#         print(f"Стоимость всех диванов:{(2 * 1200) + (1 * 1150)}")
#     elif command == 4:
#         print(f"Стоимость всех стульев:{(50 * 100) + (12 * 95) + (42 * 97)}")
#     else:
#         print("Такого номера нет")