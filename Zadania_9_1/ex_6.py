# Wyboraź sobie, że otrzymałeś z API następujące dane:
#
a = {
    'data' : [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, '120'],
        'analysis_2': [10, 100, 'test', 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}
#
# Twoim zadaniem jest wyłuskanie spod każdego klucza w powyższym słowniku tylko tych danych,
# które są typu str i wyświetlić je na ekranie.

only_string = []
for keys in a:
    value_list = a[keys]
    if isinstance(value_list, list):
        for i in range(len(value_list)):
            if isinstance(value_list[i], str):
                only_string.append(value_list[i])
            elif isinstance(value_list[i], list):
                x = value_list[i]
                for j in range(len(x)):
                    if isinstance(x[j], str):
                        only_string.append(x[j])
    elif isinstance(value_list, dict):
        y = list(value_list.keys())
        for i in range(len(y)):
            z = value_list[y[i]]
            if isinstance(z, list):
                for j in range(len(z)):
                    if isinstance(z[j], str):
                        only_string.append(z[j])

print(only_string)