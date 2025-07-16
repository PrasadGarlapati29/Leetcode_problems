
nums = [7,1,5,4]
min=nums[0]
max_value=-1
n=len(nums)
for i in range(1,n):
    if nums[i]>min:
        difference=nums[i]-min
        max_value=max(difference,max_value)
    else:
        min=nums[i]
print(max_value)
