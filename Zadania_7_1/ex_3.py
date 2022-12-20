#Napisz program, który poprosi użytkownika o podanie zestawu ulubionych przez niego kolorów (dowolna liczba).
#Kolory powinny być wpisane w jednej linii jako tekst i rozdzielone spacją.
#W programie powinien znajdować się zbiór Twoich ulubionych kolorów. Należy porównać oba zbiory:
#Twój i użytkownika oraz sprawdzić, czy są jednakowe. Jeśli tak, należy wydrukować odpowiedni komentarz, jeśli nie należy podać te kolory, które:
#    • wybrały obie osoby
#    • wybrał tylko użytkownik
#    • preferuje jedynie autor programu

my_colors = {'zielony', 'pomaranczowy'}

user_input = input('Podaj swoje ulubione kolory, oddziel każdy spacją: ')
user_colors = set(user_input.split(' '))


if my_colors == user_colors:
    print('Nasze ulubione kolory są takie same! ')
elif not my_colors.intersection(user_colors):
    print('Nie mamy wspólnych ulubionych kolorów. ')
else:
    print(f'Nasze wspólne kolory to {my_colors.intersection(user_colors)} .')
    if user_colors.difference(my_colors):
        print(f'Tylko Twoje ulubione kolory to {user_colors.difference(my_colors)} .')
    print(f'Tylko Moje ulubione kolory to {my_colors.difference(user_colors)} .')

x = {'x', 'y'}
y = set()

if y:
    print("ok")