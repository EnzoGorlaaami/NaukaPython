# Stwórz plik o nazwie przyklad.txt i umieść w nim następujący tekst:
txt = [
"Litwo, Ojczyzno moja! ty jesteś jak zdrowie;\n"
"Ile cię trzeba cenić, ten tylko się dowie,\n"
"Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
]
# Następnie wyświetl z pliku zawartość jego parzystych linii.

plik = open("przyklad.txt", "w", encoding='UTF-8')
plik.writelines(txt)
plik.close()

nowy_plik = open("przyklad.txt", "r")
caly_teskt = nowy_plik.readlines()
#print(caly_teskt)
# for linijnki in caly_teskt:
#     x = caly_teskt.index(linijnki) + 1
#     if x % 2 == 0:
#         print(linijnki)
# print(caly_teskt[1::2])
x = 1
for linijnki in caly_teskt:
    if x % 2 == 0:
        print(linijnki)
    x += 1
nowy_plik.close()