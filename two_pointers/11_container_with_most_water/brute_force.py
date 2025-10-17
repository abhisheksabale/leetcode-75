from typing import List

def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    result = 0
    while i < j:
        breadth = height[i] if height[i] < height[j] else height[j]
        length = j - i
        area = length * breadth
        if area > result:
            result = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))