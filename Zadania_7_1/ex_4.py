#Napisz program, który utworzy dwa zbiory:
#
import string
us_inp1 = int(input('Podaj granice zbioru "A" liczb naturalnych parzystych: '))

a = []

for i in range (1, (us_inp1 + 1)):
    if i % 2 == 0:
        a.append(i)
print(a)

us_inp2 = int(input('Podaj granice zbioru "B" liczb naturalnych, które przy dzieleniu przez 3 dają resztę 2: '))

b = []

for j in range (3, (us_inp2 + 1)):
    if j % 3 == 2:
        b.append(j)
print(b)

c = (set(a) | set(b))
d = (set(a) & set(b))
e = (set(a) - set(b))
f = (set(a) ^ set(b))
print(len(c))
created_set = [c, d, e, f]

name = string.ascii_lowercase[2:6]

for k in range(len(created_set)):
    if len(created_set[k]) != 0:  # DZIAŁA - zmienione 'name' na 'created_set'
        print(len(created_set[k]))
        print(f'Zbiór {name[k]} zawiera {len(created_set[k])} elementów. Ten elementy to {created_set[k]}')

if list(d) == list(b):
    print('Zbiór B zawiera sie w Zbiorze A. ')
else:
    print('Zbiór B nie zawiera sie w zbiorze A. ')