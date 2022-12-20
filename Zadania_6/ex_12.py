#Wydrukuj alfabet w porządku naturalnym, czyli od ‘a’ do ‘z’ a następnie odwróconym,
# pisanym wielkimi literami, czyli od ‘Z’ do ‘A’.

#Podpowiedź:
#Skorzystaj z kodów ASCII i konwersji na typ chr.
#
# alphabet_small = []
# alphabet_big = []
#
# for i in range(97, 123):
#     alphabet_small.append(i)
#
# for j in range(0, len(alphabet_small)):
#     print(chr(alphabet_small[j]), end= ' ')
# print()
# for k in range(65, 91):
#     alphabet_big.append(k)
#
# alphabet_big.reverse()
#
# for l in range(0, len(alphabet_big)):
#     print(chr(alphabet_big[l]), end= ' ')


import string

print(string.ascii_lowercase)
print(string.ascii_uppercase[::-1])