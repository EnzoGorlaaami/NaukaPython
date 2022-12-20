#Pamiętasz program służący do wyliczania BMI? Trochę go ulepszymy.
#Od teraz program powinien klasyfikować obliczoną wartość BMI konkretnej kategorii:
#niedowaga / waga normalna / lekka nadwaga / nadwaga.
# Dodatkowo w przypadku nadwagi chcemy sprawdzić, czy mamy do czynienia z otyłością.

print("Szybki kalkulator BMI")

wzrost = int(input("Podaj swój wzrost w cm: "))
waga = float(input("Podaj swoją wagę do jednego miejsca po przecinku w kg: "))

wzrost_kwadart = wzrost ** 2
bmi = waga * 10000 / wzrost_kwadart

print("Twoje BMI to: ", round(bmi, 3))

if bmi < 18.5:
    print('Masz niedowagę! ')
elif 18.5 <= bmi < 24:
    print('Masz normalną wagę ')
elif 24 <= bmi < 26.5:
    print('Masz lekką nadwagę! ')
elif 26.5 <= bmi < 30:
    print('Masz nadwagę! ')
elif 30 <= bmi < 35:
    print('Masz nadwagę i otyłość I stopnia! ')
elif 35 <= bmi < 40:
    print('Masz nadwagę i otyłość II stopnia! ')
else:
    print('Masz nadwagę i otyłość III stopnia! ')