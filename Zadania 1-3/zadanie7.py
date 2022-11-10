print("Szybki kalkulator BMI")

wzrost = int(input("Podaj swój wzrost w cm: "))
waga = float(input("Podaj swoją wagę do jednego miejsca po przecinku w kg: "))


# wzrostKwadrat = wzrost ** 2
#
# bmi = str(waga * 10000 / wzrostKwadrat)
# bmi3miejsca = str(bmi)

wzrostKwadrat = wzrost ** 2
bmi = waga * 10000 / wzrostKwadrat

print("Twoje BMI to: ", round(bmi, 3))