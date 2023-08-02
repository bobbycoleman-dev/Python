import uuid


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4()

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price + (self.price * percent_change)
        else:
            self.price = self.price - (self.price * percent_change)

    def print_info(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nPrice: ${self.price}\n")
