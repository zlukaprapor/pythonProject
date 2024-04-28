# -*- coding: utf-8 -*-
class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"Магазин {self.shop_name} - це {self.store_type}.")
        print(f"Кількість товарних одиниць у магазині: {self.number_of_units}")

    def open_shop(self):
        print(f"Магазин {self.shop_name} відкритий.")


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None, number_of_units=0):
        super().__init__(shop_name, store_type, number_of_units)
        if discount_products is None:
            discount_products = []
        self.discount_products = discount_products

    def get_discounts_products(self):
        print(f"Список товарів зі знижкою у магазині {self.shop_name}:")
        for product in self.discount_products:
            print(product)


# Створення екземпляру класу Discount
store_discount = Discount("Електроніка Онлайн", "онлайн-магазин", ["Смартфон", "Навушники", "Планшет"])

# Виклик методу get_discounts_products для виведення списку товарів зі знижкою
store_discount.get_discounts_products()
