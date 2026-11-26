class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        return sum(item.product.price * item.quantity for item in self.items)


class Order:
    def __init__(self, customer, total):
        self._customer = customer
        self._total = total

    @property
    def customer(self):
        return self._customer

    @property
    def total(self):
        return self._total


class Shop:
    def __init__(self, products, cart):
        self.products = {product.pid: product for product in products}
        self.cart = cart
        self.orders = []

    def show_products(self):
        for product in self.products.values():
            print(product.pid, product.name, product.price, product.stock)

    def add_to_cart(self, pid, quantity):
        product = self.products.get(pid)
        if product is None:
            print("Product not found")
            return
        if product.stock < quantity:
            print("Not enough stock")
            return
        self.cart.add(product, quantity)
        print("Added to cart")

    def calculate_total(self):
        return self.cart.calculate_total()

    def checkout(self, customer, discount=0):
        if not self.cart.items:
            print("Cart is empty")
            return
        total = self.calculate_total()
        total -= total * discount / 100
        for item in self.cart.items:
            item.product.stock -= item.quantity
        self.orders.append(Order(customer, total))
        self.cart.items.clear()
        print("Order completed:", total)

    def show_orders(self):
        for order in self.orders:
            print(order.customer, order.total)
