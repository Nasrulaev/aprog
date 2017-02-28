# def show_em_all(func):
# 	def wrapper(*args,**kwargs):
# 		print("Название функции:",func.__name__)
# 		print("Позиционные аргуметы",args)
# 		print("Именованные аргуметы",kwargs)
# 		result = func(*args,**kwargs)
# 		print("Результат",result)
# 		return result

# 	return wrapper

# def sum6(a,b):
# 	return (a + b) * 6

# @show_em_all

# def loh_you(name):
# 	print(name +",Поздравляю ты лох")
# nice_sum6 = show_em_all(sum6)
# print(sum6(5,5))
# print(nice_sum6(6,6))
# show_em_all(loh_you("Амин"))

# def no(func):
# 	def wrapper(*args,**kwargs):
# 		return str(func(*args,**kwargs)) + "(Нет)"
# 	return wrapper
# @no

# def you_pretty(name):
# 	return name + (" - красавчик")
# print(you_pretty("Камал"))

super_funce = lambda a, b: a + " " + b + " Амин"
print(super_funce("Мир","Труд"))

good_boys = ["Андрей","саид","Руслан","Aслан"]

good_boys.sort()
print(good_boys)