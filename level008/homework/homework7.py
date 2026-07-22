start=int(input("enter any number"))
stop=int(input("enter a nother number"))

i=start

if start<=stop:
    while start<=stop:
        print(i)
else:
    while i>=stop:
        print(i)
        i-=1