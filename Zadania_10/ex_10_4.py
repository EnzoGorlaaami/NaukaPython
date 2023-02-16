# 10.4
# Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka),
# złożonej z pikseli tej samej jasności.

def najdluzsza_linia():
    baza = []
    ilosc_wystapien = {}
    with open("dane.txt", "r") as plik:
        for linie in plik:
            baza.append(linie.split())
        for listy in baza:
            for wartosci in range(0, 320):
                if not ilosc_wystapien.get(listy[wartosci]):
                    ilosc_wystapien[listy[wartosci]] = 1
                    # ilosc_wystapien.update({listy[wartosci] : 1})
                else:
                    ilosc_wystapien[listy[wartosci]] += 1





    return ilosc_wystapien






print(najdluzsza_linia())