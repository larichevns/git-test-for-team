def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def guess_gender_by_name(name):
    """Определение гендера по имени (с расширенными опциями)"""
    import random

    # Различные гендерные идентичности
    genders = [
        "Мужской",
        "Женский",
        "Небинарный",
        "Гендерфлюид",
        "Агендер",
        "Бигендер",
        "Гендерквир",
        "Двудух (Two-Spirit)",
        "Нейтройс",
        "Демигёрл",
        "Демибой"
    ]

    male_endings = ['й', 'н', 'л', 'р', 'м', 'в', 'г', 'д', 'к', 'т', 'ий', 'им', 'ан', 'он']
    female_endings = ['а', 'я', 'на', 'ия', 'ла']
    neutral_endings = ['и', 'с', 'ь', 'о', 'е', 'ен', 'ис']

    name = name.strip().lower()

    if not name:
        return random.choice(genders)

    # 30% шанс получить небинарный/другой гендер
    if random.random() < 0.3:
        return random.choice(genders[2:])  # Небинарные варианты

    # Определяем по окончанию
    if any(name.endswith(end) for end in female_endings):
        return "Женский" if random.random() > 0.2 else random.choice(["Демигёрл", "Гендерфлюид", "Бигендер"])
    elif any(name.endswith(end) for end in male_endings):
        return "Мужской" if random.random() > 0.2 else random.choice(["Демибой", "Гендерфлюид", "Бигендер"])
    elif any(name.endswith(end) for end in neutral_endings):
        return random.choice(["Небинарный", "Агендер", "Нейтройс", "Гендерквир"])
    else:
        return random.choice(genders)

def gender_detector():
    """Интерактивный определитель гендера"""
    print("\n=== 🌈 Расширенный определитель гендерной идентичности ===")

    while True:
        name = input("\nВведите имя (или 'выход' для возврата): ")

        if name.lower() == 'выход':
            break

        gender = guess_gender_by_name(name)

        # Добавляем описание
        descriptions = {
            "Мужской": "традиционная мужская идентичность",
            "Женский": "традиционная женская идентичность",
            "Небинарный": "идентичность вне бинарной системы мужчина/женщина",
            "Гендерфлюид": "гендер изменяется со временем",
            "Агендер": "отсутствие гендерной идентичности",
            "Бигендер": "две гендерные идентичности одновременно",
            "Гендерквир": "квир-идентичность вне традиционных категорий",
            "Двудух (Two-Spirit)": "термин коренных американцев, третий гендер",
            "Нейтройс": "нейтральная гендерная идентичность",
            "Демигёрл": "частично женская идентичность",
            "Демибой": "частично мужская идентичность"
        }

        description = descriptions.get(gender, "уникальная идентичность")
        print(f"✨ Имя: {name}")
        print(f"🏳️‍🌈 Гендерная идентичность: {gender}")
        print(f"📝 Описание: {description}")

def calculator():
    """Основная функция калькулятора"""
    print("=== Калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Определитель гендера")
    print("6. Выход")

    while True:
        choice = input("\nВыберите операцию (1-6): ")

        if choice == '6':
            print("Выход из калькулятора")
            break

        if choice == '5':
            gender_detector()
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == '1':
                    print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Результат: {num1} / {num2} = {result}")
            except ValueError:
                print("Ошибка: введите корректное число")
        else:
            print("Ошибка: выберите операцию от 1 до 6")

if __name__ == "__main__":
    calculator()
