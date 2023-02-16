# Załóżmy, że plik przyklad.txt składa się tylko i wyłącznie z następującej linii tekstu:
# Panno święta, co Jasnej bronisz Częstochowy
# Jaki efekt otrzymamy, po zapisie poniższych poleceń?

with open("przyklad.txt", encoding="utf-8") as plik:
    print(plik.tell()) #zwroci nam 0 bo jestesmy na poczatku pliku
    print(plik.seek(43)) #zwraca 43, czyli przenosi nas na 43 pozycje zadania
    print(plik.read(1)) # wyrzuca 43 znak
