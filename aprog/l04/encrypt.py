word = input("Введите слово: ")
#res = word[-1::-1]
# res = word[len(word) // 2:] + word[0:len(word) // 2]
res = word.lower().replace("а","б").replace("о","у")
print(res)

# krasavci = ["Кадыр","Амин","Аслан"]
# print(krasavci[1:])
# krasavci.append("Мага")
# print(krasavci)
# krasavci.insert(1,"Мага")
# print(krasavci)
# dop = ["Арслан","Амин"]
# krasavci.extend(dop)
# print(krasavci)
# krasavci[2] = 3
# print(krasavci)
# krasavci.remove("Арслан")
# print(krasavci)
# print(krasavci.pop(1))
# print(krasavci)

# str1 = ", ".join(krasavci) #разбить 
# print(str1)
# print(str1.slit(' '))  # соединить

krasavci2 = "Камал", "Гуд"
print(krasavci2)
# krasavci2[1] = ", "
krasavci2 = list(krasavci2)
krasavci2[1] = ", "

krasavci3 = {1,2,3,1,5}
krasavci4 = {1,9,3,4}
# print(1 in krasavci3)
# krasavci3.add(8)
# print(krasavci3)
print(krasavci3 & krasavci4) # пересечение
print(krasavci3 | krasavci4) # объединение
print(krasavci3 - krasavci4) # разность
# дз = сделать свою технологию шифрования
# еще одна программа для расшифровки