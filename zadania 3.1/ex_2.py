    #dodać 3 do wprowadzonej wcześniej liczby
    #wyświetlić na ekranie zdanie:  ‘Teraz Ala ma już … kotów’ (w miejsce kropek wpisujecie obliczoną przez program prawidłową liczbę)
    #wyświetlić to zdanie tak, aby każde słowo było oddzielone przecinkiem
    #wyświetlić to zdanie tak, by każde słowo znajdowało się w osobnej linijce
    #sprawdzić, czy wszystkie litery są małe i jeśli nie, to zamienić je na małe (wyświetl  wynik tej zmiany)
    #zmień pierwszą literę zdania na wielką i wyświetl zdanie po tej modyfikacji







user_input = int(input("Ile kotów ma dzisiaj Ala? "))

phrase = "Dzisiaj Ala znalazła jeszcze 3 koty na podwórku ..."
user_input += 3

phrase_2 = f"Teraz Ala ma już {user_input} Kotów"
print(phrase_2)
phrase_3 = phrase_2.replace(" ",",")
print(phrase_3)
phrase_4 = phrase_2.replace(" ","\n")
print(phrase_4)
phrase_5 = phrase_2.capitalize()
print(phrase_5)

if phrase_2 == phrase_2.islower():
   print(phrase_2)
else:
    print(phrase_2.lower())
