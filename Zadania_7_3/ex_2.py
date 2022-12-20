# W pewnej grze liczbowej wylosowano następujące liczby:
# wynik = [12,1,45,76,50,23]. Okazało się jednak, że wylosowane wartości powinny zawierać się w przedziale od 1 do 49.
# Napisz program zastępujący dowolne liczby – nie tylko te konkretne z zadania - występujące w liście,
# które nie spełniają tego kryterium, na wylosowane liczby, które będą je spełniać. Program powinien
# także zakomunikować, że znalazł błędną wartość i dokonał dla niej zmiany.
#
# Podpowiedź:
# Użyj modułu random, który trzeba importować, czyli: import random na początku programu. Zawiera on szereg funkcji
# losowych - poczytaj w Internecie o funkcjach losowych w Pythonie 3.
# Jeśli chcesz wylosować liczbę całkowitą z przedziału [a,b], to możesz użyć funkcji losowej: randint(a,b), np. randint(5,10).

import random

score = [12, 1, 45, 76, 50, 23]
too_h = []

for i in range (len(score)):
    if score[i] >= 50:
        too_h.append(score[i])
        x = random.randint(1, 49)
        score.append(x)
        print(f'Znaleziona za wysoka liczba! {score[i]} została zastąpiona {x}! ')

print(f'Wylosowane liczby to {(set(score) - set(too_h))}')