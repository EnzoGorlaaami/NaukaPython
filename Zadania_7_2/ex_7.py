# Napisz program, który scali ze sobą dwa dowolne słowniki.
# Mając do dyspozycji następujące słowniki:

lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor', 7: 'Cokolwiek'}

# Otrzymamy:
# {1: 'Rahima', 2: 'Alishba', 3: 'Fizza', 4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
#
# Zwróć uwagę na to, że słowniki mogą być różnej długości.

both = dict(lovers | friends)

print(both)