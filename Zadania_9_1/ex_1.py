#Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.


a = [1, "bgfds"]
b = ["gfslssss", 1, 134]

if set(a).intersection(set(b)):
    print("Zbiory maja przynajmniej jedna wspolna czesc. ")
else:
    print("Zbiory nie maja wspolnej czesci. ")