#Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy mają być równe
# ilości wystąpień słowa w tekście.

txt = "Once Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore," \
" While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. " \
"This visitor, I muttered, tapping at my chamber door - Only this, and nothing more. more."

txt = (txt.replace(',', ''))

y = list(txt.split())
result = {}

for word in y:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1

print(result)