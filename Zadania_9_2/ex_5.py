# Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia w
# jedną listę w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]

# def list_union(counter, **kwargs):
#     equal = []
#     for val in range(counter):
#         for list in kwargs.values():
#             equal.append(list[val])
#
#     print(equal)
#
# list_even = [2, 4, 6, 10, 12, 12]
# list_odd = [1, 3, 5, 7, 9]
#
# list_union(a=list_odd, b=list_even, counter=(len(list_odd)))


def list_union(**kwargs):
    arr = []
    odds, evens = kwargs.values()
    for odd, even in zip(odds, evens): # -> [(2, 1), (4, 3), (6, 5)]
        arr.append(odd)
        arr.append(even)
    print(arr)
list_even = [2, 4, 6, 10, 12, 12]
list_odd = [1, 3, 5, 7, 9, 9, 9]

list_union(a=list_odd, b=list_even)