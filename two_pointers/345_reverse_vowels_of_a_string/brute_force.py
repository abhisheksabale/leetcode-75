def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def is_vowel(char):
        return char in vowels

    resultList = list(s)
    i = 0
    j = len(resultList) - 1
    while i < j:
        if is_vowel(resultList[i]) and not is_vowel(resultList[j]):
            j -= 1
        elif not is_vowel(resultList[i]) and is_vowel(resultList[j]):
            i +=1
        elif is_vowel(resultList[i]) and is_vowel(resultList[j]):
            resultList[i], resultList[j] = resultList[j], resultList[i]
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1

    return ''.join(resultList)

print(reverseVowels("leetcode"))