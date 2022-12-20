#Utwórz listę przechowującą 10 dowolnych liczb podanych przez użytkownika za pomocą input().
#W celu pobierania i umieszczania danych od usera, zastosuj pętle. Następnie wyświetl z listy tylko liczby parzyste.

list = []
list_even = []

for i in range(10):
    user_input = int(input("Podaj dowolną liczbę: "))
    list.append(user_input)

#
# for j in range(10):
#     if list[j] % 2 == 0:
#         list_even.append(list[j])

for num in list:
    if num % 2 == 0:
        list_even.append(num)

print(list_even)
print(list)

