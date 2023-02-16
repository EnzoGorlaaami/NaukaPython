# Odczytaj 4. linię z pliku: test.txt o zawartości:
# line1
# line2
# line3
# line4
# line5
# line6
# line7

txt = ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n', 'line6\n', 'line7\n' ]
def czwarta_linia():
    with open('test.txt', 'w+') as plik:
        plik.writelines(txt)
        plik.seek(0)
        linie = plik.readlines()
    return linie[3]

def main():
    print(f"Czwarta linia pliku test.txt to {str(czwarta_linia())}")


if __name__ == "__main__":
    main()






