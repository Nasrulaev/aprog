class WrongDay(Exception):
	pass
class WrongMonth(Exception):
	pass
class WrongYear(Exception):
	pass
while True:
	try:
		date = input("Введите дату рождения в формате дд.мм.гггг\n")
		d = int(date[0:2])
		m = int(date[3:5])
		y = int(date[6:10])
		# print(d,m,y)
		if 1 < d > 31:
			raise WrongDay
		if 1 < m > 12:
			raise WrongMonth
		if 0 <  y > 2017:
			raise WrongYear
		if (m == 12 and d in range(22,32)) or \
		(m == 1 and d in range(1,21)):
			print("Ты козерог!")
		if (m == 1 and d in range(21,32)) or \
		(m == 2 and d in range(1,20)):
			print("Ты водолей!")
		if (m == 2 and d in range(20,30)) or \
		(m == 3 and d in range(1,21)):
			print("Ты рыба!")
		if (m == 3 and d in range(21,32)) or \
		(m == 4 and d in range(1,20)):
			print("Ты овен!")
		if (m == 4 and d in range(21,31)) or \
		(m == 5 and d in range(1,22)):
			print("Ты телец!")
		if (m == 5 and d in range(22,32)) or \
		(m == 6 and d in range(1,22)):
			print("Ты близнецы!")
		if (m == 6 and d in range(22,31)) or \
		(m == 7 and d in range(1,24)):
			print("Ты рак!")
		if (m == 7 and d in range(24,32)) or \
		(m == 8 and d in range(1,24)):
			print("Ты лев!")
		if (m == 8 and d in range(24,32)) or \
		(m == 9 and d in range(1,24)):
			print("Ты дева!")
		if (m == 9 and d in range(24,31)) or \
		(m == 10 and d in range(1,24)):
			print("Ты весы!")
		if (m == 10 and d in range(24,32)) or \
		(m == 11 and d in range(1,23)):
			print("Ты скорпион!")
		if (m == 11 and d in range(23,32)) or \
		(m == 12 and d in range(1,22)):
			print("Ты стрелец!")
		break
	except ValueError:
		print("Введите данные в правильном формате")
	except WrongDay:
		print("Данные введены не правильно!")
	except WrongMonth:
		print("Данные введены не правильно!")
	except WrongYear:
		print("Данные введены не правильно!")