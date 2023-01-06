# Pamiętasz zadanie nr 9 z cyklu zadań: 5 Podstawy Pętle (to o astronautach)?
# Masz następujące zadanie - zrefaktoryzować wówczas napisany kod w taki sposób, aby rozwiązanie oprzeć o funkcje!

rocket_height = 0
# counter = 0
fuel = 0
pilot = 0
while not 5000 <= fuel <= 30000:
    fuel = int(input('Podaj ilość paliwa pomiędzy 5000 a 30000 litrów: '))


while not 1 <= pilot <= 7:
    pilot = int(input('Podaj ilość pilotów pomiędzy 1 a 7: '))


while  fuel > 0 and rocket_height <= 1999:
    fuel -= 300 + 100 * pilot
    rocket_height += 100
    print(f'Przelecieliśmy {rocket_height} Km! ')
#
#

if rocket_height >= 2000:
    print('Dolecieliśmy do orbity! ')
else:
    print(f'Paliwo się skończyło, spadniemy {rocket_height} Km w dól ;) ')