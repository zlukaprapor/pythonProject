# -*- coding: utf-8 -*-

import os

file_path = "dir1.py"  # замініть шлях на потрібний
file_size = os.path.getsize(file_path)
print("Розмір файла у байтах:", file_size)
