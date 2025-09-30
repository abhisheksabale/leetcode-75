def gcdOfStrings(str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        count = 0
        result = ""
        for i in range(len1):
            for j in range(len2):
                candidate = str1[i:j+i+1]
                temp_count = str2.count(candidate)
                if temp_count >= count:
                    result = candidate
        return result

print('Result: ' + gcdOfStrings("ABAB", "AB"))