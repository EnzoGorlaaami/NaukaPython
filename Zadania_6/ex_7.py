#Wykorzystując instrukcje warunkowe, stwórz funkcjonalność wyliczania wartości bezwzględnej z
#podanej przez użytkownika liczby, np. -5 zamieniane na 5, 5 bez zmian, czyli pozostaje 5.
#Wartością bezwzględną dowolnej liczby rzeczywistej x to: -> abs(5)
#    • ta sama liczba rzeczywista x, gdy podane x ≥ 0
#    • liczba −x (przeciwna do x), gdy podane x < 0

user_input = int(input('Podaj dowolną liczbę: '))

print(abs(user_input))

