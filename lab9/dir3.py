# -*- coding: utf-8 -*-
import glob

pattern = "*.py"  # шаблон для пошуку файлів з розширенням .txt
matching_files = glob.glob(pattern)
print("Знайдені файли за шаблоном {}: {}".format(pattern, matching_files))
