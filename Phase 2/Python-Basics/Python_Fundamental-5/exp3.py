nums = [-2,-3,4,5,-1,6 ]

nums = [0 if val < 0 else val for val in nums] # ye line nums list me se negative numbers ko 0 se replace karega aur positive numbers ko waise hi rehne dega
print(nums)