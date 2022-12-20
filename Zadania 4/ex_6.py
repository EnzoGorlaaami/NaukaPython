#1. Użytkownik wybiera czy obstawia reszkę, czy orła (literka r – reszka,literka o – orzeł)
#2. Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje
#'rzutu', czyli losowego wyboru orzeł / reszka.
#3. Komputer wyświetla wynik rzutu.
#4. Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli
#komputer to dodaje punkt dla komputera.

#Podpowiedź: W celu losowania wartości wykorzystaj metodę randint()
# (pamiętaj o linijce import random na samej górze programu) i przypisz konkretne liczby do orła/reszk

from time import sleep
import random


counter = [3, 2, 1]
player_score = 0
pc_score = 0

player_options = 0

while True:
    choice_counter = True
    while choice_counter:
        user_input = input("Orzeł (podaj 'o'), czy reszka(podaj 'r') ?: ")
        if user_input == "r":
            choice_counter = False
            player_options = 1
        elif user_input == "o":
            choice_counter = False
            player_options = 2
        else:
            print('Zły wybór, podaj ponownie!')

    for counter in [3, 2, 1]:
        print(counter)
        sleep(0)

    pc_choice = random.randint(1, 2)

    if pc_choice == 1:
        print('Wypadła reszka! ')
    else:
        print('Wypadł orzeł! ')


    if player_options == pc_choice:
        print('Wygrałeś! ')
        player_score += 1
    else:
        print('Przegrałeś! ')
        pc_score += 1


    if pc_score == 3 or player_score == 3:
        break

if pc_score > player_score:
    print('Wygrałem Mecz! ')
else:
    print('Wygrałeś Mecz! ')
