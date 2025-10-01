class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        cutoff = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= cutoff)
        return result