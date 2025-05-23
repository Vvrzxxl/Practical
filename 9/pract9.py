from PIL import Image, ImageFilter, ImageDraw, ImageFont

import matplotlib.pyplot as plt
import numpy as np
#1
try:
   cat = Image.open('cats/Cat.jpg')
except:
    print('Ошибка')

# Выводим информацию о размере изображения, формате и цветовой модели
print("Размер изображения:", cat.size)
print("Формат изображения:", cat.format)
print("Цветовая модель:", cat.mode)

# Отображаем изображение
cat.show()

#2

# Открываем изображение
cat = Image.open('cats/Cat.jpg')

# Создаем уменьшенную копию в 3 раза
small_cat = cat.resize((cat.width//3, cat.height//3))
small_cat.save('small_cat.jpg')

# Горизонтальное зеркальное отражение
cat_horizontal = cat.transpose(Image.FLIP_LEFT_RIGHT)
cat_horizontal.save('cat_horizontal.jpg')

# Вертикальное зеркальное отражение
cat_vertical = cat.transpose(Image.FLIP_TOP_BOTTOM)
cat_vertical.save('cat_vertical.jpg')

#3
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
#4

image = Image.open("cats\Cat.jpg")
# this open the photo viewer
image.show()
plt.imshow(image)


size = (500, 100)
crop_image = image.copy()
# to keep the aspect ration in intact
crop_image.thumbnail(size)


copied_image = image.copy()
# base image
copied_image.paste(crop_image, (500, 200))
# pasted the crop image onto the base image
plt.imshow(copied_image)
