#Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej
#jako parametr listy

nums = [4, 6, 8, 24, 12, 2]

# def najwyzsza_liczba(lista):
#     lista.sort(reverse=True)
#
#     return lista[0]
#
# print(najwyzsza_liczba(nums))

max_value = -float('inf') #
max_index = -1

for idx, num in enumerate(nums): # -> [(0, 4), (1, 6), (2, 8)]
    if num > max_value:
        max_value, max_index = num, idx

print(max_value, max_index)
# for i in range(len(nums) -1):
#     print(nums[i] > nums[i + 1])