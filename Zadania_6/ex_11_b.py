#kwadrat 5 x 5 bez wypełnionego środka

square_side = int(input('Podaj bok kwadratu: '))
#
# for j in range(square_side):
#     print('*', end = ' ')
# print()
# for j in range(2, square_side):
#     print('*', end = ' ')
#     for i in range(2, square_side):
#         print(' ', end=' ')
#     print('*', end=' ')
#     print()
# for j in range(square_side):
#     print('*', end = ' ')


for i in range(square_side):
    if i == 0 or i == square_side - 1:
        print('*' * square_side)
    else:
        print('*' + ' ' * (square_side - 2) + '*')