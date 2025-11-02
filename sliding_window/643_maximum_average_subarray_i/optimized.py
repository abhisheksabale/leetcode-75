from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    currsum = maxsum = sum(nums[:k])
    for i in range(k, len(nums)):
        currsum += nums[i] - nums[i - k]
        maxsum = max(maxsum, currsum)
    return maxsum / k

print(findMaxAverage([-1], 1))