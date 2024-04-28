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

    def set_number_of_units(self, new_number):
        self.number_of_units = new_number
        print(f"Кількість товарних одиниць було оновлено: {self.number_of_units}")

    def increment_number_of_units(self, increment):
        self.number_of_units += increment
        print(f"Кількість товарних одиниць збільшено на {increment}.")
        print(f"Поточна кількість товарних одиниць: {self.number_of_units}")


# Створення екземпляру класу Shop з атрибутом number_of_units за замовчуванням
store = Shop("Електроніка Онлайн", "онлайн-магазин")

# Виведення початкової кількості товарних одиниць
print("Початкова кількість товарних одиниць:")
store.describe_shop()

# Виклик методу set_number_of_units() для встановлення нової кількості товарних одиниць
store.set_number_of_units(50)

# Виклик методу increment_number_of_units() для збільшення кількості товарних одиниць
store.increment_number_of_units(30)
