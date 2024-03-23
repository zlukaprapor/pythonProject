def get_square_color(position):
    column, row = position[0], int(position[1])
    # Перевірка на парність рядка і стовпчика
    if (ord(column) - ord('a') + row) % 2 == 0:
        return "black"
    else:
        return "white"