unknown = '\U000057A6'
unknown_bytes = unknown.encode('utf-8')
print(unknown_bytes)
unknown_string = unknown_bytes.decode('utf-8')
print(unknown_string)
print("Рядок unknown_string:", unknown_string)
print("Рядок unknown:", unknown)
print("Чи однакові значення: ", unknown_string == unknown)
