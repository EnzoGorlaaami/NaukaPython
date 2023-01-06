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
    #town = input('Podaj Miasto: ')
    line = input('Podaj Miasto i opady: ')
    if line == "":
        print(weather)
        break
    town, precipitation = line.split()# 'Bosotn 12' -> [Boston, 12]
    # team = line[0]
    # precipitation = line[1]
    precipitation = int(precipitation)

    #precipitation = int(input('Podaj opady dla danego miasta: '))
    if weather.get(town) is None:
        weather[town] = precipitation
        print(f'Dodano {town} z iloscia opadow {precipitation}.')
    else:
        weather[town] += precipitation
        print(f'Dodano ilosc opadow {precipitation} do miasta {town}.')


