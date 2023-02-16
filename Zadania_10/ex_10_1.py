# 10.1
# Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.

def najjasniejszy_pixel():
    jasny_pixel = []
    baza = []
    with open("dane.txt", "r") as plik:
        for linie in plik:
            baza.append(linie.split())
            for listy in baza:
                listy.sort(reverse=True)
                x = int(listy[0])
            jasny_pixel.append(x)
    jasny_pixel.sort(reverse=True)

    return jasny_pixel[0]


def najciemniejszy_pixel():
    ciemny_pixel = []
    baza = []
    with open("dane.txt", "r") as plik:
        for linie in plik:
            baza.append(linie.split())
            for listy in baza:
                listy.sort()
                x = int(listy[0])
            ciemny_pixel.append(x)
    ciemny_pixel.sort()

    return ciemny_pixel[0]

def main():
    print(f'Najciemniejszy pixel ma wartość: {najciemniejszy_pixel()}, a najjaśniejszy: {najjasniejszy_pixel()}.')

if __name__ == "__main__":
    main()