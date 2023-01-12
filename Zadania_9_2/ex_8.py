# Napisz funkcję, ktora przyjmować będzie godzinę i minutę (wykorzystaj keyword arguments)
# i powinna ona zwrócić kąt (podany w stopniach) między wskazówką godzinową a minutową w tym podanym czasie.

# Podpowiedź:
#Możesz wykorzystać funkcję abs w celu obliczania wartości bezwzględnej, np.
#print(abs(-5)) # 5

def pointer_angle(hour, minute):
    hour_angle = hour * 30
    minute_angle = minute * 6
    return f'Kat miedzy wskazowkami to {abs(hour_angle - minute_angle)} stopni.'


input_hour = int(input('Podaj godzine: '))
input_minute = int(input('Podaj minute: '))
print(pointer_angle(input_hour, input_minute))
