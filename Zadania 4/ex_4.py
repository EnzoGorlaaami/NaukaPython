#Zasymuluj grę w papier, kamień, nożyce. Oczywiście będzie to uproszczona wersja, ponieważ będzie zapewniała wprowadzenie
# danych tylko jednorazowo. Pobierz od użytkownika numer 1 słowo spośród: "kamień", "papier", "nożyce",
# operację przeprowadź również dla użytkownika numer 2. Następnie wyświetl, który z użytkowników wygrał to jednorazowe starcie
# (pamiętaj o tym, który przedmiot jest w grze "silniejszy" od drugiego).
# Dodatkowo zabezpiecz program przed wprowadzeniem nieprawidłowych danych,
# czyli jeżeli użytkownik nie wprowadzi ani "kamień", ani "papier", ani "nożyce" program ma natychmiastowo przerwać
# działanie i wyświetlić komnikat: "Błędne dane!".

print('Witam w grze "Papier, nożyce, kamień"!' )
options = ['papier', 'nożyce', 'kamień', 'kamien', 'nozyce']

wyniki = {('papier', 'kamień'): 1, ('papier', 'kamien'): 1, ('nożyce', 'papier'): 1, ('nozyce', 'papier'): 1,
          ('kamień', 'nożyce'): 1, ('kamien', 'nozyce'): 1, ('kamien', 'nożyce'): 1, ('kamień', 'nozyce'): 1}

player_1 = input("Gracz 1, Podaj swój wybór: ")
player_2 = input("Gracz 2, Podaj swój wybór: ")

wybory = (player_1, player_2)
wartosc_wyboru = wyniki.get(wybory, 'win_2')

if player_1 and player_2 in options:
    if wartosc_wyboru == 1:
        print('Gracz 1 wygrał! ')
    elif player_1 == player_2:
        print('Remis!')
    else:
        print('Gracz 2 wygrał! ')
else:
    print('Podano nieprawidłowe wybory!')