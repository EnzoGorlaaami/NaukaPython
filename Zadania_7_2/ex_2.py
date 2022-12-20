# Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o nowych albumach do słownika.
# Program ma zawierać proste menu.

print('Witam w naszym słowniku Albumów! ')

music = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
for i in music:
    print(i)

menu = {1 : '1. Dodaj album wraz z wykonawcą', 2 : '2. Znajdź wykonawcę albumu',
        3 : '3. Usuń  album', 4 : '4. Zakończ program'}

print('Wszystkie komendy wpisujemy bez polskich znaków. ')

for h in range(1, len(menu) + 1):
    print(menu.get(h))
while True:
    user_input_menu = int(input('Co robimy?: '))
    if user_input_menu == 1:
        user_input_append = int(input('Ile albumów chcesz dodać?: '))
        for i in range(0, user_input_append):
            user_input1 = input('Dodaj album: ')
            user_input2 = input('Podaj wykonawce albumu: ')
            music.update({user_input1 : user_input2})

    elif user_input_menu == 2:
        user_input = str(input('Wykonawcę którego Albumu chcesz poznać? '))
        x = music.get(user_input, 'Brak danych')
        if  x == 'Brak danych':
            print(x)
        else:
            print(f'Wykonawcą albumu {user_input} jest {x} .')

    elif user_input_menu == 3:
        user_input_delete = int(input('Ile albumów chcesz usunąć ze słownika?: '))
        for k in range(0, user_input_delete):
            user_input3 = input('Jaki album chcesz usunąć?: ')
            if user_input3 in music:
                music.pop(user_input3)
                print('Słowo zostało usunięte!')
            else:
                print('Brak takiego słowa! ')

    elif user_input_menu == 4:
        print("Do następnego razu! ")
        break