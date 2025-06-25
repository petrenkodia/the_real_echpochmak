# Функция process_data
"""Первый аргумент data - список данных для обработки
Принимает произвольное количество операций через *operations
Поддерживаемые операции: "sort", "unique", "reverse", "filter_positive", "double"
Именованный параметр reverse (по умолчанию False) для обратной сортировки
Дополнительные параметры через **options могут включать min_value, max_value для фильтрации
Применяет операции в порядке их указания
Возвращает обработанный список"""

def process_data(data, *operations, reverse=False, **options):
    result = data.copy() # не меняем входные данные

# Сначала фильтруем (если в конце заданы опции мин/макс)
    if 'min_value' in options:
        result = [x for x in result if x >= options['min_value']]
    if 'max_value' in options:
        result = [x for x in result if x <= options['max_value']]

# Потом операции в порядке указания
    for operation in operations:
        if operation == "sort":
            result.sort(reverse=reverse) # менованный параметр метода sort: сортировка по убыванию
        elif operation == "unique":
            result = list(set(result))
        elif operation == "reverse": # просто операция "разворот"
            result = result[::-1]
        elif operation == "filter_positive":
            result = [x for x in result if x > 0]
        elif operation == "double":
            result = [x * 2 for x in result]

    return result

data = [3, 3, 1, 4, 5, 9, -2]
print(process_data(data, "filter_positive", "sort", "unique"))
print(process_data(data, "sort", "double", max_value = 8, min_value = 3)) # УРА, работает!
print(process_data(data, "sort", reverse=True)) # сортировка по убыванию (с именованным параметром операции)
print(process_data(data, "sort", "reverse")) # сортировка, а потом - разворот
print(process_data(data, "reverse")) # просто разворот

# Функция create_report
"""Обязательный аргумент title - заголовок отчета
Произвольное количество разделов через *sections
Именованные параметры: author (по умолчанию "Система"), format (по умолчанию "text")
Дополнительные метаданные через **metadata
Если format="text": возвращает простой текстовый отчет
Если format="html": оборачивает разделы в HTML теги
Добавляет в отчет дату создания и все переданные метаданные"""

# Функция send_notification
"""Обязательные аргументы: recipient (получатель) и message (текст)
Произвольное количество дополнительных получателей через *cc_recipients
Именованный параметр urgent (по умолчанию False)
Именованный параметр delivery_method (по умолчанию "email")
Дополнительные опции через **options (subject, retry_count, etc.)
Возвращает словарь с информацией об отправке, включая количество получателей и статус"""