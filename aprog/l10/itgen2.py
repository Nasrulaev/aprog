import random
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# letters = [letter for letter in alphabet[:6]if letter != "г"]
# print(letters)


def generator(letters,name_count,letter_count):
	for i in range(name_count):
		random_name = ""
		for j in range(letter_count):
			random_name += random.choice(list(letters))
		yield random_name

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for name in generator(alphabet,3,6):
	print(name)