# Znajdź błąd w poniższym przykładzie realizującym odczyt danych z pliku: przyklad.txt.

plik = open("przyklad.txt", "r")

linie = plik.readlines()
print(linie)

plik.close() #brakuje zamkniecia pliku

#lub mozna uzyc Context Managera :

with open("xxx.txt", "r") as plik:

    x = plik.readlines()
    print(x)

