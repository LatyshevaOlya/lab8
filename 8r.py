from PIL import Image
def z1():
    # Задаем пути к исходному и выходному изображениям
    input_image_path = 'pythonProject1/image.jpg'
    output_image_path = 'pythonProject1/cropped_image.jpg'
    # Задаем координаты для обрезки
    left = 100
    upper = 100
    right = 400
    lower = 400
    # Открываем изображение
    image = Image.open('dr.jpg')
    # Определяем область для обрезки
    cropped_image = image.crop((left, upper, right, lower))
    # Сохраняем обрезанное изображение
    cropped_image.save(output_image_path)
    print(f"Изображение успешно обрезано и сохранено как {output_image_path}")

def z2():
        prazd = {
            'Пасха': 'vesna.jpg',
            'День рождения': 'dr.jpg',
            'Новый Год': 'snow.jpg'
        }
        imageR = 'snow.jpg'
        imageD = 'dr.jpg'
        imageV = 'vesna.jpg'
        s = input("Напишите праздник: ")
        if s in prazd:
            image_path = prazd[s]
            image = Image.open(image_path)
            image.show()
        elif s != "День рожднения":
            image_path = prazd[s]
            image = Image.open(imageD)
            image.show()
        elif s != "Пасха":
            image_path = prazd[s]
            image = Image.open(imageV)
            image.show()
        elif s != "Новый год!":
            image_path = prazd[s]
            image = Image.open(imageR)
            image.show()

        else:
            print("Введенное значение не найдено в списке.")


        name = input("Введите имя: ")
        image = Image.open("dr.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 30)

        text = f"{name}, поздравляю!"
        text_width, text_height = draw.textsize(text, font=font)
        position = ((image.width - text_width) // 2, 10)  # Позиция текста в центре вверху
        draw.text(position, text, font=font, fill="black")
        image.save("new_dr.png")

def z3():
    from PIL import Image, ImageDraw, ImageFont

    # Запрашиваем имя пользователя
    name = input("Введите имя: ")

    # Открываем изображение
    image = Image.open("dr.jpg")
    draw = ImageDraw.Draw(image)

    # Загружаем шрифты
    font_regular = ImageFont.truetype("arial.ttf", 30)
    font_bold = ImageFont.truetype("arialbd.ttf", 30)  # Шрифт Arial Bold для жирного текста
    number = 1
    # Формируем текст
    text = f"{name}, поздравляю!"
    # Используем метод text с direction=0 для получения размеров текста
    text_width, text_height = draw.text((0, 0), text, font=font_regular, direction=0)

    # Позиция текста в центре вверху или внизу (в данном примере - вверху)
    position = ((image.width - text_width) // 2, 10)

    # Выводим текст с разным цветом и шрифтами
    draw.text(position, text[:text.find(',')], font=font_bold, fill="black")  # Имя жирным шрифтом
    draw.text(position, text[text.find(',') + 1:], font=font_regular,
              fill="black")  # Остальная часть текста обычным шрифтом

    # Сохр
    image.save("new_dr.png")
z3()