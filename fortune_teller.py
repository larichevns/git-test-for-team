import random

def fortune_teller():
    """Генератор предсказаний судьбы"""

    fortunes = [
        "Сегодня упадет прод!",
        "Ожидайте мит на 5 часов!",
        "Астрологи объявили неделю кентавров"
    ]

    name = input("Введите ваше имя: ")
    print(f"\n Предсказание для {name}: ")
    print(random.choice(fortunes))

if __name__ == "__main__":
    fortune_teller()