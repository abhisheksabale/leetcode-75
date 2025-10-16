def isSubsequence(s: str, t: str) -> bool:
    lastFoundAt = 0
    currentWordAt = 0
    while lastFoundAt < len(t) and currentWordAt < len(s):
        if s[currentWordAt] == t[lastFoundAt]:
            currentWordAt += 1
        lastFoundAt += 1

    if currentWordAt == len(s):
        return True
    else:
        return False

print(isSubsequence("abc", "ahbgdc"))