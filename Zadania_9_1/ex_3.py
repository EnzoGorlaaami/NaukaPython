# Mając poniższy słownik:
a = {"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
# dokonaj jego odwrócenia, tzn. niech wartości staną się kluczami, a klucze wartościami.
# Dla powyższego przykładu poprawnym wynikiem będzie:
#{3 : ‘a’, 1 : ‘b’, 10 : ‘c’, 15 : ‘d’, 20 : ‘e’}

#b = list(a.keys())
#c = list(a.values())
d = {}


for key, value in a.items():
    d[value] = key


# for i in range(len(c)):
#     d.update({c[i]: b[i]})
a
print(d)