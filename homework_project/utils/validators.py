# Функция validate_email
# Проверяет корректность email адреса
# Должен содержать @ и точку в домене
# Проверяет базовую структуру email

def validate_email (email):
    if "@" not in email or len(email.split("@")) > 2:
        print(f"Ошибка в '{email}' - Одна собака в одни руки!")
        return False
    domen = email.split("@")[1]
    if "." not in domen:
        print(f"Ошибка в '{email}' - Домен без точки, как хуй без дрочки!") # сори, я сама шутку придумала, не могла не поделиться
        return False
    zapret = [" ", "?", "%"] #
    for symb in zapret:
        if symb in email:
            print(f"Ошибка в '{email}' - Символ {symb} надо убрать")
            return False
    return True
print(validate_email("abc@dd.ru"))
print(validate_email("abc@dd@.ru"))
print(validate_email(".abc@dd,ru"))
print(validate_email("abc@dd.%ru"))

# Функция validate_phone
# Проверяет российские номера телефонов
# Поддерживает разные форматы: +7, 8, 7
# Проверяет количество цифр

def validate_phone(num):
    znaki_sudby = ["+", "(", ")", "-", " "]
    chisla_is_cosmosa = [str(i) for i in range(10)]
    kolvo = 0
    if num[0] != "7" and not num.startswith('8') and num[0:2] != "+7":
        print(f"Ошибка в '{num}'. \n- Я Руусскииий!\n- нет.")
        return False
    for elem in num:
        if elem not in chisla_is_cosmosa and elem not in znaki_sudby:
            print(f"Ошибка в '{num}'. '{elem}' тут лишний)")
            return False
        if elem in chisla_is_cosmosa:
            kolvo += 1
    if kolvo != 11:
        print(f"Ошибка в '{num}'. Цифр должно быть 11, а тут '{kolvo}')")
        return False
    print(f"Номер '{num}' зачетный!:)")
    return True

print(validate_phone("8 (921) 422-64-93"))
print(validate_phone("+7 (921) 422-64-93"))
print(validate_phone("-7 (921) 422-64-93"))
print(validate_phone("9 (921) 422-64-93"))
print(validate_phone("+7 (92%) 422-64-93"))
print(validate_phone("+7 (91) 422-64-93"))

# Функция validate_data
# Принимает данные для валидации
# Произвольное количество функций-валидаторов через *validators
# Дополнительные параметры через **validation_options
# Возвращает результат валидации и список ошибок

# Валидатор из валидаторов, писос, конечно) Делала с нейронкой, но вроде разобралась

def validate_data(data, *validators, **validation_options):
    is_valid = True
    errors = []

    for validator in validators:
        # Вызываем валидатор, передаем - данные и опции, ожидаем - результат и список ошибок
        result, error_msg = validator(data, **validation_options)
        if not result:
            is_valid = False
            errors.append(error_msg)

    return is_valid, errors

# Делаем парочку простых валидаторов

def validate_name(data, **kwargs):  # Исправлено *kwargs на **kwargs
    value = data.get('name')  # Добавлены кавычки вокруг name
    if not value:
        return False, "Поле 'name' не должно быть пустым"
    return True, ""

def validate_age(data, min_age=18, **kwargs):  # Исправлено *kwargs на **kwargs
    if data.get('age') is None:
        return False, "Поле 'age' отсутствует"
    if data['age'] >= min_age:
        return True, ""
    return False, f"Возраст должен быть не менее {min_age}"

# Тестовые прогоны:

user = {'name': 'Руслан', 'age': 32, "kotik" : True}
is_valid, errors = validate_data(user, validate_name, validate_age)
print(f"Пользователь '{user['name']}' валидирован: {is_valid}\nОшибки: {errors}")

user2 = {'name': 'Алёша', 'age': 3}
is_valid, errors = validate_data(user2, validate_name, validate_age)
print(f"Пользователь '{user2['name']}' валидирован: {is_valid}\nОшибки: {errors}")

anon = {'age': 10}
is_valid, errors = validate_data(anon, validate_name, validate_age, min_age=9) # передаю новый мин. возраст
print(f"Пользователь 'anon' валидирован: {is_valid}\nОшибки: {errors}")
