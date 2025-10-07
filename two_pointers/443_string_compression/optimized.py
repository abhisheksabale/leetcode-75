class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_string = ""
        count = 1
        for i in range(len(chars)):
            if i == len(chars)-1:
                compressed_string += chars[i]
                if count > 1:
                    compressed_string += str(count)
            elif chars[i] == chars[i+1]:
                count += 1
            else:
                compressed_string += chars[i]
                if count > 1:
                    compressed_string += str(count)
                count = 1

        for i in range(len(compressed_string)):
            chars[i] = compressed_string[i]

        return len(compressed_string)