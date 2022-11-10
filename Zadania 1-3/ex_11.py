# Utwórz dwa dowolne stringi o różnych wartościach. Utwórz trzeci napis, który będzie się
# składał z pierwszej połówki pierwszego napisu oraz drugiej połówki drugiego napisu. Skorzystaj z ujemnych indeksów.
imie1 = "Massimo"
imie2 = "Aligieri"
imie3 = "Kacjanr"



pierwsza_czesc = len(imie1) // 2
druga_czesc = len(imie2) // 2
print(f'{imie1[:pierwsza_czesc]}{imie2[druga_czesc:]}')


tekst1 = 'xyz'

tekst2 = tekst1[:]
