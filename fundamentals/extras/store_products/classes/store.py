class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        for product in new_product:
            self.products.append(product)
        return self

    def sell_product(self, id):
        print("*****SOLD!*****")
        for product in self.products:
            if product.id == id:
                product.print_info()
                self.products.pop(self.products.index(product))
        return self

    def inflation(self, percent_increase):
        print("***Price increase on all products!***\n")
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        print(f"Clearance on all {category} jerky!\n")
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

    def display_product_list(self, category):
        for product in self.products:
            if category == "all":
                product.print_info()
            elif product.category == category:
                product.print_info()
