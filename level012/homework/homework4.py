nums=[-12,23,-3432,344,0,-23,12,-7,234,734,-23,]

zero=0
true=0
false=0

for num in nums:
    if num==0:
        zero+=1
    elif num<0:
        false+=1
    elif num>0:
        true+=1
print(f"zero={zero}")
print(f"true={true}")
print(f"false={false}")