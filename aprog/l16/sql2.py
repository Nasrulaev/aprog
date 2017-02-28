import sqlite3
conn = sqlite3.connect("weapon_shop.db")
curs = conn.cursor()

curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
# print(rows)

curs.execute("SELECT name, cost FROM weapons WHERE cost < 4000 ORDER BY cost DESC")
rows = curs.fetchall()
for row in rows:
	print("Название  оружия: {0[0]}, Цена оружия: {0[1]}".format(row))

curs.execute("UPDATE weapons SET name = 'АминаСтвол', cost = 30000s WHERE name = 'P90'")
curs.execute("DELETE FROM weapons WHERE name = 'Desert Eagle'")
conn.commit()

curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
print(rows)


curs.close()
conn.close()





# print("Твоё имя: {0[0]},\nТвоя фамилия: {0[5]},\nТы Амин: {0[1]},\nТы тупой:{0[2]},\nТы учишься в {0[3]},\nТвой возраст {0[4]}".format(row))