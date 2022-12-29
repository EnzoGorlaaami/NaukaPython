#Napisz program, sprawdzający czy dany wyraz jest palindromem (jest czytany tak samo od przodu i tyłu), np. sedes, Anna.

input = (list(input('Podaj dowolny wyraz: ')))

if input == input[::-1]:
    print("Palindrom")
else:
    print("Nie Palindrom")

# y = []
# x = len(input)
# y.extend(input)
# input.reverse()
#
# counter = 0
# counter2 = 0
#
# if x % 2 == 0:
#     for i in range(int(x / 2)):
#         if input[i] == y[i]:
#             counter += 1
# else:
#     for j in range(int((x / 2) -1)):
#         if input[j] == y[j]:
#             counter2 += 1
#
# if counter == (x / 2) or counter2 == ((x / 2) -1):
#     print("Twój wyraz to palindrom! ")
# else:
#     print("Niestety, Twój wyraz nie jest palindromem. ")
