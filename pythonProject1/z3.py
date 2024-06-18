from PIL import Image


image = Image.open("risunok5.png")
pixels = image.getdata()
new_pixel = []
for pixel in pixels:
    new_pixel.append((min(pixel), pixel[1], max(pixel)))


image.putdata(new_pixel)


rotated_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

rotated_image.save("risunok6.png")
rotated_image.show()
