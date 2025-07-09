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

def write_data(filename, *data, separator="\n", mode="w", **options): # Здесь в options можно передать encoding
    with open(filename, mode, encoding=options.get('encoding', 'utf-8')) as file:
        text = separator.join(str(item) for item in data)
        if mode == "w":
            print("Фаил перезаписан")
            file.write(text) # .write() возвращает количество записанных символов, нет смысла его в return
            return True
        if mode == "a":
            print("Запись сделана")
            text = "\n" + text + separator # Балуюсь
            file.write(text)
            return True
        elif mode == "r":
            print("Фаил прочитан:")
            return file.readlines() # Добавила, чтобы легко проверить, что записали))
    return False

print(write_data("diary.txt", "Дорогой дневник", "мне не подобрать слов", "чтобы описать боль и унижение",
                 "которые я испытал сегодня...", mode="w", separator=", ", encoding="utf-8"))
print(write_data("diary.txt", 1, 2, 3, "Поехали", mode="a", separator=")\n"))
print(write_data("diary.txt", mode="r"))

# Функция process_csv
# Обязательный аргумент filename
# Произвольное количество функций-обработчиков через *processors
# Именованные параметры: delimiter, skip_header, encoding
# Применяет обработчики к каждой строке
# Возвращает обработанные данные

# Тут без нейронки бы не сделала:(
# Сначала создаем файл (с пустыми строками/имена с мал. буквы):

with open('data.csv', 'w', encoding='utf-16') as file: # Сделала utf-16, чтобы в экселе норм отображалось
    file.write("имя,Возраст,Город\n")
    file.write("   \n")
    file.write("диана,28,Тольятти\n")
    file.write(",,\n")
    file.write("руслан,32,Санкт-Петербург\n")

import csv 

def process_csv(filename, *processors, delimiter=',', skip_header=False, encoding='utf-16'):
    result = []
    with open(filename, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter) # читаем по строкам и по разделителю (delimiter)

        if skip_header:
            next(reader)  # пропускаем заголовок

        for row in reader:
            for processor in processors: # применяем все обработчики для каждой строки
                row = processor(row)
            if row: # заморочка от пустых строк, обработчик удаляет пробелы -> пустые не добавятся
                result.append(row)

    return result

# Обработчики:
def remove_empty(row):
    return [item for item in row if item.strip()]

def capitalize_names(row):
    if row:
        row[0] = row[0].capitalize()
    return row

print(process_csv('data.csv', capitalize_names, remove_empty, skip_header=False))
print(process_csv('data.csv', capitalize_names, skip_header=True)) # С пустыми
