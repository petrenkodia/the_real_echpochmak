# Функция build_url
# Обязательный аргумент base_url
# Произвольные параметры запроса через **params
# Правильно кодирует специальные символы в параметрах
# Возвращает готовый URL с параметрами

def build_url(base_url, **params):
    if params:
        description = (f'{k}={v}' for k, v in params.items())
        return f"https://{base_url}/{"&".join(description)}"
    return f"https://{base_url}"

print(build_url("diana.com", page=2, list=4))

# Функция format_table
# Обязательный аргумент data - список списков или словарей
# Именованные параметры: headers (заголовки), align (выравнивание)
# Дополнительные опции через **formatting_options
# Возвращает отформатированную таблицу в виде строки

def format_table(data, headers, align="left", **formatting_options):
    return None
data = [
    ["Руслан", "cпасибо, что проверяешь домашки"],
    ["Диана", "эту задачу не смогла решить("] # Очень сложна :(((
]
print(format_table(data, headers=["Имя", "Сообщение"], align="right"))

# Функция log_message
# Обязательный аргумент message
# Именованный параметр level (по умолчанию "INFO")
# Именованный параметр timestamp (по умолчанию True) - добавлять ли время
# Дополнительная информация через **details
# Возвращает отформатированную строку лога

import datetime
# Делала с тобой по видео, добавила время, не понимаю только зачем это применяется
def log_message(message, level="INFO", timestamp : bool = True, **details):

    conct_det = ''
    for k, v in details.items():
        conct_det = conct_det + ", " + f"{k}={v}"

    if timestamp:
        return f'[{level}] {datetime.datetime.now().strftime("%H:%M")} {message}{conct_det}'
    else:
        return f'[{level}] {message}{conct_det}'

lm = log_message("Мяф", level="High", timestamp = True, cat="кот")
print(lm)

# Функция create_config
# Принимает произвольные настройки через **settings
# Именованный параметр prefix (по умолчанию "config_") для добавления к ключам
# Именованный параметр validate (по умолчанию True) для проверки настроек // Не понимаю что проверять (?)
# Возвращает словарь конфигурации

def create_config(prefix="config_", validate=True, **settings):
    slovar = {}

    for k, v in settings.items():
        slovar[prefix+str(k)] = v

    if validate: # типо пасхалка
        for v in slovar.values():
            if v == 42:
                return "Вы нашли ответ на главный вопрос вопрос жизни, вселенной и всего такого!"

    return slovar
print(create_config(prefix="smth_", validate=False, config=42, name="Диана"))
