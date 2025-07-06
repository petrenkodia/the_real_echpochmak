# Декоратор timer
# Измеряет время выполнения функции
# Выводит результат в формате: "Функция {название} выполнилась за {время} секунд"
# Должен сохранять оригинальное имя и документацию функции

import time

# делала с тобой по видео, непонятно зачем тут вообще wrapper
def timer(func):
    def wrapper(*args):
        st = time.time()
        result = func(*args)
        print(f"Функция {func.__name__} выполнилась за {time.time() - st} сек.")
        return result

    wrapper.__name__ = func.__name__  # Вручную копируем имя
    wrapper.__doc__ = func.__doc__  # и документацию (по совету нейронки, чтобы не терять инфу об ориг. функции)

    return wrapper

@timer
def calc(*numbers):
    return sum(numbers)

print(calc(1, 2, 3)) # У тебя тут выдавал ошибку, пофиксила, но без range. Почему-то долго делает - 3-4 сек((

@timer
def say_hello():
    time.sleep(0.5)
    print("Привет!")
say_hello()

# Декоратор logger
# Логирует вызов функции с аргументами и результат
# Выводит информацию о входящих аргументах и возвращаемом значении
# При ошибке в функции логирует исключение

"""Логгирует (от англ. log) — означает записывать информацию о работе программы (логи) в специальный файл, 
консоль или систему мониторинга для последующего анализа."""

def logger(func):
    def wrapper(*args, **kwargs):
        # Логируем вызов функции с аргументами
        print(f"Вызов функции {func.__name__} с аргументами:")
        if args:
            print(f" - Позиционные: {args}")
        if kwargs:
            print(f" - Именованные: {kwargs}")

        # Выполняем функцию, чтобы вывести результат
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула: {result}")

        return result

    # Нейронка говорит, что надо копировать метаданные - вручную или через wraps (модуль какой-то)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__

    return wrapper # вот тут () не нужны!!!

@logger
def add(a, b):
    """Складывает два числа"""
    return a + b

add(3, 5)
print(f"// Функция {add.__name__} {add.__doc__}. Она определена в модуле {add.__module__[2:6]}") # вот зачем wraps

@logger
def compl(name, dobroe_slovo="дракончик"):
    return f'"{name} - {dobroe_slovo}! :)"'

compl(name="Руслан", dobroe_slovo="cолнышко")
compl(name="Диана")

# Декоратор validate_type
# Принимает ожидаемые типы аргументов
# Проверяет типы всех переданных аргументов
# Выбрасывает TypeError при несоответствии типов



def validate_type(*exp_types):  # создаёт декоратор, принимая ожидаемые типы арг. для проверки

    def decorator(func):  # Вот я не понимаю, ну зачем же так сложно реализованы декораторы, ппц
        def wrapper(*args):
            for i in range(len(args)): # по кол-ву арг-ов или типов
                if not isinstance(args[i], exp_types[i]):
                    raise TypeError(f"Аргумент {i + 1} должен быть {exp_types[i].__name__}, а получен {type(args[i]).__name__}")
            result = func(*args)
            return result
        return wrapper
    return decorator

# Пример использования
@validate_type(int, float)
def sum_numbers(a, b):
    return a + b

print(sum_numbers(2, 3.5))
print(sum_numbers(2, "3.5"))
