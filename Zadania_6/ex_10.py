#Program ma realizować pobranie od użytkownika przedziału (dolnego i górnego) liczb i
#następnie ma wylosować wartość z podanego przedziału.
#Następnie realizowana jest już główna część programu – czyli użytkownik ma odgadnąć wylosowaną liczbę.
# Proces wygląda tak, że użytkownik podaje liczbę, program sprawdza, czy jest to wylosowana wcześniej liczba
# - jeśli nie, to podaje informacje, czy użytkownik podał za dużą czy małą liczbę i daje mu możliwość ponownego wpisania wartości.
# Po każdej błędnej próbie, użytkownikowi nalicza się 1 ujemny punktów
# (zaczyna od ilości punktów równej różnicy przedział_górny - przedział_dolny).
# Po odgadnięciu liczby, na ekranie powinien wyświetlać się komunikat “Gratulacje! Zdobyłeś X punktów” (X - wartość punktacji użytkownika).

import random

start = int(input('Podaj dolny zakres swoich licz: '))
end = int(input('Podaj górny zakres swoich licz: '))

counter = end - start

pc_random = random.randint(start, end)
while counter >= 0:
    guess = int(input('Zgadnij, jaką liczbe z Twojego przedziału, wylosował komputer: '))
    # if guess <= end and guess >= start:
    if guess in range(start, end):
        if guess == pc_random:
            print('Gratulacje ! To właśnie ta liczba! Zdobyłeś ' + str(counter) + ' punktów! ')
            break
        elif start <= guess < pc_random:
            print('Podałeś za małą liczbę, próbuj dalej!')
            counter -= 1
        elif guess > pc_random:
            print('Podałeś za dużą liczbę, próbuj dalej!')
            counter -= 1
    else:
        print('Liczba poza zakresem! ')
