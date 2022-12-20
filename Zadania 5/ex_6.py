#Zadanie polega na napisaniu programu, który będzie sumować liczby całkowite wpisane przez użytkownika tak długo,
# aż po wczytaniu poprzedniej liczby suma zwiększyła się, Na koniec program wypisuje ostateczną sumę Początkowo suma wynosi 0.
# Zastosuj do tego rozwiązania pętlę while.
# Przykład:
# Użytkownik przykładowo wprowadza kolejno liczby 1, 2, 3, 0 wtedy zwrócona suma to 1 + 2 + 3 + 0 = 6. Z kolei dla liczb 1, 9, 2, -12 suma wyniesie 0.
# ctrl + /


result = 0
check = 1
while True:
    user_input = int(input('Podaj liczbę całkowitą: '))
    # result += user_input
    #if user_input <= 0:
        #    break
    if result + user_input > result:
        result += user_input
    else:
        pass

# user_input = int(input('Podaj liczbę całkowitą: '))
# while result + user_input > result:
#     user_input = int(input("Podaj liczbe calkowita"))
#     result += user_input

print(f'Twoj wynik to: {result}')
