# Zad 1.
# Napisz program wydrukowywujący poniższy wzór:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



for i in range(6):
    print("* " * i)

for i in range(4, 0, -1):
    print("* " * i)


for i in range(1, 10):
    if i <= 5:
        print('* ' * i)
    else:
        print('* ' * (10-i))