# Stwórz funkcję, która przyjmować będzie dowolny zestaw parametrów reprezentowanych przez **kwargs.
# Następnie niech taka funkcja utworzy z kwargs słownik, który będzie składał się
# z takim samych par klucz:wartość co kwargs, ale będą one odwrócone.
# Na przykład:
# Gdy kwargs przyjmie postać {klucz1:wartość1, klucz2:wartość2}, to powstały słownik ma mieć następującą strukturę: {wartość1:klucz1, wartość2:klucz2}.
#
# Następnie zapisz tak utworzony słownik do pliku o nazwie output.json.

rev_dict = {}
def reverse_dict(**kwargs):
    for item in kwargs:
        rev_dict.update({kwargs[item] : item})
    return rev_dict

reverse_dict(a=1, b=2, c=3, d=4)

import json

with open("output.json", "w") as outfile:
    json.dump(rev_dict, outfile)

