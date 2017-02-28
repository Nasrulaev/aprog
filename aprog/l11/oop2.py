# class Mammals:
# 	def __init__(self, name, habitat, food, properties):
# 		self.name = name
# 		self.habitat = habitat
# 		self.food = food
# 		self.properties = properties

# 	def eat(self, food):
# 		res = "{0.name} поел(а) {1}".format(self, food)
# 		print(res)	

# class Cat(Mammals):
# 	def say(self):
# 		print("Мяу мифоу нгеонг")
	# def __init__(self, name, habitat, food, properties):
	# 	self.name = name
	# 	self.habitat = habitat
	# 	self.food = food
	# 	self.properties = properties

	# def eat(self, food):
	# 	res = "{0.name} поел(а) {1}".format(self, food)
	# 	print(res)

# class Dog(Mammals):
# 	super().__init__(name, habitat, food, properties,bark_loughtness)
# 	self.bark_loughtness = bark_loughtness

	# def __init__(self, name, habitat, food, properties,bark_loughtness):
	# 	self.name = name
	# 	self.habitat = habitat
	# 	self.food = food
	# 	self.properties = properti
	# def say(delf):
	# 	if bark_loughtness < 100:
	# 		print("Гав-гав")
	# 	elif:
	# 		print("Граааааааааар")
	# def __init__(self, name, habitat, food, properties):
	# 	self.name = name
	# 	self.habitat = habitat
	# 	self.food = food
	# 	self.properties = properties

	# def eat(self, food):
	# 	res = "{0.name} поел(а) {1}".format(self, food)
	# 	print(res)

	# def say(self):
	# 	print("Однако здравствуйте")

	# def bark(self):
	# 	print("Гав-гав")
# 	def eat(self,food):
# 		super().eat(food)
# 		print("И разорвала " + food + "на куски")

# selectipon = input("""Выберите вид:
# Домосед
# Мусорщик\n""")

# name = input("Введите имя:\n")

# cat = Cat(name = name, habitat = selectipon, food = "Рыба", properties = "Дом")
# print(cat.name)
# cat.eat("мясо")
# cat.say()

# dog = Dog(name = "Саид", habitat = "Каспийск", food = "картошка",properties = "общяга",bark_loughtness = )
# dog.bark()
# dog.say()

class Mammals:
	def __init__(self, name, habitat, food, properties):
		self.name = name
		self.habitat = habitat
		self.food = food
		self.properties = properties

	def eat(self, food):
		res = "{0.name} поел(а) {1}".format(self, food)
		print(res)

	def say(self):
		print("Однако здравствуйте")


class Cat(Mammals):
	def say(self):
		print("Мяу миаоу ня нгеонг")

class Dog(Mammals):

	def __init__(self, name, habitat, food, properties, bark_loughtness):
		super().__init__(name, habitat, food, properties)
		self.bark_loughtness = bark_loughtness

	def bark(self):
		if self.bark_loughtness < 1000:
			print("Гав-Гав")
		else:
			print("Граааааааар")

	def eat(self,food):
		super().eat(food)

		print("И разорвала " + food + " на куски")


selection = input("""Выберите вид:
Домосед
Мусорщик\n""")

name = input("""Выберите имя:""")

cat = Cat(name=name,habitat=selection,food="рыба",properties="дом")
print(cat.name)
cat.eat("Мясо")
cat.say()

dog = Dog(name="Саид",habitat="Каспийск",food="Картошка",properties="общага", bark_loughtness=5000)
dog.bark()
dog.say()
dog.eat("Шаурму,Виски")
