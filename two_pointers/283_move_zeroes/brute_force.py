from typing import List


def moveZeroes(nums: List[int]) -> None:
    lastZeroFoundAt = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastZeroFoundAt] = nums[i]
            lastZeroFoundAt += 1

    for i in range(lastZeroFoundAt, len(nums)):
        nums[i] = 0

inp = [0,1,0,3,12]
moveZeroes(inp)
print(inp)