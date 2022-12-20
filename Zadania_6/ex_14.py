#Zadanie jest dość nietypowe, ale myślę, że pomoże lepiej zrozumieć strukturę list zagnieżdżonych.
# Twoim zadaniem jest za pomocą listy i zagnieżdżonej w niej list z gwiazdkami, odzwierciedlić kształt +,
# a następnie wydrukować zawartość tych list, aby otrzymać oczekiwany efekt

stars = [['     *     '], ['****']]

for i in range(4):
    print(stars[0])

for i in range(2):
    print(stars[1], end= ' ')

print()

for i in range(4):
    print(stars[0])

#or
for k in range(4):
    print()

stars_2 = [['     *     '], ['     *     '], ['     *     '], ['     *     '], ['****   ****'], ['     *     '], ['     *     '], ['     *     '], ['     *     ']]

for j in stars_2:
    print(j)