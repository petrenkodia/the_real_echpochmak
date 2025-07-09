import statistics

### Функция sum_numbers ###
# Принимает произвольное количество чисел через *numbers
# Если чисел нет, возвращает 0
# Игнорирует значения, которые не являются числами, но выводит предупреждение
# Поддерживает целые и дробные числа

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"ПЕРДУПРЕЖДЕНИЕ: '{num}' не является числом!")
    return total

print(sum_numbers(1, 2, 'a'))

### Функция find_extremes ###
# Принимает произвольное количество значений через *values
# Именованный параметр return_type (по умолчанию "both")
# При "both": возвращает кортеж (минимум, максимум)
# При "min": возвращает только минимум
# При "max": возвращает только максимум
# Если значений нет, возвращает None

def find_extremes(*values, return_type="both"):
    if not values:
        return None
    if return_type == "min":
        return min(values)
    elif return_type == "max":
        return max(values)
    return (min(values), max(values)) # both

print(find_extremes(5, -1, 10, return_type="min"))

### Функция create_sentence ###
# Принимает произвольное количество слов через *words
# Именованный параметр separator (по умолчанию " ")
# Именованный параметр end_mark (по умолчанию ".")
# Именованный параметр capitalize_first (по умолчанию True)
# Объединяет слова через разделитель, добавляет знак препинания
# При необходимости делает первую букву заглавной

def create_sentence(*words, separator=" ", end_mark=".", capitalize_first=True):
    sent = separator.join(words) + end_mark # сначала складывала через for, но нейронка сказала .join лучше
    if capitalize_first:
        sent = sent[0].upper() + sent[1:]
    return sent

print(create_sentence("hi", "bitches", end_mark="!", separator=", "))  # поменяла местами знак и разд-ль, работает)

### Функция calculate_statistics ###
# Принимает произвольное количество чисел через *numbers
# Именованные параметры для выбора статистик: mean, median, mode (все по умолчанию True)
# Дополнительные параметры через **options
# Возвращает словарь с запрошенными статистиками

def calculate_statistics(*numbers, mean=True, median=True, mode=True, **options):
    result = {}
    if numbers:
        if mean:
            result['mean'] = sum(numbers) / len(numbers)
        if median:
            result['median'] = statistics.median(numbers) #result['median'] = sorted(numbers)[len(numbers)//2]
        if mode:
            try: # нейронка предложила доб. искл., т.к. моды может не быть
                result['mode'] = statistics.mode(numbers)
            except statistics.StatisticsError:
                result['mode'] = None
    result.update(options)
    return result

print(calculate_statistics(1, 1, 2, 3, option="Эчпочмак"))
