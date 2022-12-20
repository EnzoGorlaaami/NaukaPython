#Wprowadź krotkę d = (1, [2, 4], 'tekst', 3 + 5j) i:
#a) wyświetl jej ostatni element
#b) wyświetl jej pierwszy i drugi element
#c) sprawdź, czy tekst 'abc' jest elementem krotki

d = (1, [2, 4], 'tekst', 3 + 5j)

print(d[-1])
print(d[:2])
print('abc' in d)
