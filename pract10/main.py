
from PIL import Image,  ImageFilter, ImageDraw, ImageFont
from PIL.Image import Image
from utils import add_watermark_to_image

#1
try:
    with Image.open('1.jpeg') as source:
        text_crop_box = (0, 0, 700, 272)
        crop_text = source.crop(text_crop_box)

        dogs_crop_box = (0, 188, 375, 465)
        crop_dogs = source.crop(dogs_crop_box)

        crop_text.save('papka/text.png', "png")
        crop_dogs.save('papka/dogs.png', "png")
except OSError:
    print("[ОШИБКА] Возникли проблемы с доступом к картинке.")
#2
def lab():
 holidays = {
    "День рождения": 'happy.jpg',
    "День матери": "mama.jpg",
    "День  Студента": 'student.jpg',
    "8 Марта": '8mart.jpg'
}

 print("Покажем картинку для праздника!")
 print("Нам известны следующие праздники:")
 for h in holidays:
     print(f" - {h}")

 try:
     holiday = input("Для какого праздника вы ищите картинку: ")

     if holiday.lower() in holidays:
         with Image.open(holidays[holiday]) as img:
             print("Вот ваша картинка!")
             img.show(holidays)
             sys.exit()
 except ValueError:
     print("[Такого праздника нет..")
lab()
#3


try:
        name = input("Кого поздравляем : ")

        with Image.open("1.jpeg") as source:

            txt = Image.new("RGBA", source.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)
            fnt = ImageFont.truetype("arial.ttf", 60, encoding="UTF-8")

            draw.rectangle((0, 0, source.width, 120), fill=(255, 0, 0))
            draw.text(
                (100, 30),
                f"{name}, поздравляем!",
                font=fnt,
                fill=(255, 255, 255),
                stroke_width=6,
                stroke_fill=(125, 125, 255),
            )

            result: Image = Image.alpha_composite(source, txt)
            result.show()
except OSError:
 print(" Возникли проблемы с доступом к картинке или шрифту.")



