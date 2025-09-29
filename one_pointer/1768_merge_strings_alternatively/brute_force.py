class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fin = []
        if len(word1) > len(word2):
            length = len(word1)
        else:
            length = len(word2)
        for i in range(length):
            if i < len(word1):
                fin.append(word1[i])
            if i < len(word2):
                fin.append(word2[i])
        return "".join(fin)