# Program ma tworzyć rachunek za prestiżową kolację w restauracji dla poszczególnych osób.
#
# Dla przykładowej listy:

bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

# Wynikiem ma być słownik w postaci:
# {
# ‘Tom’ : {‘potrawy’ : [‘Calamari’, ‘American Hot’, ‘Chocolate Fudge Cake’], ‘cena’ : 21.95},
# ‘Clare’ : {‘potrawy : [‘Bruschetta Originale‘, ‘Fiorentina’, ‘Tiramisu’], ‘cena’ : 20.90},
# …
# }
clients = {}
price_all = {}
for i in range(len(bill_items)):
    dishes = []
    price = 0
    if clients.get((bill_items[i])[0], 1) == 1:
        price += float((bill_items[i])[2])
        dishes.append((bill_items[i])[1])
        clients[(bill_items[i])[0]] = dishes
        price_all[(bill_items[i])[0]] = price
    else:
        price += float((bill_items[i])[2])
        dishes.append((bill_items[i])[1])
        clients[(bill_items[i])[0]] = clients[(bill_items[i])[0]] + dishes
        price_all[(bill_items[i])[0]] = price_all[(bill_items[i])[0]] + price

bill = {}
customers = clients.keys()
for name in customers:
    bill.update({name : {'dishes' : clients[name], 'cena' : price_all[name]}})

print(bill)