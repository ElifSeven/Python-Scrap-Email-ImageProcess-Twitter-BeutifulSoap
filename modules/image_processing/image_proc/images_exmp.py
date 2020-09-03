from PIL import Image, ImageFilter

img = Image.open('/Users/elifseven/Desktop/pythonProject1/modules/image_processing/images/pikachu.jpg')
# print(img)

print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

filtered_img_sharpen = img.filter(ImageFilter.SHARPEN)
filtered_img_sharpen.save("sharpen.png", "png")

filtered_img_grey = img.convert('L')
filtered_img_grey.save("grey.png", "png")
rotated = filtered_img_grey.rotate(90)
# rotated.show()

box = (100, 100, 480, 480)
region = filtered_img_grey.crop(box)
region.save("grey.png", "png")
region.show()

img2 = Image.open('/Users/elifseven/Desktop/pythonProject1/modules/image_processing/images/astro.jpg')
# print(img2.size)

# new_img = img2.resize((400,400))

img2.thumbnail((400, 400))
img2.save("astro2.jpg")
img2.show()
