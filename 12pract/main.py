import json
#12_1
with open('mock.json') as file:
    data = json.load(file)

for product in data['products']:
    print(f"Название: {product['name']} Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()
    #12_2

def add_product():
    new_product = {}
    new_product['name'] = input("Введите название продукта: ")
    new_product['price'] = float(input("Введите цену продукта: "))
    new_product['weight'] = input("Введите вес продукта: ")
    new_product['available'] = bool(input("Продукт в наличии? (True/False): "))

    with open('mock.json', 'r') as file:
        data = json.load(file)
        data['products'].append(new_product)

    with open('mock.json', 'w') as file:
        json.dump(data, file, indent=4)


# Добавляем новый продукт
add_product()

# Выводим содержимое файла JSON
with open('mock.json') as file:
    data = json.load(file)

for product in data['products']:
    print(f"Название: {product['name']} Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()



#12_3
en_ru_dict = {}
with open('en_ru.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        words = line.strip().split(' - ')
        en_word = words[0]
        ru_translations = words[1].split(', ')
        for ru_word in ru_translations:
            en_ru_dict[ru_word] = en_ru_dict.get(ru_word, []) + [en_word]

# Создание русско-английского словаря и запись его в файл ru_en.txt
with open('ru_en.txt', 'w') as file:
    for ru_word in sorted(en_ru_dict.keys()):
        en_words = ', '.join(sorted(en_ru_dict[ru_word]))
        file.write(f"{ru_word} - {en_words}\n")
