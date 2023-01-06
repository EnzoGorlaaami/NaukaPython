a = [2, 6, 22, 31, -21, 0, 1, 8, 9, 10]

def list_filter(numb_list):
    check_list = []
    if len(numb_list) != 10:
        return "Zla ilosc elementow w liscie"
    else:
        for numb in numb_list:
            if numb <= -10 or numb >= 10:
                check_list.append(numb)

        return f'Liczby dwucyfrowe to: {check_list}. '

print(list_filter(a))