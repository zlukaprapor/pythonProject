# -*- coding: utf-8 -*-

import os

current_directory = os.getcwd()
print("Повний шлях поточного каталогу:", current_directory)

files_in_directory = os.listdir(current_directory)
print("Список файлів у поточному каталозі:", files_in_directory)
