# Napisz program wyznaczający n (podawane przez użytkownika) pierwszych liczb ciągu Fibonacciego. Przykład:
# dla n = 5
# 0, 1, 1, 2, 3, 5

n = int(input('Podaj dowolną liczbę: '))

a,b = 0, 1
print(a)
print(b)
for i in range(n-1):
    c = a + b
    print(c)
    a, b = b, c

#
# for i in range (1,x):
#     y = numb[i-1]  + numb[i]
#     numb.append(y)
#
# print(numb)