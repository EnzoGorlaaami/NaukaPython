# Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy: Manager oraz Order.
# W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia,
# a wartością jego ilość na stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.
#
# Funkcjonalność programu to:
# - dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt, którego id znajduje się już w słowniku,
# to nie będziemy dodawali nowej pary do dicta, ale zwiększali ilość danego obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
# - usuwanie o 1 zamówienia ze słownika o określonym id
#
# Podpowiedź:
# Pseudokod slownika:
# # self.orders = {obiekt1 : jego_ilosc} ok
#
# Sprzedawanie produktu:
#
# def sell(self, id_to_sell):
#     for order in self.orders:
#         if order.id == id_to_sell:
#            self.orders[order] -= 1

class Order:
    def __init__(self, idx, name, price):
        self.idx = idx
        self.name = name
        self.price = price


    def printer_(self):
        print(f'ID: {self.idx}, Name: {self.name}, Price: {self.price}$. ')


class Manager:
    def __init__(self):
        self.orders: dict[Order, int] = {}

    def add_order(self, new_order, quantity):
        if len(self.orders) == 0:
            self.orders.update({new_order: quantity})
            return
        for order in list(self.orders):
            if order.idx == new_order.idx:
                self.orders[order] += quantity
                return
        self.orders.update({new_order : quantity})


    def sell(self, id_to_sell):
        for order in self.orders:
            if order.idx == id_to_sell:
               self.orders[order] -= 1


    def printer_(self):
        for orders in self.orders:
            Order.printer_(orders)
            print(f'Quantity: {self.orders[orders]}')

def menu():
    man = Manager()
    # order = Order(1, 'deska', 50)
    # order_1 = Order(2, 'telefon', 99)
    # order_2 = Order(1, 'deska', 50)
    # man.add_order(order, 3)
    # man.add_order(order_1, 2)
    # man.add_order(order_2, 1)
    # print(man.orders)
    menu = 'Menu:\n1: List od orders\n2: Add order\n3: Sell order\n4: Exit'
    print(menu)
    user_input = int(input('What You want to do?: '))
    while True:
        if user_input == 1:
            man.printer_()
            user_input = int(input('What You want to do?: '))
        elif user_input == 2:
            # idx = int(input('Set id of order: '))
            # name = input('Set name of order: ')
            # price = int(input('Set price of order: '))
            # quantity = int(input('Set quantity of order: '))
            # man.add_order(Order(idx, name, price), quantity)
            # user_input = int(input('What You want to do?: '))

            # Trzeba wrzucic do add_order
        elif user_input == 3:
            id_to_sell = int(input('Set ID Product to sell: '))
            man.sell(id_to_sell)
            user_input = int(input('What You want to do?: '))
        elif user_input == 4:
            print('See You next time. ')
            break
        else:
            print('Wrong choice! ')
            user_input = int(input('What You want to do?: '))



def main():
    menu()


if __name__ == "__main__":
    main()
