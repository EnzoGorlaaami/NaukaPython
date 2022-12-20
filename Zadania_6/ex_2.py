#Napisz program pobierający od użytkownika liczbę n i wyświetlający wartość sumy 1 + 2 + 3 + … + n.

user_input = int(input('Podaj dowolną liczbę: '))
wynik = 0

for i in range(user_input):
    wynik += i

print(wynik)