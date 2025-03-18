#1
try:
   n = int(input("Введите число: "))
   a = n % 3==0
   print(a)
except ValueError:
   print("Не делиться!")

#2
try:
    n = int(input("Введите число: "))
    a = 100/ n
    print(a)
except ValueError:
    print(" Нужно вводить число!")
except ZeroDivisionError:
    print(" Деление на ноль!")

#3
try:
   n = input("Введите дату : ")
   day, month, year = map(int, n.split('.'))
   print(day * month == int(str(year)[-2:]))
   print("Магическая дата")
except ValueError:
   print(" Неправильный формат даты.")
#4
def lab_6() -> bool:

    ticket_number = input("Введите номер билета: ")
    ticket_number_length = len(ticket_number)

    if ticket_number_length < 2 or ticket_number_length % 2 > 0:
        print("Количество символов в номере должно быть четным.")
        return False

    [left_numbers, right_numbers] = ticket_number[:: int(len(ticket_number) / 2)]
    left_sum = sum(int(i) for i in list(left_numbers))
    right_sum = sum(int(i) for i in list(right_numbers))

    return left_sum == right_sum

print(lab_6())

