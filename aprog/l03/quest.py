print("Медведь подойди к моей лапе ")
x = input("Подойти 1, Убежать 2 : ")
if x == "1":
    print("Вас убил медведь")
elif x == "2":
    print("Вас переехала машина")
else:
    print("Вы сказали что-то \
 непонятное и медвведь ушел")
    print("Но пришел его отец,\nЧто будем делать? ")
    x = input("1 Ударить его в лицо\n\
2 Выяснить обстоятельства : ")
    if x == "1":
        print("Вы сломали руку и умерли!")
    else:
        print("Вы не смогли догориться. Что делать теперь?!")
        x = input("1 Позвать Кадыра на помощь\
            2 Дождаться Амина :")
        if x == "1":
            print("Все всех убили")
        else:
            print("Наступила вечная тьма. Спасибо Амину")
