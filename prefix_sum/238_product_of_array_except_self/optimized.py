from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    ans = [1] * length
    current = 1
    for i in range(length):
        ans[i] *= current
        current *= nums[i]
    current = 1
    for i in range(length-1, -1, -1):
        ans[i] *= current
        current *= nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))