#Napisz program sprawdzający, czy podana przez użytkownika jest ujemna,
#dodatnia lub czy ma wartość równą 0.

user_input = int(input('Podaj dowolną liczbę całkowitą: '))

if user_input < 0:
    print("Podana wartość jest liczbą ujemną. ")
elif user_input == 0:
    print('Podałeś zero. ')
else:
    print('Podałeś liczbę dodatnią')