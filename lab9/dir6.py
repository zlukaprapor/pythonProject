# -*- coding: utf-8 -*-
import time

# Отримання кількості секунд з початку "епохи Unix"
seconds_since_epoch = time.time()

# Переведення секунд у дні та роки
days_since_epoch = seconds_since_epoch / (60 * 60 * 24)
years_since_epoch = days_since_epoch / 365

print("Кількість днів з початку епохи Unix:", int(days_since_epoch))
print("Кількість років з початку епохи Unix:", int(years_since_epoch))
