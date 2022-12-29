# Stwórz program, który policzy częstotliwość cyfr w danej liczbie (którą poda użytkownik).
# Przykład:
# Input: 1235555
# Output:
# 1: 1
# 2: 1
# 3: 1
# 5: 4

x = str(input('Podaj dowolną liczbę: '))
numb = {}
for i in x:
    if x.find(str(i)) == 1:
        numb[i] = x.count(str(i))

print(numb)


freaquency = {}
for digit in x:
    if digit not in freaquency:
        freaquency[digit] = 1
    else:
        freaquency[digit] += 1

for digit, count in freaquency.items():
    print(f"{digit}: {count}", end=" ")