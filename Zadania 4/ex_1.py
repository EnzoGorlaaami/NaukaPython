#Poproś użytkownika o podanie 3 dowolnych długości
#boków trójkąta. Sprawdź, czy jest to trójkąt prostokątny (wykorzystaj
#własność trójkąta prostokątnego, która mówi że suma kwadratów dwóch
#(przyprostokątnych) jest równa kwadratowi przeciwprostokątnej).

counter = 0
boki = []

while counter < 2:
    user_input = int(input('Podaj długość przyprostokątnej: '))
    boki.append(user_input)
    counter += 1
if counter == 2:
    user_input = int(input('Podaj długość przeciwprostokątnej: '))
    boki.append(user_input)

x = boki[0]
y = boki[1]
z = boki[2]

if x ** 2 + y ** 2 == z ** 2:
    print('Gratulacje, podałeś właściwe wartości trójkąta prostokątnego! ')
else:
    print('Niestety, ten trójkąt nie jest prostokątny')