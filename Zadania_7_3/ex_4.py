# Napisz program, który poprosi użytkownika o podanie imion kilku swoich dobrych znajomych.
# Korzystając z wprowadzonych danych, dla każdego z podanych znajomych, program ma wyświetlić spersonalizowany komunikat,
# na przykład powitanie, pozdrowienie, który będzie skierowany do konkretnej osoby.

numb = int(input("Ilu znajomych chcesz przywitać? "))
friends = []
for name in range(numb):
    name = input('Podaj Imie znajomego: ')
    friends.append(name)

for i in range(len(friends)):
    print(f'Witaj {friends[i]}, Mój przyjacielu! ')