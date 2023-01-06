# Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia w
# jedną listę w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]
list_even = [2, 4, 6, 8]
list_odd = tuple[1, 3, 5, 7]
def list_union(**kwargs):
    equal = []
    for klucz in kwargs:
        for i in range(kwargs):
            equal.append(kwargs[klucz][i])

    print(equal)


list_union(a=list_odd, b=list_even)