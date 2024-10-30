class Order:
    def __init__(self, customer_email):
        self.customer_email = customer_email
        self.products = []
        self.purchased = False

    def add_product(self, product):
        self.products.append(product)
        return self.products

    def get_total_price(self, ):
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        return total_price

    def get_total_quantity_of_products(self, ):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def purchase(self):
        self.purchased = True


class Product:
    def __init__(self, name, unit_price, quantity=1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def get_price(self, ):
        return self.unit_price * self.quantity
