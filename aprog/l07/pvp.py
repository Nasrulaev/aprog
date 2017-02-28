import random
def create_player(player):
	player["Имя"] = input("Введите имя игрока: ")
	player["Жизни"] = 1000
	player["Атака"] = 50
	boost = input("Взять броню - 1\nВзять оружие - 2\n")
	if boost == "1":
		player["Жизни"] += 500
	else:
		player["Атака"] += 25
def hit(agressor,victim):
	damage = agressor["Атака"] + random.randint(-50,50)
	victim["Жизни"] -= damage
	print("{0[Имя]} нанёс: {1[Имя]} {2} урона".format(agressor,victim,damage))
def show_params(player):
	print("{1}: {0}".format(player["Жизни"],player["Имя"]))
def fight(player1,player2):
	while True:
		hit(player1,player2)
		hit(player2,player1)
		show_params(player1)
		show_params(player2)
		input()
		if player1["Жизни"] <= 0:
			print(player2["Имя"],"уничтожил",player1["Имя"])
			break
		if player2["Жизни"] <= 0:
			print(player1["Имя"],"уничтожил",player2["Имя"])
			break
		if player1["Жизни"] <= 0 and player2["Жизни"] <= 0:
			print("Оба игрока умерли!")
player1 = {}
player2 = {}
create_player(player1)
create_player(player2)
# print(player1,player2)
fight(player1,player2)