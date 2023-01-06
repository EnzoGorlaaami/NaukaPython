# Napisz funkcję, ktora przyjmować będzie godzinę i minutę (wykorzystaj keyword arguments)
# i powinna ona zwrócić kąt (podany w stopniach) między wskazówką godzinową a minutową w tym podanym czasie.

# Podpowiedź:
#Możesz wykorzystać funkcję abs w celu obliczania wartości bezwzględnej, np.
#print(abs(-5)) # 5

def pointer_angle(hour, minute):
    hour = hour * 30
    minute = minute * 6
    return f'Kat miedzy wskazowkami to {abs(hour - minute)} stopni.'

print(pointer_angle(hour=int(input('Podaj godzine: ')),minute=int(input('Podaj minute: '))))