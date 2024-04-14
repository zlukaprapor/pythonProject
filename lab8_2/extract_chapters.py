def extract_chapters(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            data = file.read()
            # Декодування байтів у текст, використовуючи правильне кодування (наприклад, cp1252)
            text = data.decode('cp1252')

        chapters = []
        for line in text.split('\n'):
            # Перевірка, чи починається рядок з "CHAPTER" і має формат заголовка
            if line.strip().startswith("CHAPTER"):
                chapters.append(line.strip())

        with open(output_file, 'w', encoding='utf-8') as file:
            for chapter in chapters:
                file.write(chapter + '\n')

        print(f"Успішно знайдено та записано заголовки розділів у файл {output_file}.")
    except FileNotFoundError:
        print("Файл не знайдено.")

input_file = "robinson_crusoe.txt"
output_file = "chapters.txt"

extract_chapters(input_file, output_file)
