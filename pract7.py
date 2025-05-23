import random
from utils import get_uniq_random_int, get_occurence_count

#1
def lab7():

    from_n = 0
    to = 20

    try:
        print("Какое число я загадал от" ,from_n, "до" ,to)
        a = input("Ваш ответ: ")
        random_numbers = [random.randint(from_n, to) for _ in range(5)]

        print("Я загадывал: ", ", ".join(map(str, random_numbers)))
        if int(a) in random_numbers:
            print(" Поздравляю! Вы угадали число!")
            return True
        print("Нет такого числа")
        return False
    except ValueError:
        print(" Возможно вы ввели не число...")
        return False

#2
def lab7_2():

    list = [random.randint(0, 10) for _ in range(10)]
    numbers = {}

    for i in list:
        if i in numbers:
            numbers[i] += 1
        else:
            numbers[i] = 1

    print("Список значений: ", ", ".join(map(str, list)))

    for a, b in numbers.items():
        if v > 1:
            print(f'Значение "{a}" встретилось {b} раз(-а)!')

#3
def lab7_3():

    week_days = (
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    )

    days_num = input("Сколько выходных на неделе хотите: ")

    try:
        if int(days_num) == 7:
            print("А работать кто будет?)")
        elif int(days_num) == 0:
            print("Ого, без выходных!")
        else:
            weekends = week_days[-int(days_num) :]
            lost_week_days = week_days[: -int(days_num)]
            print("выходные дни: ", ", ".join(weekends))
            print("Но поработать нужно в эти дни: ", ", ".join(lost_week_days))
    except ValueError:
        print(" Не правильно ввели значение")
    except IndexError:
        print(" Значение должно быть от 0 до 7")

#4
def lab7_4():

    group1 = [
        "Абраменко",
        "Бочаров",
        "Бурдейная",
        "Добров",
        "Коновальчиков",
        "Лукьянчикова",
        "Малахов",
        "Мельников",
        "Микрюкова",
        "Огородникова",
    ]
    group2 = [
        "Оржаховская",
        "Пихтина",
        "Сажнев",
        "Сухопар",
        "Тарасова",
        "Шахбалаева",
        "Ярошевская",
        "Капкайкина",
        "Ершов",
        "Юлдашев",
    ]

    group1_players = tuple(
        group1[i] for i in get_uniq_random_int(5, len(group1) - 1)
    )
    group2_players = tuple(
        group2[i] for i in get_uniq_random_int(5, len(group2) - 1)
    )

    total_team = group1_players + group2_players

    print("Игроки из 1-й группы:", ", ".join(group1_players))
    print("Игроки из 2-й группы:", ", ".join(group2_players))
    print("Наша общая команда:", ", ".join(total_team))
    print(f"Играет",len(total_team), "игроков")
    print("В алфавитном порядке:", ", ".join(sorted(total_team)))

    occurence_target = "Абраменко"
    occurence_count = get_occurence_count(sorted(total_team), "Абраменко")
    print(occurence_target, "встречался в списке игроков", occurence_count, "раз!")


lab7_4