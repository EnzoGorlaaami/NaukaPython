lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2']
#
# Niech program:
# 1 wydrukuje te listy
# 2 wydrukuje pierwszy oraz czwarty element z lista1
# 3 przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
# 4 przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
# 5 doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
# 6 skasuje element o indeksie 2 z lista1
# 7 wyznaczy liczbę elementów lista3
# 8 powiększy lista1 o elementy lista3
# Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.
#1
print(lista1, lista2, lista3)
#2
print(lista1[0], lista1[3])
#3
x =[]
x.append(lista2[1])
lista2.pop(1)
lista2.insert(1, {str(x) : (lista3[1])})
print(lista2)
#4
y = lista3[2]
lista3.pop(2)
lista3.insert(1,{str(y) : input('Podaj dowolną wartość: ')})
print(lista3)
#5
lista1.append('slowo')
print(lista1)
#6
lista1.pop(2)
print(lista1)
#7
print(len(lista3))
#8
lista1.extend(lista3)
print(lista1)