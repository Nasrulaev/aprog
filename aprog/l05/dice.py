# a = 1
# while a <= 10:
# 	print (a)
# 	a += 1
# a = 1
# name = "Амин"
# while name != "Артур":
# 	print(name)
# 	a += 1
# 	if a == 4:
# 		name = "Артур"

# while True:
# 	name = input("Угадайте нужное имя: ")
# 	if name == "Зубер":
# 		print("Как ты догадался?!")
# 		break
# 	print("Лошара!")
names = ["Кадыр","Амин","Аслан"]
for name in names:
	print(name)

user = {"Имя":"Руслан","Фамилия":"Насрулаев","Возраст":"15"}
for key in user.keys():
	print(key,"-",user[key])

for value in user.value():
	print(value)

for key, value in user.items():
	print(key, value)