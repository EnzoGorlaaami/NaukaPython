#Napisz program, wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik.

user_input = int(input('Podaj wysokość potęgi: '))

for num in range(1, user_input + 1):
    print(2 ** num)

counter = 1


while counter < user_input + 1:
    print(2 ** counter)
    counter += 1
