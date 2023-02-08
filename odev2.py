total = 0
while True:
    number = input("Enter a number(exit=q): ")
    if number == "q":
        break
    total = total + int(number)

print(total)
