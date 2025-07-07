# Функция read_file
# Обязательный аргумент filename
# Именованный параметр encoding (по умолчанию "utf-8")
# Дополнительные опции через **options (например, strip_lines, skip_empty)
# Обрабатывает ошибки чтения файла, возвращает содержимое файла или список строк (list)

def read_file(filename, encoding="utf-8", **options):
    with open(filename, 'r', encoding=encoding) as file:
        lines = file.readlines() # Читаем по линиям, чтобы дальше делать перебор

        if options.get('strip_lines'):
            lines = [line.strip() for line in lines]

        if options.get('skip_empty'):
            lines = [line for line in lines if line.strip() != ""]

        if options.get('as_list'):
            return lines
        else:
            return '\n'.join(lines)

print(read_file("song.txt", strip_lines=True, skip_empty=True, as_list=True)) # Список отформатир. строк
print(read_file("song.txt", strip_lines=True, skip_empty=True)) # Текстом


# Функция write_data
# Обязательный аргумент filename
# Произвольное количество данных для записи через *data
# Именованный параметр separator (по умолчанию "\n"), mode (по умолчанию "w")
# Дополнительные опции через **options

# Функция process_csv
# Обязательный аргумент filename
# Произвольное количество функций-обработчиков через *processors
# Именованные параметры: delimiter, skip_header, encoding
# Применяет обработчики к каждой строке
# Возвращает обработанные данные
