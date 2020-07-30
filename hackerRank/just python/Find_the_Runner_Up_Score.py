n = int(input())

nums = map(int, input().split())    
nums=set(nums)
nums=list(nums)
nums.sort(reverse = True) 
print(nums[1])
