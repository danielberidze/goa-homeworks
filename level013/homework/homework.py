o=["no","yes"]

age=int(input("enter your age: "))
city=int(input("do you have citizenship if yes input 1 if no input 0: "))

print(o[city])

if age>=18 and city==1:
    print("you can enter")
else:
    print("do not enter")