""" Различные способы импорта """

# Импорт отдельных функций
from core.basic_functions import create_profile, calculate_discount
print(create_profile("Ди", 28, "petrenkodia@ya.ru"))
print(calculate_discount(42, discount_percent=11, membership="vip"))

# Импорт целых модулей (БЕЗ FROM, добавится оставшаяся функция, но вызов через образение (as)
import core.basic_functions as baza
print(baza.format_name("Руслан", "Большаков", "Батькович", format_style="reverse"))

# Импорт с алиасами (кроме последней)
from data.processors import sum_numbers as sn, find_extremes as fe, create_sentence as cs, calculate_statistics
print(sn(1, 2, 'a'))
print(fe(5, -1, 10, return_type="min"))
print(cs("hi", "bitches", end_mark="!", separator=", "))
print(calculate_statistics(1, 11, 2, 16, 16, option="Эчпочмак"))

# Импорт из подпакетов (тут и так все в подпапках, получается уже сделано)

""" Демонстрация работы с аргументами """

# Примеры вызова функций только с позиционными аргументами
print(sn(1, 2, 3))

# Примеры с именованными аргументами
print(calculate_discount(price=121, discount_percent=11, membership="премиум"))

# Примеры со смешанным использованием
print(baza.format_name("Дианочка", "Петреночка", format_style="full"))

# Демонстрацию keyword-only и positional-only аргументов
### В базовых функциях были знаки "*" и "/":

### Все аргументы после "*" должны передаваться по имени (т.е. discount_percent = 15, а не просто 15)
print(calculate_discount(121, discount_percent=11, membership="vip"))

### Все аргументы до "/" только позиционные (передаются строго по порядку, нельзя указать имя аргумента)! После - пофиг
print(baza.format_name("Руслан", "Большаков"))

# Использование *args и **kwargs
from core.advanced_functions import send_notification as s_n

sms = s_n(
    "Диана",
    '"В пятницу 18.07 идем тусить в Севкабель!"',
    "Руслан", # *args
    "Соня КряГок",
    "Аннушка",
    urgent="Супер-важно",
    delivery_method="Телеграмм",
    tema="Ищу компанию", # **kwargs
    sloznost_otkaza=19,
    parol="Эчпочмак"
)

for key, value in sms.items():
    print(f"{key}: {value}")

# Распаковку списков и словарей
### Не поняла, что имеется ввиду, нейронка вот что дала в пример (пусть будет перед глазами):

def flexible(*args, **kwargs):
    print("Позиционные:", *args)
    print("Именованные:", kwargs) # вот тут распаковать ** не вышло, выдал ошибку, надо через key\value как выше
# Пример комбинированной распаковки:
args_list = [1, 2, 3]
kwargs_dict = {'x': 10, 'y': 20}
flexible(*args_list, **kwargs_dict)

### Теперь задание
profile_data = {'name': 'Диана', 'age': 28, 'city': 'Тольятти'}
print(create_profile(**profile_data)) # передали распакованный словарь

numbers_list = [1, 2, 3, "a", 4.5]
print(sn(*numbers_list)) # распаковка списка в аргументы

""" Работа декораторов """

# Применение декораторов к функциям
# Демонстрацию их эффектов

from utils.decorators import timer, logger

@timer
@logger # применится первым
def add(a, b):
    return a + b
print(" --- Декораторы: --- ")
add(3, 5)

""" Обработку конфигурации не делала, т.к. мы не изучали настройки """
