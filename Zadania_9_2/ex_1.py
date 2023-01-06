#Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej
#jako parametr listy

nums = [4, 6, 8, 24, 12, 2]

def najwyzsza_liczba(lista):
    lista.sort(reverse=True)

    return lista[0]

print(najwyzsza_liczba(nums))