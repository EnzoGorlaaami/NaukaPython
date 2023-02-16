# Masz do dyspozycji plik przyklad.txt o następującej zawartości:
# Jak czarne ptaki, lecąc lecąc w wyższą nieba nieba stronę,
# Coraz się zgromadzały. Ledwie słońce zbiegło zbiegło
# Z południa, już już ich stado pół pół niebios obiegło
#
# Jak możesz zauważyć, gdzieniegdzie wkradły się powtórzenia słów. Zmodyfikuj i zapisz nowy plik tak, aby się ich pozbyć.

# przyklad = ["Jak czarne ptaki, lecąc lecąc w wyższą nieba nieba stronę, "
#             "Coraz się zgromadzały. Ledwie słońce zbiegło zbiegło "
#             "Z południa, już już ich stado pół pół niebios obiegło"]
#
# czysty_tekst = []
# def tekst_bez_powtorzen():
#
#     with open("przyklad7.txt", "w+", encoding="utf-8") as plik:
#         plik.writelines(przyklad)
#         plik.seek(0)
#         for linie in plik.readlines():
#             for slowa in linie.split():
#                 if czysty_tekst.count(slowa) == 0:
#                     czysty_tekst.append(slowa)
#     return czysty_tekst
#
# def plik_z_czystym_tekstem():
#     tekst_bez_powtorzen()
#     with open("przyklad7.txt", "w", encoding="utf-8") as plik:
#         for slowa in czysty_tekst:
#             plik.write(slowa)
#             plik.write(" ")
#     with open("przyklad7.txt", "r", encoding="utf-8") as plik:
#         return plik.readlines()
#
# def main():
#     print(f'Nasz plik po wycięciu powtórzeń: '
#           f'{plik_z_czystym_tekstem()}')

def main():
    with open('przyklad_txt.txt', "r", encoding='UTF-8') as file:
        contents = file.read()

    words = contents.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    new_contents = " ".join(unique_words)

    with open('new_przyklad.txt', "w", encoding='UTF-8') as file:
        file.write(new_contents)


if __name__ == "__main__":
    main()
