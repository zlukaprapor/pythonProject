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
