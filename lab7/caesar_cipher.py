def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Визначаємо зсув для великих і малих літер
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            # Зсув у межах алфавіту
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            # Якщо символ не є літерою, додаємо його незмінним
            shifted_char = char
        encrypted_message += shifted_char
    return encrypted_message