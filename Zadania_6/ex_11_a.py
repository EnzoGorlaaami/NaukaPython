#Wydrukuj za pomocą pętli i symbolu gwiazdki poniższe kształty:
#Wykorzystaj pętle zagnieżdżone (pętla umieszczona w innej pętli), gdzie pętla zewnętrzna będzie służyła do
# przechodzenia po wierszach, a pętla wewnętrzna do rysowania gwiazdek w obrębie wiersza.

#prostokąt 7 x 6

user_input1 = int(input('Podaj wysokość prostokąta: '))
user_input2 = int(input('Podaj szerokość prostokąta: '))

for i in range(0, user_input1):
    for j in range(0, user_input2):
        print('*', end = ' ')
    print()

#TODO Zmiana na wydajniejsze