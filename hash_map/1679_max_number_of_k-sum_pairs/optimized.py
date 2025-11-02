from typing import List
from collections import defaultdict

def maxOperations(nums: List[int], k: int) -> int:
    hash_map = defaultdict(int)
    pairs = 0
    for num in nums:
        if hash_map[k - num] > 0:
            pairs += 1
            hash_map[k - num] -= 1
        else:
            hash_map[num] += 1

    return pairs

print(maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))