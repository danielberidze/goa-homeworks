countrys=["georgia","ukrayn","china","united states of america","japan","england","germany"]

man=int(input("enter number 0-6:  "))

while man>6:
    print("try don't enter more then 6")
    
    man=int(input("enter number 0-6 :  "))
if man<=6:
    print(countrys[man])
