from datetime import datetime

# Реализуйте следующие функции:

# Функция create_profile
# Принимает обязательные аргументы: name (строка) и age (число)
# Принимает необязательные аргументы: email (по умолчанию None) и city (по умолчанию "Москва")
# Добавьте валидацию: проверьте, что возраст положительный и меньше 150
# Если передан email, проверьте что он содержит символ "@"
# Возвращает словарь со всеми переданными данными
# Добавьте к результату поле created_at с текущей датой

def create_profile(name: str, age: int, email: str | None = None, city: str = "Москва"):
    if 0 < age < 150:
    profile = {
        "name": name,
        "age": age,
        "email": email if email and "@" in email else "Не указан",  # Не примет email без "@"
        "city": city,
        "created_at": datetime.now().strftime("%d.%m.%Y")
    }
    else:
        raise ValueError("Возраст должен быть положительным и меньше 150")
    return profile

print(create_profile("Ди", 28))
print(create_profile("Ди", 28, "petrenkodia@ya.ru"))

# Функция calculate_discount
# Первый аргумент price - обязательный позиционный
# Все остальные аргументы должны быть именованными (используйте *) --- ??? распаковка ??? ---
# discount_percent (по умолчанию 10) - размер скидки в процентах
# membership (по умолчанию "обычный") - тип членства клиента
# Если membership равно "премиум", добавьте дополнительно 5% к скидке
# Если membership равно "vip", добавьте дополнительно 10% к скидке
# Возвращает словарь с исходной ценой, размером скидки, финальной ценой и типом членства

def calculate_discount(price: float, *, discount_percent: int = 10, membership: str = "обычный"):
# Все аргументы после "*" должны передаваться по имени (т.е. discount_percent = 15, а не просто 15)
    extra = 0
    if membership == "премиум":
        extra = 5
    elif membership == "vip":
        extra = 10
# или: extra = 5 if membership == "премиум" else 10 if membership == "vip" else 0
    total_discount = discount_percent + extra
    final_price = price * (100 - total_discount) / 100
    return {
        "Исходная цена": price,
        "Размер скидки": total_discount,
        "Финальная цена": round(final_price, 2), # до копеек
        "Тип членства": membership
    }

print(calculate_discount(121, discount_percent=11, membership="vip"))

# Функция format_name
# Первые два аргумента first_name и last_name должны быть только позиционными (используйте /)
# Третий аргумент middle_name необязательный и может передаваться любым способом
# Параметр format_style (по умолчанию "short") определяет стиль форматирования
# При "short": возвращает "Фамилия И.О." или "Фамилия И." если нет отчества
# При "full": возвращает "Фамилия Имя Отчество" полностью
# При "reverse": возвращает "Имя Фамилия" или "Имя Отчество Фамилия"

def format_name(first_name: str, last_name: str, /, middle_name: str = None, format_style: str = "short"):
# Все аргументы до "/" только позиционные (передаются строго по порядку, нельзя указать имя аргумента)! После - пофиг
    if format_style == "short":
        initials = f"{first_name[0]}."
        if middle_name:
            initials += f"{middle_name[0]}."
        return f"{last_name} {initials}"
    elif format_style == "full": # ФИО
        full_name = f"{last_name} {first_name}"
        if middle_name:
            full_name += f" {middle_name}"
        return full_name
    elif format_style == "reverse": # ИОФ :)
        reverse_name = first_name
        if middle_name:
            reverse_name += f" {middle_name}"
        reverse_name += f" {last_name}"
        return reverse_name
    else:
        raise ValueError("Неопознанный стиль форматирования :3")

print(format_name("Руслан", "Большаков", "Батькович", format_style="short"))
print(format_name("Руслан", "Большаков", "Батькович", format_style="full"))
print(format_name("Руслан", "Большаков", "Батькович", format_style="reverse"))
