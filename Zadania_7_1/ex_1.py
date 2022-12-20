#Utwórz listę składającą się z następujących elementów: 'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'.
#Przekształć tę listę w zbiór i zachowaj pod nową nazwą, a następnie:
#    • policz, ile elementów zawiera oryginalna lista kolorów
#    • policz, ile różnych kolorów zostało użytych
#    • wyświetl każdy z elementów zbioru w oddzielnej linii
#    • dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)
#    • usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)

colors = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski',
          'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

# colors_set = set(['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny',
#                   'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'])
colors_set = set(colors)
print(len(colors))
print(len(colors_set))

colors_clean = list(colors_set)

for i in range(len(colors_clean)):
    print(colors_clean[i])

colors_set.add('burgund')

print(colors_set)

colors_set.remove('czerwony')

print(colors_set)