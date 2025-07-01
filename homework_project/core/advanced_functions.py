import datetime

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

def create_report(title, *sections, author="Система", format="text", **metadata):
    report = f"\nЗаголовок: {title}\nАвтор: {author}\nФормат: {format}\n"

    for i, section in enumerate(sections, 1):
        report += f"РАЗДЕЛ {i}: {section}\n"
    if metadata:
        report += " - МЕТАДАННЫЕ - \n"
        for key, value in metadata.items():
            report += f"{key}: {value}\n"
    report += f"Дата: {datetime.datetime.now().strftime("%d-%m-%Y")}"
    if format == "html":
        report = f"<html><body><h1>{title}</h1><pre>{report}</pre></body></html>" # pre - значит с сохранением формата

    return report

report = create_report(
    "Котики",
    "Трехцветные", "Лысенькие", "Мурчащие",
    author="Диана",
    format="html",
    cats="love", mur="murmur"
)
print(f"\n--- Задание 2 ---")
print(report)

# Функция send_notification
"""Обязательные аргументы: recipient (получатель) и message (текст)
Произвольное количество дополнительных получателей через *cc_recipients
Именованный параметр urgent (по умолчанию False)
Именованный параметр delivery_method (по умолчанию "email")
Дополнительные опции через **options (subject, retry_count, etc.)
Возвращает словарь с информацией об отправке, включая количество получателей и статус"""


def send_notification(recipient, message, *cc_recipients, urgent: str | bool = False, delivery_method="email", **options):
    all_recipients = [recipient] + list(cc_recipients)

    return {
        "Получатели": all_recipients,
        "Всего": len(all_recipients),
        "Сообщение": message,
        "Срочность": urgent if urgent else "normal",  # Исправлено здесь
        "Метод": delivery_method,
        **options
    }

pukpuk = send_notification(
    "Диана",
    '"В четверг 03.07 идем в бар!"',
    "Руслан",
    "Соня КряГок",
    urgent="Супер-важно",
    delivery_method="Телеграмм",
    tema="Бар",
    sloznost_otkaza=19
)

print(f"\n--- Задание 3 ---")
for key, value in pukpuk.items():
    print(f"{key}: {value}")
