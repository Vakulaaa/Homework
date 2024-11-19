#
#
# class Item:
#     def __init__(self, name, price, weight, category = "some category"):
#         self.price = price
#         self.category = category
#         self.weight = weight
#         self.name = name
#
#     def __str__(self):
#         return f"Product {self.name}, price: {self.price}, category: {self.category}, weight: {self.weight}"
#
# class Buyer:
#     def __init__(self, name, surname, phone_number):
#         self.name = name
#         self.surname = surname
#         self.phone_number = phone_number
#
#     def __str__(self):
#         return f"""User: {self.name, self.surname}
#                    Phone number: {self.phone_number}"""
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#
#     def add_product(self, item, cnt):
#         if item in self.products:
#             self.products[item] += cnt
#         else:
#             self.products[item] = cnt
#
#     def get_total(self):
#         return sum(cnt for product, cnt in self.products.items())
#
#     def __str__(self):
#         products_info = "\n".join([f"{self.item} - Количество {self.cnt}" for item, cnt in self.products.items()])
#         return (f"{self.user}\nЗаказ:\n {products_info}\n Стоимость: {self.get_total} грн.")
#
#
# user_1 = Buyer(name= "Ivan", surname="Ivanov", phone_number="7896473422")
# product_1 = Item(name = "notebook", price = "12000", category = "notebooks", weight = "3 kg")
# purchase_1 = Purchase(user_1)
# purchase_1.add_product(product_1, 1)
#
