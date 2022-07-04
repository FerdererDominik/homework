# 1
# i = 0
# with open("mbox-short.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     list_split = list(text.split())
#     for mail in list_split:
#         if '@' in mail and 'source' not in mail and '>' not in mail and ')' not in mail:
#             print(mail)
#             i += 1
#     print(f'кол-во мейлов:{i}')

# 2
# list_1 = []
# with open("romeo.txt", "r", encoding="utf-8") as file:
#     text = list(file.read().split())
#     sort = sorted(text)
#     for str in sort:
#         if str in list_1:
#             continue
#         list_1.append(str)
#     print(list_1)

# 3
# def read_last(lines, txt):
#     with open(txt, "r", encoding="utf-8") as file:
#         num = 0 - lines
#         text = file.read()
#         list_txt = list(text.split('\n'))
        # for line in list_txt[num::]: я пробовал сделать через фор для красоты вывода, но в конце выдает none
        #     print(line)
#         return list_txt[num::]
# text = input("Введите название файла:")
# line = int(input("Введите кол-во выведенных последних строк"))
# print(read_last(line, text))

# 4
# def long(txt):
#     with open(txt, "r", encoding="utf-8") as file:
#         text = list(file.read().split())
#         list_longest = []
#         longest = 0
#         for word in text:
#             if len(word) > longest:
#                 longest = len(word)
#         for lens in text:
#             if longest == len(lens):
#                 list_longest.append(lens)
#         return list_longest, longest
# file_name = input('Введите название файла:')
# print(long(file_name))