from PIL import Image

im = Image.open("koala.jpg")
pixels = im.load()

x, y = im.size

# print(x, y)
# print(im)
dep = int(input("Введите глубину сепии:\n"))
for i in range(x):
	for j in range(y):
		r, g, b = pixels[i, j]
		mid = (r + g +b) // 3
		# pixels[i, j] = mid, mid, mid
		r, g, b = mid + dep * 2, mid + dep, mid
		pixels[i, j] = r, g, b


im.save("koala3.jpg")
im.show()
