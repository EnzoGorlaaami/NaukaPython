user_input = input("Podaj zdanie z minimum 5 spacjami na początku: ")
spacja = "     "
counter = 0

while counter == 0:
    if spacja in user_input:
        print(user_input)
        print(user_input.lstrip())
        counter += 1
    else:
        print("Błedne zdanie, spróbuj jeszcze raz! :)")
        counter += 1

