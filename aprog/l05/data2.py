a = ["Руслан","Джамиля","Амин"]
print(a)
a.append("Андрей")
print(a)
x = (1, 2,"Зубер")
print(x[2])
string = ", ".join(a)
print(string)
a.sort()
print(a)

en_ru_dict = {
"house":"дом",
"apple":"яблоко",
"school":"школа"}

print(en_ru_dict["school"])
en_ru_dict["house"] = "жилище"
print(en_ru_dict)
en_ru_dict["phone"] = "телефон"
print(en_ru_dict["phone"])