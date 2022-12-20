#Zad. 1
#Napisz program wyświetlający liczby całkowite z przedziału <0; y>, gdzie y podaje użytkownik. Wykonaj to na pętli for i while.

user_input = int(input('Podaj dowolną liczbę całkowita: '))



for liczba in range(user_input):
    print(liczba)

counter = 0
while counter <= user_input:
    print(counter)
    counter += 1

