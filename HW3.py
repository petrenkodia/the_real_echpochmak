print("--- СПИСКИ list [] ---")

print("\nЗадача 1: Базовые операции со списками")
# Запросить 5 фруктов и сохранить в список. Вывести третий фрукт и общее количество фруктов.
fruits = input("Введите 5 фруктов (через пробел): ").split()  # Яблоко Банан Апельсин Груша Киви
print("Третий фрукт:", fruits[2])
print("Всего фруктов:", len(fruits))

print("\nЗадача 2: Удаление дубликатов")
# Дан список чисел с повторениями. Создать новый список без дубликатов, сохранив порядок.
# Вывести исходный список, новый список и количество удаленных дубликатов.
numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8, 7, 9]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Без дубликатов:", unique)
print("Удалено элементов:", len(numbers) - len(unique))

print("\nЗадача 3: Объединение списков")
# Даны два списка. Создать новый список, содержащий все элементы обоих списков в порядке возрастания.
# Вывести исходные списки и объединенный отсортированный список.
list1 = [3, 7, 1, 9, 5]
list2 = [8, 2, 6, 4, 10]
merged = sorted(list1 + list2)
print("Объединённый список:", merged)

print("\nЗадача 4: Матрица и операции с ней")
# Создать матрицу 3x3, заполненную числами от 1 до 9.
# Вывести матрицу, сумму элементов на главной диагонали и максимальные элементы в каждой строке.
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
matrix = [a, b, c]
# генерация матрицы от нейроночки: matrix = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
print("Матрица:")
for row in matrix:
    print(*row)
print("Сумма диагонали:", sum(matrix[i][i] for i in range(3)))
print("Максимумы строк:")
for i in range(3):
    print(f"Строка {i+1}: {max(matrix[i])}")

print("\nЗадача 5: Обработка вложенных ")
# Дан вложенный список. Вывести все числа из списка по порядку, каждое на новой строке.
nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
numbers = [
    nested_list[0],
    *nested_list[1][:2],
    *nested_list[1][2],
    nested_list[2],
    *nested_list[3]
]
print(*numbers, sep='\n')

print("\n--- КОРТЕЖИ tuple () ---")

print("\nЗадача 1: Создание и доступ к элементам кортежа")
# Создать кортеж из 5 профессий. Вывести первую и последнюю профессию, а также общее количество профессий.
prof = ("лекарь", "изобретатель", "наставник", "колдун", "друид")
print("Первая профессия:", prof[0])
print("Последняя профессия:", prof[-1])
print("Всего профессий в кортеже:", len(prof))

print("\nЗадача 2: Распаковка кортежа")
# Создать кортеж с информацией о студенте. Распаковать в переменные и вывести информацию в заданном формате.
student = ("Супер Биг Дик Ган", 16, 4.5)
name, age, gpa = student
print(f"Студент: {name}\nВозраст: {age}\nСредний балл: {gpa}")

print("\nЗадача 3: Работа с вложенными кортежами")
# Создать кортеж с инф. о городах. Найти город с наибольшим населением и вывести его название, координаты и население.
cities = (
    ("Москва", (55.7558, 37.6173), 12500000),
    ("Санкт-Петербург", (59.9343, 30.3351), 5400000),
    ("Новосибирск", (55.0084, 82.9357), 1600000)
)
megapolis = cities[0]
for city in cities:
    if city[2] > megapolis[2]:
        megapolis = city
print(f"Город с наибольшим населением: {megapolis[0]}\nКоординаты: {megapolis[1]}\nНаселение: {megapolis[2]}")

print("\nЗадача 4: Кортежи в качестве ключей словаря")
# Создать словарь, где ключи - кортежи (месяц, год), значения - количество дней.
# По запросу вывести информацию о количестве дней в указанном месяце или сообщение об отсутствии данных.
days_in_month = {
    (1, 2024): 31,
    (2, 2024): 29,
    (3, 2024): 31,
    (4, 2024): 30
}
month = int(input("Введите месяц (1-12): "))
year = int(input("Введите год: "))
mes_god = (month, year)
if mes_god in days_in_month:
    print(f"Месяц: {month}, год: {year}\nКоличество дней: {days_in_month[mes_god]}")
else:
    print("Данных для этого месяца нет")

print("\nЗадача 5: Работа со списком кортежей")
# Создать список студентов (кортежи).
# Найти студента с самым высоким средним баллом и вывести полную информацию о нем с сообщением о лучшем студенте.
students = [
    ("Дан Балан", 18, 4.5),
    ("Грифон Андрей", 19, 4.9),
    ("Эрик Пэнисов", 20, 4.3),
    ("Крыса Лариса", 18, 4.7)
]
the_best = students[0]
for stud in students:
    if stud[2] > the_best[2]:
        the_best = stud
# Нахождение максимума функцией: the_best = max(students, key=lambda x: x[2])
print(f"Имя: {the_best[0]}, Возраст: {the_best[1]}, Средний балл: {the_best[2]}")
print(f"Лучший студент: {the_best[0]}")

print("\n--- СЛОВАРИ dict { key : value } ---")

print("\nЗадача 1: Создание и доступ к элементам")
# Дан словарь стран и столиц.
# 1) Запросить страну, вывести столицу или сообщение об отсутствии.
# 2) Вывести все страны и столицы.
countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Япония": "Токио",
    "Австралия": "Канберра",
    "Пония": "Кёнигпон"
}
country = input('Введите название страны (например, "Пония"): ')
rod_pad = country[:-1] + "и"
print(f"Столица {rod_pad}: {countries[country]}")
for country, capital in countries.items():
    print(f"{country}: {capital}")

print("\nЗадача 2: Объединение словарей")
# Даны два словаря. Объединить с приоритетом второго. Вывести исходные и результат.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5, "e": 6}
dict3 = dict1.copy()
dict3.update(dict2)
print("Словарь №1:", dict1, "\nСловарь №2:", dict2, "\nСловарь №3 (объединенный):", dict3)

print("\nЗадача 3: Подсчет частоты слов")
# Дана строка. Создать словарь частот слов (без регистра). Вывести текст, слова с частотами, самое частое слово.
text = "Apple orange banana apple banana apple orange grape"
words = text.lower().split()
slovar = {}
for word in words:
    if word in slovar:
        slovar[word] += 1  # если есть, увеличиваем счётчик
    else:
        slovar[word] = 1   # если нет, добавляем
print(slovar)
most_common = max(slovar, key=slovar.get) # сравнивает по значениям, выдает ключ словаря (фрукт), а не ключ функции ("key")
print(f"Самое частое слово: '{most_common}' (встречается {slovar[most_common]} раз)")

print("\nЗадача 4: Вложенные словари")
# Дан словарь студентов с оценками. 1) Добавить студента/предмет/оценки. 2) Добавить оценку.
# 3) Посчитать средний балл. 4) Вывести всех студентов и предметы.
students = {
    "Иванов": {
        "Математика": [5, 4, 5],
        "Физика": [4, 5, 4],
        "Информатика": [5, 5, 5]
    },
    "Петров": {
        "Математика": [3, 4, 3],
        "Физика": [4, 4, 4],
        "Информатика": [5, 4, 5]
    }
}
students["Сидоров"] = {"Математика": [5, 5, 5]}
students["Иванов"]["Английский"] = [4, 4, 4]
students["Петров"]["Физика"].append(5) # добавили оценку в лист оценок
ivanov_grades = [] # Пустой СПИСОК для всех оценок Иванова
for subject in students["Иванов"]: # Перебираем все предметы Иванова (ключи вложенного словаря)
    ivanov_grades.extend(students["Иванов"][subject]) # Добавляем элементы в общий СПИСОК (append бы добавил списком)
# Вместо цикла можно генерацией:
# ivanov_grades = [grade for subject in students["Иванов"].values() for grade in subject]
average = sum(ivanov_grades) / len(ivanov_grades)
print(f"Средний балл Иванова: {average:.2f}") # Округлили до 2-х знаков
print("Список всех студентов:")
for student in students:
    print(f"{student}: {', '.join(students[student].keys())}")

print("\nЗадача 5: Телефонная книга")
# Дан словарь контактов. 1) Показать все. 2) Найти по имени. 3) Добавить/изменить/удалить. 4) Вывести количество.
phone_book = {
    "Иван": "123-45-67",
    "Мария": "765-43-21",
    "Алексей": "111-22-33"
}
print("Все контакты:")
for name, phone in phone_book.items():
    print(f"{name}: {phone}")
print("Телефон Марии:", phone_book["Мария"])
phone_book["Елена"] = "999-88-77"
phone_book["Иван"] = "555-55-55"
del phone_book["Алексей"]
print(f"В телефонной книге {len(phone_book)} контактов")
print("Обновлённая телефонная книга:")
for name, phone in phone_book.items():
    print(f"{name}: {phone}")
# Совет от нейронки - проверять ключи перед удалением/поиском:
# "Замените phone_book["Мария"] на phone_book.get("Мария", "не найден"), а del на phone_book.pop("Алексей", None)"

print("\n--- МНОЖЕСТВА set {} ---")
print("\nЗадача 1: Базовые операции с множествами")
# Даны два множества. Вывести: объединение, пересечение, разности, симметрическую разность.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Объединение: оператор | или метод union().
union_set = set1.union(set2)
print(f"Объединение: {union_set}")
# Пересечение: оператор & или метод intersection().
intersec_set = set1.intersection(set2)
print(f"Пересечение: {intersec_set}")
# Разность: оператор - или метод difference().
differ_set12 = set1.difference(set2)
print(f"Разность set1 - set2: {differ_set12}")
differ_set21 = set2.difference(set1)
print(f"Разность set2 - set1: {differ_set21}")
# Симметрическая разность - элементы только в 1 из множеств. Оператор ^ или метод .symmetric_difference()
sym_set = set1.symmetric_difference(set2)
print(f"Симметрическая разность: {sym_set}")

print("\nЗадача 2: Уникальные символы")
# Дан список слов. Найти уникальные символы (сортировка) и их количество.
words = ["hello", "world", "python"]
all_chars = [char for word in words for char in word] # читать с конца: берем каждую БУКВУ в СЛОВЕ, из каждого СЛОВА в списке "слова"
uniq_sort_chars = sorted(set(all_chars))
print("Уникальные символы:", uniq_sort_chars)
print("Количество уникальных символов:", len(uniq_sort_chars))
# Способ №2 как объединить все символы в множество:
# unique_chars = set().union(*words)
# При выводе сортируем и находим длину

print("\nЗадача 3: Анализ интересов")
# Дан список людей с интересами. 1) Уникальные интересы. 2) Общие интересы. 3) Поиск людей по интересу.
people = [
    {"name": "Алиса", "interests": ["чтение", "музыка", "программирование"]},
    {"name": "Боб", "interests": ["спорт", "музыка", "путешествия"]},
    {"name": "Виктор", "interests": ["программирование", "путешествия", "фотография"]}
] # список словарей
interesy = set() # пустое множество для уникальных интересов
for chel in people:
    interesy.update(chel["interests"]) # update распаковывает список интересов (каждого человека по очереди))
print("Уникальные интересы:", interesy)
# вариант с генерацией списка интересов:
# interesy = {interest for chel in people for interest in chel["interests"]}
# "взять все интересы для каждого человека chel в списке people".
obch_interesy = set(people[0]["interests"]) # установили интересы 1-го человека
for chel in people[1:]:
    obch_interesy &= set(chel["interests"]) # объединение с предыдущими
print("Общие интересы:", obch_interesy)
# obch_interesy = set.intersection(*[set(chel["interests"]) for chel in people])
# генерим СПИСОК: set-им интересы каждого chel-а из людей, потом этот СПИСОК МНОЖЕСТВ распаковываем и находим &
poisk_int = input("Введите интерес: ")
ludi = [chel["name"] for chel in people if poisk_int in chel["interests"]]
print("Люди с этим интересом:", ", ".join(ludi))

print("\nЗадача 4: Анализ текста с множествами")
# Даны две строки. Преобразовать в множества слов. Вывести: общие слова, уникальные для каждой, все уникальные.
text1 = "Python is a great programming language It is easy to learn and use"
text2 = "Java is also a good programming language It is widely used in enterprise"
words1 = set(text1.lower().split())
words2 = set(text2.lower().split())
print("Общие слова:", words1 & words2)
print("Только в text1:", words1 - words2)
print("Только в text2:", words2 - words1)
print("Все уникальные слова:", words1 | words2)
# Не понятно условие, на всякий добавила уникальные для каждой строки:
print("Все уникальные для каждой из строк:", words1 ^ words2)

print("\nЗадача 5: Решето Эратосфена") # делала с нейронкой(((, но вроде поняла
# Для N(30): 1) Создать мн-во 2..N. 2) Удалять кратные текущему простому. 3) Вывести процесс и итоговые простые числа.
N = 30
numbers = set(range(2, N + 1))
print("Исходное множество чисел:", numbers)
primes = set()

while numbers:
    current = min(numbers) # Берем с наименьшего, они точно простые
    numbers.remove(current)  # Удаляем из numbers перед обработкой!
    primes.add(current) # Добавляем в простые

    multiples = set(range(current * 2, N + 1, current)) # сам формирует кратные
    print(f"Удаляем кратные {current}: {multiples}")
    numbers -= multiples # реально удаляем)

    print("Оставшиеся числа:", numbers or "{}")

print(f"\nПростые числа до {N}:", sorted(primes))
print("Количество простых чисел:", len(primes))
