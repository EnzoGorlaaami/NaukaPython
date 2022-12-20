# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
#     • korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.

znaki_do_usuniecia = [',', '.', ':', ';', '!', '?']

user_input = str(input('Podaj dowolne zdanie: '))

for i in range(len(znaki_do_usuniecia)):
    user_input.split(znaki_do_usuniecia[i])
    user_input.replace(znaki_do_usuniecia[i], '')
    print(user_input)
