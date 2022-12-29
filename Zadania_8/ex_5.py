# Stwórz następującą strukturę danych (słownik):
# zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0}, "Klient_222" {"nazwa_deseru” : "lody waniliowe", "rachunek" : 5.0 }}
# Następnie wyświetl nazwy wszystkich klientów i dla każdego z nich stwórz podsumowanie zamówienia:
#
# Przykładowy output:
# Klient_1335:
# nazwa_potrawy rosół
# ocena 5
# rachunek 20.0
#
# Klient_222:
# nazwa_deseru lody waniliowe
# rachunek 5.0

orders = {"Klient_1335": {"nazwa_potrawy": "rosół", "ocena": 5, "rachunek": 20.0},
              "Klient_222": {"nazwa_deseru": "lody_waniliowe", "rachunek": 5.0}}


for client in orders:
    print(f'{client}: ')
    x = orders.get(client)
    for key in x:
        print(f'{key} : {x[key]}')
    print()


