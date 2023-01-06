# Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału 5 - 120.
# Następnie usuń ze zbioru wszystkie liczby parzyste.
#
# import random
# a = []
#
# while len(a) < 15:
#     a.append(random.randint(5, 120))
# print(a)
#
# even_numbers = []
#
# for number in a:
#     if number % 2 != 0:
#         even_numbers.append(number)
#
# print(even_numbers)


import random

s = set()
for i in range(15):
    s.add(random.randint(5, 120))

for elem in list(s):
    if elem % 2 == 0:
        s.remove(elem)

print(s)

