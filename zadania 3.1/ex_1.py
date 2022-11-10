
user_input = input("Podaj dodwolny wyraz nie krótszy, niż 7 znaków: ")
last_letter = user_input
mid = len(user_input) // 2
if len(user_input) > 7:
    print(user_input)
    print(len(user_input))
    print(f'{user_input[0]}, {user_input[-1]}')
    print(user_input[mid-1:mid+2])
else:
    print("Zła ilosć znaków")
