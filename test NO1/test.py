#ტერმინალი არის ადგილი სადაც კოდის შდეგი გამოდის
#დაბაგინგი არის კოდის ერორებისგან განთავისუფლება
#პითონი კოდს კითხულობს ზემოდან ქვემოთ


feri = "Black"
saxeli = "danieli"
chemi_asaki = 16

print(feri)
print(saxeli)
print(chemi_asaki)


num1=int(input("enter any number :"))
num2=int(input("enter a nother number :"))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(F"{num1}>{num2}={num1>num2}")
print(F"{num1}<{num2}={num1<num2}")

counter=0

for i in range(5):
    num=int(input("enter a number :"))
    counter+=num
print(counter)

counter=0
num1=int(input("enter any number: "))
num2=int(input("enter any number: "))
num3=int(input("enter any number: "))
num4=int(input("enter any number: "))
num5=int(input("enter any number: "))

nums=[num1,num2,num3,num4,num5]

even_counter=0
add_counter=0

for num in nums:
    if num%2==0:
        even_counter+=1
    else:
        add_counter+=1
print(f"even_counter = {even_counter}")
print(f"add_counter = {add_counter}")


secret_pasword="goa12345"
enter=(input("enter pasword: "))

while enter!=secret_pasword:
    print("pleas try again")
    enter=(input("enter pasword: "))
print("login successful")

secret_number=5
enter=int(input("enter the number"))

while enter !=secret_number:
    if enter<secret_number:
        print(">")
        enter=int(input("enter the number"))
    if enter>secret_number:
        print("<")
        enter=int(input("enter the number"))
    if enter==secret_number:
        print("you gues the number")
        break

start=int(input("enter start number: "))
end=int(input("enter end number: "))

even=0
odd=0

for i in range(start , end):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"even={even}")
print(f"odd={odd}")