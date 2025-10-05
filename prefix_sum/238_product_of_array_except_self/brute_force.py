from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        temp = 1
        for j in range(len(nums)):
            if j == i:
                continue
            temp = temp * nums[j]
        result.append(temp)
    return result

print(productExceptSelf([-1,1,0,-3,3]))