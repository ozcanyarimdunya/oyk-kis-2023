uzun = 4
kisa = 2
print("----")
print("-  -")
print("-  -")
print("----")
print(",,,,,,")

print(uzun*"$")
print("$", (kisa-2)*" ", "$")
print("$", (kisa-2)*" ", "$")
print("$", (kisa-2)*" ", "$")
print(uzun*"$")

name = "özcan"
surname = "yarimdunya"

fullname = name + " " + surname
print(fullname)


print(name.title(), surname.upper())

string = "i am here at uni at 10a"
print(string.strip())

print(string.split("a"))

my_list = ["ankara", "istanbul", "eskisehir"]
print(my_list)
#my_list.append("bursa")
print(my_list.insert(1, "bursa"))
print(my_list)
my_list.remove("ankara")
print(my_list)
print(my_list.pop(2))
print(my_list)

