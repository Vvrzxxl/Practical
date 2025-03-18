import random

# 1
n = int(input("Введите N слов: "))
b = []
for i in range(n):
    word = input("Введите слово: ")
    b.append(word)
result = ' '.join(b)
print(result)

#2
b = []
while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    else:
        b.append(word)
result = ' '.join(b)
print(result)

#3
word = input("Введите слово: ")
if 'ф' in word:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")


#4

right = 0
error = 0

while error < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = num1 + num2
    answer = input(f"{num1} + {num2} = ")

    if int(answer) == result:
        print("Правильно!")
        right += 1
    else:
        print("Ответ неверный")
        error += 1

print(f"Игра окончена. Правильных ответов: {right}")