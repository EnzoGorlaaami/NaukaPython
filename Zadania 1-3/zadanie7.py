print("Szybki kalkulator BMI")

wzrost = int(input("Podaj swój wzrost w cm: "))
waga = float(input("Podaj swoją wagę do jednego miejsca po przecinku w kg: "))


wzrostKwadrat = wzrost ** 2

bmi = str(waga * 10000 / wzrostKwadrat)
bmi3miejsca = str(bmi)

print("Twoje BMI to: ", bmi[:4])