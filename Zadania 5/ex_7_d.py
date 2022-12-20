#d choinkę o wysokości 5*

# counter = 1
# height = 5
# star = '*'
#
# zakres = star * counter
#
# for j in range(height):
#     zakres = star * counter
#     if counter % 2 == 0:
#         print(zakres.center(height, ' '), end= ' ')
#         print()
#         counter += 1
#     else:
#         print(zakres.center(height, ' '), end= ' ')
#         print()
#         counter += 1

height = 5
for i in range(height):
    print(' ' * (height - i) + '*' * (2 * i + 1) + ' ' * (height - i))