from binascii import unhexlify

gif_hex_string = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
gif = unhexlify(gif_hex_string)

if gif[:6] == b'GIF89a':
    print("Файл формату GIF є коректним.")
else:
    print("Файл формату GIF не є коректним.")

width = int.from_bytes(gif[6:8], byteorder='little')
height = int.from_bytes(gif[8:10], byteorder='little')
print("Ширина GIF-файлу:", width)
print("Висота GIF-файлу:", height)

if width == 1 and height == 1:
    print("Ширина та висота GIF-файлу рівні 1.")
else:
    print("Ширина та висота GIF-файлу не рівні 1.")
