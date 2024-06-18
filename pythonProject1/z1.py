from PIL import Image


def calculate_average_color(risunok1):
    image1 = Image.open(risunok1)
    width, height = image1.size
    pixels = image1.getdata()

    total_red = 0
    total_green = 0
    total_blue = 0

    for y in range(height):
        for x in range(width):
            index = y * width + x

            total_red += pixels[index][0]
            total_green += pixels[index][1]
            total_blue += pixels[index][2]

    average_red = total_red // (width * height)
    average_green = total_green // (width * height)
    average_blue = total_blue // (width * height)
    print(f"Среднее значение цветов: {average_red} {average_green} {average_blue}")

    return image1


if __name__ == "__main__":
    image = calculate_average_color("risunok1.png")
    #image.show()
