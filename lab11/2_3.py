from binascii import unhexlify

# Відкриваємо файл з шістнадцятковим рядком GIF-зображення
gif_hex_string = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
gif = unhexlify(gif_hex_string)

# Отримуємо ширину та висоту зображення з файлу GIF
width = int.from_bytes(gif[6:8], byteorder='little')
height = int.from_bytes(gif[8:10], byteorder='little')

# Записуємо інформацію про ширину та висоту у текстовий файл
with open('validate.txt', 'w', encoding='utf-8') as file:
    file.write("Ширина зображення: {}\n".format(width))
    file.write("Висота зображення: {}\n".format(height))

print("Інформацію про ширину та висоту зображення записано у файл 'validate.txt'.")
