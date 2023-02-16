# W załączeniu znajduje się plik data.json. Przechowuje on informacje o różnych pakietach informacji.
# Twoim zadaniem jest napisanie skryptu, który będzie odczytywał taki pliku i
# drukował poniższy komunikat zawierający informacje o każdym z pakietów:
#
#
# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150
import json

print("Interface Status ")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
with open("data.json", "r") as plik:
    data = json.load(plik)
    records = data['imdata']

for record in records:
    dn = record['l1PhysIf']['attributes']['dn']
    descr = record['l1PhysIf']['attributes']['descr']
    speed = record['l1PhysIf']['attributes']['speed']
    mtu = record['l1PhysIf']['attributes']['mtu']
    print(f"| {dn:<50} | {descr:<20} | {speed:<6} | {mtu:<6} | ")
    #print("| %47s | %18s | %5s |  %4s |" % (dn, descr, speed, mtu))

    # print("| %50s | %20s | %6s |  %6s |" % str(dn), str(descr), str(speed), str(mtu))
    # print(f"{dn:}{descr: >20}{speed: <20}{mtu: <20}")


# for first in records:
#     for second in first:
#         third = first.get(second)
#         for atr in third:
#             fourth = third.get(atr)
#             for val in fourth:
#               # print(f"{fourth.get('dn', 'Not Found'): <40} {fourth.get('descr', 'Not Found'): <20} {fourth.get('speed', 'Not Found'): <20}")

                # print(fourth.get('dn', 'Not Found'),"    ", end="")
                # print(fourth.get('descr', 'Not Found'),"    ", end="")
                # print(fourth.get('speed', 'Not Found'),"    ", end="")
                # print(fourth.get('mtu', 'Not Found'))