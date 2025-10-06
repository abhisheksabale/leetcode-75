from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                for k in range(j+1, n):
                    if nums[j] < nums[k]:
                        return True

    return False

print(increasingTriplet([0,4,2,1,0,-1,-3]))