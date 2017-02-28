# def hello(name):
# 	print("Привет, {0}!!!".format(name))

# hello("Амин")
# hello("Ватсон")

# def sum5(a,b):
#  	s = a + b + 5
# 	return s

# print(sum5(5,6))
# summa = sum5(5,6)
# print(summa + 1)

# def input_number():
# 	while True:
# 		try:
# 			number = int(input("Введите число: "))
# 			return number
# 		except ValueError:
# 			print("Введите правильные данные")

# a = input_number()
# b = input_number()
# print("Сумма чисел {0} и {1} = {2}".format(a,b,a + b))

# print(sum5(b = 3,a = 5))

# def  hello2(name,target = "горы"):
# 	print("Привет,{0}. Иди-ка ты в {1}".format(name,target))

# hello2("Амин")
# hello2("Арслан","школу")

# print(1,end=" ")
# print(2)

# def get_first_two_values_from_list(list1):
# 	return list1[0], list1[1]

# m = get_first_two_values_from_list(["Амир","Кадыр",8,9])
# a, b = m
# print(a,b)
# a, b = get_first_two_values_from_list(["Амир","Кадыр",8,9])
# a, b = 5, 6
# print(a,b)

def show_good_boys(*args):
	for boy in args:
		print("Мальчик:", boy,end=" ")
	print()

show_good_boys("Джавид","Руслан")

def get_toys(**kwargs):
	for toy, price in kwargs.items():
		print("У игрушки {0} цена {1}".format(toy,price))

get_toys(mashinka=10,kukla=75,арбуз=12)

def mul5(a, b):
	c = a * b * 5
	return c
print(mul5(1,2))