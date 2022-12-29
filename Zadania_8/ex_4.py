# Napisz program generujący wszystkie możliwe kombinacje liczb 4-cyfrowych, np. 1000, 1001, 1002, ..., 9999.
from memory_profiler import profile
number = input("Podja liczbe")



import random

x = range(1000, 9001)

# for i in range(999, 9001):
#     x.append(i)
print(f' Ilość liczb: {len(x)}, najniższa: {x[0]}, najwyższa: {x[-1]}')
