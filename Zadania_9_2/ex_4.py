#Napisz funkcję odbierającą w postaci *args dowolną ilość elementów i zwracającą ich iloczyn.

def product(*args):
    score = 1
    for numb in args:
        score *= numb

    print(score)

product(2, 2)