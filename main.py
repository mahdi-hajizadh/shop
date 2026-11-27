from engine import Cart, Product, Shop


def main():
    products = [
        Product(1, "Laptop", 1200, 5),
        Product(2, "Mouse", 25, 20),
        Product(3, "Keyboard", 75, 10),
    ]
    shop = Shop(products, Cart())
    shop.show_products()
    shop.add_to_cart(1, 2)
    shop.add_to_cart(2, 3)
    shop.checkout("Ali", 10)
    shop.show_orders()


if __name__ == "__main__":
    main()
