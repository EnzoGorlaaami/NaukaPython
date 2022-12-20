from memory_profiler import profile

#c
#***
#***
#***

@profile
def func():
    w = 5
    h = 100
    for i in range(w):
        for j in range(h):
            print('*', end=" ")
        print()

    # for i in range(h):
    #     print('*' * w)


func()

