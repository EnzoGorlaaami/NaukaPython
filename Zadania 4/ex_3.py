#Pobierz od użytkownika 3 liczby i wyświetl największą z nich.

counter = 0
liczby = []

while counter < 3:
    user_input = int(input('Podaj dowolną liczbę całkowitą: '))
    liczby.append(user_input)
    counter += 1

print(max(liczby))