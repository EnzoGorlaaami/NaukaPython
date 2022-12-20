#Utwórz słownik, który przechowuje definicje wyrazów i ich wytłumaczenia.
#Zarządzanie słownikiem ma się odbywać za pomocą interaktywnego MENU
#(MENU ma być obsługiwane za pomocą print() oraz input() oraz ma wyglądać tak jak poniżej):
#1. Dodaj słowo wraz z definicją
#2. Znajdź definicję słowa
#3. Usuń słowo wraz z definicją z słownika
#4. Zakończ program
# menu = {1: '1. Dodaj słowo wraz z definicją', 2: '2. Znajdź definicję słowa',
#         3: '3. Usuń słowo wraz z definicją ze słownika', 4: '4. Zakończ program'}
# for h in range(1, len(menu) + 1):
#     print(menu.get(h))

dictionary = {}

print('Witam w Twoim słowniku ;) ')
print('Wszystkie komendy wpisujemy bez polskich znaków, białych znaków oraz wielkich liter! ')

print("1: Dodaj słowo wraz z definicją")
print("2. Znajdź definicję słowa")
print("3. Usuń słowo wraz z definicją ze słownika")
print("4. Zakończ program")
while True:
    user_choice = int(input('Co robimy?: '))
    if user_choice == 1:
        num_words = int(input('Ile słów chcesz dodać?: '))
        for i in range(num_words):
            word = input('Dodaj słowo: ')
            definition = input('Podaj definicję swojego słowa: ')
            # user_dict.update({user_input1 : user_input2})
            dictionary[word] = definition

    elif user_choice == 2:
        num_words = int(input('Ile słów chcesz odczytać ze słownika?: '))
        for i in range(0, num_words):
            word = input('Jaką definicję chcesz poznać?: ')
            print(dictionary.get(word, 'Brak definicji w słowniku'))

    elif user_choice == 3:
        num_words = int(input('Ile słów chcesz usunąć ze słownika?: '))
        for i in range(num_words):
            word = input('Jaką definicję chcesz usunąć?: ')
            if word in dictionary:
                del dictionary[word]
                print('Słowo zostało usunięte!')
            else:
                print('Brak takiego słowa! ')
    elif user_choice == 4:
        print("Do następnego razu! ")
        break


