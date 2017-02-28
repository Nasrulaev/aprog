# a = "Амин красавчик"
# b = 6
# c = 6.1
# d = True
# e = None
# print(a, b, c, d, e)
# print(type(a), type(b), type(c))
# print(type(d), type(e))

# print(a[0:4])
# print(a[0] + a[1] + a[2] + a[3]) - конкантинация
# print(a[5:])
# print(a[-5:])
# print(a[-100:100])
# print(a[0:10:2])
# print(a[-1:-4:-1])
# print(len(a))
poem = """Ты видел деву на скале
В одежде белой над волнами
Когда, бушуя в бурной мгле,
Играло море с берегами,
Когда луч молний озарял
Ее всечасно блеском алым
И ветер бился и летал
С ее летучим покрывалом?
Прекрасно море в бурной мгле
И небо в блесках без лазури;
Но верь мне: дева на скале
Прекрасней волн, небес и бури."""
print(poem.find("море"))
print(poem.rfind("море"))
print(poem[::-1])
print(poem.count("море"))

print(poem.upper())
print(poem.lower())
print(poem.title())

print(poem.replace("море","небо"))

krasavci = ["Кадыр","Амин","Аслан"]
print(krasavci[1:])
krasavci.append("Мага")
print(krasavci)
krasavci.insert(1,"Мага")
print(krasavci)
dop = ["Арслан","Амин"]
krasavci.extend(dop)
print(krasavci)
krasavci[2] = 3
print(krasavci)
krasavci.remove("Арслан")
print(krasavci)
print(krasavci.pop(1))
print(krasavci)

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