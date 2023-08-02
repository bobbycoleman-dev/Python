from classes.store import Store
from classes.product import Product

# CREATE STORE INSTANCE
store = Store("Bobby's Beef Jerky Emporium")

# CREATE PRODUCTS
beef_jerky1 = Product("Hickory Smoked", 50, "beef")
beef_jerky2 = Product("Teriyaki", 40, "beef")
venison_jerky1 = Product("Korean BBQ", 60, "venison")
venison_jerky2 = Product("Applewood Smoked", 50, "venison")
gator_jerky1 = Product("Jamaican Jerk", 80, "gator")
gator_jerky2 = Product("Louisiana Rub", 70, "gator")

# ADD PRODUCTS TO STORE
store.add_product(
    [
        beef_jerky1,
        beef_jerky2,
        venison_jerky1,
        venison_jerky2,
        gator_jerky1,
        gator_jerky2,
    ]
)

store.display_product_list("all")
store.set_clearance("beef", 0.1)
store.sell_product(beef_jerky1.id)
store.display_product_list("beef")

store.inflation(0.2)
store.sell_product(gator_jerky1.id)
store.display_product_list("all")
