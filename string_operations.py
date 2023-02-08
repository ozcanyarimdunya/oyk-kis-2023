info_dict ={
    "name": "test",
    "age": 100
}
print(info_dict)
# { "name": "test", "age": 100 }

name = input("Enter your name: ")
age = input("Enter your age: ")

info_dict["name"] = name
info_dict["age"] = int(age)

print(info_dict)

# enter your name:
# enter your age:

# { "name": "ozcan", "age": 30 }

#
# info_dict["name"] = input("isim: ")
# info_dict["age"] = input("yas: ")
# print(info_dict)
