#Napisz program, który wyświetli liczby z przedziału <50; 100> podzielne przez całkowitą liczbę k,
# którą podaje użytkownik. Przekształć program tak, aby przedział podawał również użytkownik.

start = int(input('Podaj przedział liczb od najmniejszej: '))
end = int(input('Do największej: '))
divider = int(input('Wyświetl w tym przedziale podzielne przez: '))



for liczba in range(start, end + 1):
    if liczba % divider == 0:
        print(liczba)
