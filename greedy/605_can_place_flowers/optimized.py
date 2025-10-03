class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        i = 0
        while i < length:
            if flowerbed[i] == 1:
                i += 2
            elif (i == length - 1 or flowerbed[i + 1] == 0) and (i == 0 or flowerbed[i - 1] == 0):
                count += 1
                i += 2
            else:
                i += 1
            if count >= n:
                return True
        return count >= n