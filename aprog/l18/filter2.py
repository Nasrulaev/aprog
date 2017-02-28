from PIL import Image

im = Image.open("koala.jpg")
pixels = im.load()

x, y = im.size

# print(x, y)
# print(im)
br = int(input("На сколько изменить яркость?:\n"))
for i in range(x):
	for j in range(y):
		r, g, b = pixels[i, j]
		pixels[i, j] = r + br, g + br, b + br

im.save("koala2.jpg")
im.show()