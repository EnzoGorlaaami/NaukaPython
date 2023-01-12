# Pamiętasz zadanie nr 9 z cyklu zadań: 5 Podstawy Pętle (to o astronautach)?
# Masz następujące zadanie - zrefaktoryzować wówczas napisany kod w taki sposób, aby rozwiązanie oprzeć o funkcje!


def get_fuel():
    fuel = 0
    while not 5000 <= fuel <= 30000:
        fuel = int(input('Podaj ilość paliwa pomiędzy 5000 a 30000 litrów: '))
    return fuel

def get_pilots():
    pilot = 0
    while not 1 <= pilot <= 7:
        pilot = int(input('Podaj ilość pilotów pomiędzy 1 a 7: '))
    return pilot

def cosmic_fly(fuel, pilot):
    rocket_height = 0
    while fuel > 0 and rocket_height <= 1999:
        fuel -= 300 + 100 * pilot
        rocket_height += 100
        print(f'Przelecieliśmy {rocket_height} Km! ')
    if rocket_height >= 2000:
        print('Dolecieliśmy do orbity! ')
    else:
        print(f'Paliwo się skończyło, spadniemy {rocket_height} Km w dól ;) ')

def main():

    cosmic_fly(get_fuel(), get_pilots())

if __name__ == "__main__":
    main()