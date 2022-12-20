user_input = int(input('Podaj liczbę naturalną: '))

dzielniki_wlasciwe = 0

for liczby in range(1, user_input):
    if user_input % liczby == 0:
        dzielniki_wlasciwe += liczby

if dzielniki_wlasciwe == user_input:
    print("Podana liczba jest liczbą doskonałą! ")
else:
    print('Podana liczba nie jest liczbą doskonałą. ')