from PIL import Image

img = Image.open("risunok3.jpg")

img_bw = img.convert("L")

flipped_img = img_bw.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

new_width = 400
new_height = 300
resized_img = flipped_img.resize((new_width, new_height))

resized_img.save("risunok4.jpg")
resized_img.show()

print("Изображение успешно обработано и сохранено в файл risunok4.jpg")
