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


# Створення екземпляру класу Shop з атрибутом number_of_units за замовчуванням
store = Shop("Електроніка Онлайн", "онлайн-магазин")

# Виведення значення атрибута number_of_units
print("Початкова кількість товарних одиниць:")
store.describe_shop()

# Зміна значення атрибута number_of_units та виведення знову
store.number_of_units = 100
print("\nОновлена кількість товарних одиниць:")
store.describe_shop()
