list_name = []
list_price = []
list_quantity = []
i = 0

class Product:
    name = None
    price = None
    quantity = None

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def add_cart(self):
        name = input('ведите товар')
        list_name.appand(name)
        quantity = input('ведите товар')
        list_quantity.appand(quantity)
        price = input('ведите товар')
        list_price.appand(price)

    def summ(self):
        while i < len(list_price):
            pass

Cart.add_cart()
