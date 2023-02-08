my_list = ["gs", "fb","es"]
print(my_list, type(my_list))

for var_name in my_list:
    print(var_name, type(var_name))
    print(var_name.upper())
    name = "var_" + var_name
    print(name)
    print("")

print("done!")
