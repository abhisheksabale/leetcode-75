from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    i = 0
    j = k
    result = 0
    while j <= len(nums):
        sum = 0
        for n in range(i, j):
            sum += nums[n]
        avg = sum / k
        if avg > result:
            result = avg
        i += 1
        j += 1
    return result

print(findMaxAverage([-1], 1))