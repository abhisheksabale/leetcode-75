class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fin = []
        length = min(len(word1), len(word2))
        for i in range(length):
            fin.append(word1[i])
            fin.append(word2[i])
        if len(word1) > length:
            fin.append(word1[length:])
        if len(word2) > length:
            fin.append(word2[length:])
        return "".join(fin)