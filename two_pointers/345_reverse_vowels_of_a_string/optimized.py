class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U'}
        n = len(s)
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < n and s[left] not in vowels:
                left += 1
            while right > -1 and s[right] not in vowels:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)