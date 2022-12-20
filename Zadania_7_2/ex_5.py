# Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy
# (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
# Przykładowy input: n = 5
# Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

x = int(input('Podaj liczbę całkowitą n: '))

dict = {}

for i in range (1, x + 1):
    dict.update({i : i * i})

print(f'Twój słownik liczb to {dict}. ')