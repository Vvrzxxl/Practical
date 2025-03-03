import random

#4/1
password = input("Введите пароль: ")
password_harder = input("Повторите пароль: ")

if password == password_harder:
        print("Пароль принят")
else:
        print("Пароль не принят. Попробуйте еще раз.")

#4/2
place_number = None

while not place_number:
        place_number = input("Место: ")

if int(place_number) in range(37, 55):
        print("Место боковое")

if int(place_number) % 2 == 0:
        print("Место верхнее")

else:
        print("Место нижнее")

import random
def lab3():
    year = None

    try:
        while year is None:
            year_input = input("Введите год: ")
            if year_input.isdigit():  # Проверяем, что введено число
                year = int(year_input)
            else:
                print("Введите только число")

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"Год {year} високосный.")
        else:
            print(f"Год {year} не високосный.")
    except ValueError:
        print("Введите только число")


lab3()

#4/4
import random

# основные цвета
COLORS = ("красный", "синий", "желтый")

color1 = input("Введите первый цвет (красный, синий, желтый): ").strip().lower()
color2 = input("Введите второй цвет (красный, синий, желтый): ").strip().lower()

# проверка
if color1 not in COLORS or color2 not in COLORS:
    print("Ошибка! Введите только основные цвета: красный, синий или желтый.")
else:
    # если цвета одинаковые
    if color1 == color2:
        print(f"Получается цвет: {color1}")
    # проверка
    elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("Получается цвет: Фиолетовый")
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("Получается цвет: Оранжевый")
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("Получается цвет: Зеленый")