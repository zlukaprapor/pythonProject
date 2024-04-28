# -*- coding: utf-8 -*-
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print(f"Магазин {self.shop_name} - це {self.store_type}")

    def open_shop(self):
        print(f"Магазин {self.shop_name} відкритий")


# Створення екземпляру класу Shop
store = Shop("Електроніка Онлайн", "онлайн-магазин")

# Виведення атрибутів окремо
print(f"Назва магазину: {store.shop_name}")
print(f"Тип магазину: {store.store_type}")

# Виклик методів
store.describe_shop()
store.open_shop()
