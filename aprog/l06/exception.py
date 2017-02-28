# while True:
# 	try:
# 		n1 = int(input("Введите первое число: "))
# 		n2 = int(input("Введите второе число: "))
# 		print("Результат деления", n1 / n2)
# 		break
# 	except ValueError:
# 		print("Ты больной идиот,введи ЧИСЛО!")
# 	except ZeroDivisionError:
# 		print("На нуль делить нельзя!")
# except:      (Командная срока не будет выдавать ошибок)
# 	pass

# raise ValueError ("Вызывает ошибку")

class RuslanError(Exception):
	pass
try:
	name = input("Введите имя: ")
	if name == "Руслан":
		raise RuslanError
	else:
		print("Ты молодец!")
except RuslanError:
	print("Фатальная ошибка!Вы ввели запретное имя!\n\
За вами уже выехали!")
