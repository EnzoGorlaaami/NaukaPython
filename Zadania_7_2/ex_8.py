# Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
# Dla danych:
dane = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
# Oczekujemy wyniku:
# “S002”, “S009”, “S007”

wartosci = dane.values()

y = tuple(wartosci)
x = list(tuple(wartosci))

uniq = []

for i in range (len(y)):
    if y.count(str(x[i])) == 1:
        uniq.append(str(x[i]))


print(uniq)