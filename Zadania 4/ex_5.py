#Napisz program pobierający od użytkownika 2 liczby. Sprawdź, czy co najmniej 1 z nich jest parzysta.

user_input1 = int(input('Podaj pierwszą liczbę całkowitą: '))
user_input2 = int(input('Podaj drugą liczbę całkowitą: '))

if user_input1 % 2 == 0 or user_input2 % 2 == 0:
    print('Co najmniej jedna z podanych liczb jest parzysta ')
else:
    print('Żadna z liczb nie jest parzysta ')