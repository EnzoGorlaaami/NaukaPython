# Wyobraź sobie, że jesteś pogodynką i robisz zestawienie opadów deszczu na dany miesiąc.
# Problem polega jednak na tym, że dane miasta wraz z opadami są nieuporządkowane oraz użytkownik
# może wpisywać nieskończenie wiele par: miasto oraz opad aż do momentu podania pustej linii.
# Twoim zadaniem jest zinterpretowanie podanych danych wejściowych i podać wynik na wzór poniższego przykładu.
#
# Wejście:
# Boston 12
# Londyn 10
# Boston 12
# [pusta linia]
#
# Wyjście:
# Boston : 24
# Londyn : 10

weather = {}

while True:
    town = input('Podaj Miasto: ')
    if town != "":
        precipitation = int(input('Podaj opady dla danego miasta: '))
        if weather.get(town, 1) == 1:
            weather[town] = precipitation
            print(f'Dodano {town} z iloscia opadow {precipitation}.')
        else:
            weather[town] = weather[town] + precipitation
            print(f'Dodano ilosc opadow {precipitation} do miasta {town}.')
    else:
        print(weather)
        break

