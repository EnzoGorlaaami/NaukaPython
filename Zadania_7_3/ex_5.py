# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?),
# a następnie korzystając z metod operujących na listach, program powinien:
# • podawać liczbę wyrazów w zdaniu
# • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
# • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak,
# to które są to wyrazy i jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu
# nie występuje program również powinien o tym informować
# • posortować wyrazy ze zdania alfabetycznie i wydrukować je w zmienionej kolejności.

punctuations = [',', '.', ':', ';', '!', '?']

sentence = input('Podaj dowolne zdanie: ')

sentence_without_punctuation = ""

for character in sentence:
    if character not in punctuations:
        sentence_without_punctuation += character

sentence_list = list(sentence_without_punctuation.split())

print(f'Liczba wyrazów w Twoim zdaniu to {(len(sentence_list))}. ')

print(sentence_without_punctuation.split())
counter = 0

for word in sentence_without_punctuation.split():
    if word.istitle():
        print(f'Wyraz z wielkiej litery to {word}. ')
        counter += 1
if counter == 0:
    print('Brak wyrazów z wielkiej litery')


to_find = ['i', 'w', 'na', 'pod', 'dla']
to_find_counter = 0
for word in sentence_without_punctuation.split():
    if to_find.count(word) >= 1:
        print(f'Słowo "{word}" znajduje sie w zdaniu pod indeksem {(sentence_without_punctuation.split()).index(word)}')
        to_find_counter += 1
if to_find_counter == 0:
    print("Żaden z wyrazów: 'i', 'w', 'na', 'pod', 'dla', nie znajduję się w Twoim zdaniu. ")

z = sentence_without_punctuation.split()
z.sort()
print(z[::-1])

