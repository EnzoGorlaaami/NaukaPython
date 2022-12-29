# W trakcie Wigilii Bożego Narodzenia, pięciu członków rodziny: Adam, Stanisław, Joanna, Kornelia i Kacper składają sobie życzenia.
# Stwórz program, który wyświetli wszystkie możliwe połączenia między członkami rodzin, jakie mogą zajść w trakcie składania sobie życzeń,
# np. Adam - Stanisław, Adam - Joanna, Adam - Kornelia, Adam - Kacper itd.
import itertools


family = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

for i in range(len(family)):
    for j in range (i+1, len(family)):
        print(f"{family[i]} - {family[j]}")


print(list(itertools.combinations(family, 2)))
print(list(itertools.combinations_with_replacement(family, 2)))