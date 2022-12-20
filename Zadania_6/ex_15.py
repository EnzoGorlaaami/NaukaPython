#Stwórz słownik przechowujący 5 dowolnych nr PESEL jako klucze i do każdego z nich przypisz cechy osób o podanym PESELu
# w formie kolejnego słownika (cechy te to: kolor_oczu, imie, nazwisko, wiek), czyli możliwa by była operacja:
#    • Za pomocą pętli for dodaj do każdej wartości w słowniku (która jest kolejnym słownikiem) nowy klucz
#    (imię_matki) oraz nadaj odpowiednie wartości
#    • Usuń z słownika osoby, których pesel kończy się na znak ‘1’.
#    • Wydrukuj zawartość słownika w przyjaznej formie (w komunikacie mają nie wyświetlać się klamry {})

persons = {90101103836:  {'fav_color': 'niebieskie', 'name': 'Roman', 'surname': 'Woch', 'age': 32}, 90909012345: {'fav_color': 'niebieskie', 'name': 'Jim', 'surname': 'Halpert', 'age': 36},
90909054323 : {'fav_color': 'brązowe', 'name': 'Dwight', 'surname': 'Schrute', 'age': 46}, 90909012354: {'fav_color': 'zielone', 'name': 'Pam', 'surname': 'Beesly', 'age': 30},
90909012541 : {'fav_color' : 'czarne', 'name': 'Michael', 'surname': 'Scott', 'age': 42}}

keys_dict = list(persons.keys())


for i in range(len(persons)):
   user_input = input('Podaj imię Matki dla ' + str(keys_dict[i]) + ' : ')
   persons.get(keys_dict[i]).update({'mother_name' : str(user_input)})


for j in range(len(keys_dict)):
    if str(keys_dict[j])[-1] == str(1):
        persons.pop(keys_dict[j])

#dodać usunięcię z listy keys_dict

for k in range(len(persons)):
    one_pers = persons.get(keys_dict[k])
    print(f'Dla numeru pesel {keys_dict[k]} dane wrażliwe to: ')
    print(f'Kolor oczu: {str(one_pers.get("fav_color"))}, Imię: {str(one_pers.get("name"))}, Nazwisko: {str(one_pers.get("surname"))}'
          f', Wiek: {str(one_pers.get("age"))}, oraz Imię Matki: {str(one_pers.get("mother_name"))} ')






