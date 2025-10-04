class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        # Step 1: Clean up spaces in-place
        n = self.remove_extra_spaces(chars)

        # Step 2: Reverse the whole string
        self.reverse(chars, 0, n - 1)

        # Step 3: Reverse each word
        self.reverse_each_word(chars, n)

        return ''.join(chars[:n])

    def remove_extra_spaces(self, chars: list[str]) -> int:
        n = len(chars)
        i = 0  # read pointer
        j = 0  # write pointer

        while i < n and chars[i] == ' ':
            i += 1  # skip leading spaces

        while i < n:
            if i > 0 and chars[i] == chars[i - 1] == ' ':
                i += 1  # skip multiple spaces
                continue
            chars[j] = chars[i]
            i += 1
            j += 1

        # remove trailing space
        if j > 0 and chars[j - 1] == ' ':
            j -= 1

        return j  # new length

    def reverse(self, chars: list[str], left: int, right: int):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def reverse_each_word(self, chars: list[str], n: int):
        start = 0
        while start < n:
            end = start
            while end < n and chars[end] != ' ':
                end += 1
            self.reverse(chars, start, end - 1)
            start = end + 1
