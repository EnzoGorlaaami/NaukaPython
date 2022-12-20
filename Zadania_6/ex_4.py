#Napisz program wyświetlający nazwę dnia tygodnia zależnie od liczby wprowadzonej przez użytkownika
# (1 – poniedziałek ,…, 7 – niedziela, inna – „nie ma takiego dnia”)

# days = ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')

user_input = int(input('Podaj numer Twojego dnia od jeden do siedmiu: '))


days = {1: 'poniedzialek', 2: 'wtorek'}

while True:
    if 1 <= user_input <= 7:
        #print("Twój dzień tygodnia to " + days[user_input - 1] + " !")
        print(days.get(user_input))
        break
    else:
        print('Nie ma takiego dnia!')



