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

def calculator():
    """Основная функция калькулятора"""
    print("=== Калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")

    while True:
        choice = input("\nВыберите операцию (1-5): ")

        if choice == '5':
            print("Выход из калькулятора")
            break

        if choice in ['1', '2', '3', '4']:
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
            print("Ошибка: выберите операцию от 1 до 5")

if __name__ == "__main__":
    calculator()
