#Wypisz wartość średniej arytmetycznej pierwszych 10 liczb naturalnych

liczby_naturalne = 0
counter = 0

for liczby in range(1, 11):
    liczby_naturalne += liczby
    counter += 1

print("=" * 30, "OUTPUT", "=" * 30)
print(liczby_naturalne / counter)
print("=" * 30, "OUTPUT", "=" * 30)
