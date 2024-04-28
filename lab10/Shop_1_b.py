# -*- coding: utf-8 -*-
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print(f"Магазин {self.shop_name} - це {self.store_type}")

    def open_shop(self):
        print(f"Магазин {self.shop_name} відкритий")


# Створення трьох різних екземплярів класу Shop
store1 = Shop("Електроніка Онлайн", "онлайн-магазин")
store2 = Shop("Книжковий Світ", "онлайн-книгарня")
store3 = Shop("Одяг для спорту", "онлайн-бутік")

# Виклик метода describe_shop() для кожного екземпляру
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()
