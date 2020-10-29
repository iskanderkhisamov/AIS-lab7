import random
import string

print("Задание 1:")
in_list = []
for i in range(10):
    in_list.append(random.randint(-10, 10))
print("Исходный список:", in_list)
out_list = []
in_list = in_list[::2]
for i in in_list:
    if i < 0:
        out_list.append(i)
print("Новый список:", out_list)

print()

print("Задание 2:")
uppers = 0
lowers = 0
letters = []
for i in range(10):
    letters.append(random.choice(string.ascii_letters))
for i in letters:
    if i.islower():
        lowers += 1
    else:
        uppers += 1
print(letters)
print("Количество прописных: {}, строчных: {}".format(uppers, lowers))
