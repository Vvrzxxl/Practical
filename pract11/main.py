import os
import random
import csv
from PIL import Image, ImageFilter


# 2
VALID_IMAGE = ("jpg", "jpeg", "png")
#1
img = Image.open('cats/Cat.jpg')

img = img.filter(ImageFilter.CONTOUR)
img.save("1.jpg")

img = img.filter(ImageFilter.DETAIL)
img.save("2.jpg")

img = img.filter(ImageFilter.EDGE_ENHANCE)
img.save("3.jpg")

img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.save("4.jpg")

img = img.filter(ImageFilter.EMBOSS)
img.save("5.jpg")

def lab_11():

    csv1 = os.path.join(os.getcwd(), 'lab10', 'lab_11_3_mock.csv')

    try:
        price = 0

        with open(csv1, "r", encoding="UTF-8") as f:
            reader = csv.reader(f)
            next(reader)

            print("Нужно купить:")
            for item, count, prices in reader:
                price += int(prices) * int(count)
                print(f"[ ] {item} - {count} шт. за {prices} руб.")
            print(f"Итого: {price} руб.")
    except OSError:
        print("Проблемы с файламом CSV.")


lab_11()
