#Napisz program, który wczyta dowolne zdanie podane przez użytkownika. Usunie z tego zdania znaki interpunkcyjne (, . : ; ! ?), a następnie:
#korzystając z metod krotek:
#    • zliczy wszystkie wyrazy w zdaniu
#    • wydrukuje wszystkie wyrazy ze zdania w jednej linii
#    • poda jaki jest pierwszy i czwarty wyraz w tym zdaniu
#korzystając z metod zbiorów:
#    • zliczy unikatowe wyrazy w zdaniu
#    • wyświetli unikatowe wyrazy ze zdania w jednej linii
#    • poda jaki jest pierwszy i czwarty wyraz w tym zdaniu, zakładając, że pierwszy wyraz rozpoczyna zbiór.
#    • sprawdzi, czy elementy: pierwszy i czwarty z ostatnich poleceń podpunktów a i b są takie same czy też nie.

punctuations = [',', '.', ':', ';', '!', '?']

sentence = input('Podaj dowolne zdanie: ')

sentence_without_punctuation = ""

for character in sentence:
    if character not in punctuations:
        sentence_without_punctuation += character


print(sentence_without_punctuation)





