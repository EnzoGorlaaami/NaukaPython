#Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
#• wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
#• pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika.

#Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
#W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

muzyka = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}


for album in muzyka.keys():
    print(album)

user_input = str(input('Wykonawcę którego Albumu chcesz poznać? '))
x = muzyka.get(user_input)
if not x:
    print("Brak")
else:
    print(f'Wykonawcą albumu {user_input} jest {x} .')
