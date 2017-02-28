import random
player1 = {"Имя":"Джон Доу","Деньги":1000,"Ставка":0,"Бросок":0}
player2 = {"Имя":"Джон Доу","Деньги":1000,"Ставка":0,"Бросок":0}

player1["Имя"]=input("Введите имя 1-го игрока: ")
player2["Имя"]=input("Введите имя 2-го игрока: ")

while True:
	player1["Ставка"] = int(input(player1["Имя"] + " введите вашу ставку: "))
	if player1["Ставка"] > player1["Деньги"] :
		player1["Ставка"] = player1["Деньги"]

	player2["Ставка"] = int(input(player2["Имя"] + " введите вашу ставку: "))
	if player2["Ставка"] > player2["Деньги"] :
		player2["Ставка"] = player2["Деньги"]

	player1["Бросок"] = random.randint(2,12)
	player2["Бросок"] = random.randint(2,12)
	if player1["Ставка"] > player2["Ставка"]:
		player2["Ставка"] = player1["Ставка"]
		print("Ставки сравнялись: ",player1["Ставка"])
	elif player2["Ставка"] > player1["Ставка"]:
		player1["Ставка"] = player2["Ставка"]
		print("Ставки сравнялись: ",player2["Ставка"])
	if player1["Ставка"] > player1["Деньги"]:
		player1["Ставка"] = player1["Деньги"]
		print("Ставка: ",player1["Ставка"])
	elif player2["Ставка"] > player2["Деньги"]:
		player2["Ставка"] = player2["Деньги"]
		print("Ставка: ",player2["Ставка"])
	if player1["Бросок"] > player2["Бросок"]:
		player1["Деньги"] += player2["Ставка"]
		player2["Деньги"] -= player2["Ставка"]
		print(player1["Имя"],"Победил")
		print(player1["Имя"],"Имеет: ",player1["Деньги"])
		print(player2["Имя"],"Имеет: ",player2["Деньги"])
	elif player2["Бросок"] > player1["Бросок"]:
		player2["Деньги"] += player1["Ставка"]
		player1["Деньги"] -= player1["Ставка"]
		print(player2["Имя"],"Победил")
		print(player1["Имя"],"Имеет: ",player1["Деньги"])
		print(player2["Имя"],"Имеет: ",player2["Деньги"])
	else:
		print("Ничья")

	if player1["Деньги"] <= 0:
		print(player2["Имя"],"пустил по ветру",player1["Имя"])
		break
	if player2["Деньги"] <= 0:
		print(player1["Имя"],"пустил по ветру",player2["Имя"])
		break