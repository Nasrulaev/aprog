class Shaurma:
	count = 0

	# def get_count():
	# 	print("количество шаурмы: ", Saurma_count)

	@classmethod
	def get_count():
		print("количество шаурмы: ", Saurma_count)

	def __init__(self, kind, cost, size):
		self.kind = kind
		self.cost = cost
		self.__size = size
		Shaurma.count += 1

	def __del__(self):
		Saurma_count -= 1
		print("шаурма умерла")

	def poison(self, eater):
		if self.__size > 0:
			print("{0}, был отравлен {1.kind} шаурмой".format(
				eater, self))
			self.__size -= 5
		else:
			print("шаурмы больше нет!")


	# def get_size(self):
		# return self.size

	@property
	def size(self):
		return self.size

	@size.setter
	def size(self, value):
		print("ШШаурма возрадилась")
		self.__size = value

	def __add__(self, other):
		return Shaurma("Мегашавуха",(self.count + other.count) * 10, self.size + other.size)

	def __add__(self, other):
		return "шаурма: {0.kind}, цена: {0."
chicken_shaurma = Shaurma("куринной", 70, 15)
print(chicken_shaurma)
chicken_shaurma.poison("Руслан")

meat_shaurma = Shaurma("мясной", 70, 15)
print(chicken_shaurma)
meat_shaurma.poison("Руслан")
del chicken_shaurma
meat_shaurma.poison("Амин")
meat_shaurma.poison("Камал")
meat_shaurma.poison("Мага")
print(meat_shaurma.__size)
Shaurma.get_count()