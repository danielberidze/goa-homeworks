nums=[3,7,1,9,5,3,7,10,25,78]
max_num=nums[0]

for num in nums:
    if num>max_num:
        max_num=num
print(f"bigest number in {max_num}")