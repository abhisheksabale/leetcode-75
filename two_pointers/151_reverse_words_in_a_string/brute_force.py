def reverseWords(s: str) -> str:
    temp = ""
    result = []
    s = remove_starting_whitespace(s)
    s = remove_trailing_whitespace(s)
    for i in range(len(s)):
        if s[i] != " ":
            temp += s[i]
        else:
            result.append(temp)
            temp = ""
    if temp != "":
        result.append(temp)
    result = [word for word in result if word]
    result = reverse_list(result)
    return " ".join(result)

def remove_starting_whitespace(s: str) -> str:
    for i in range(len(s)):
        if s[i] != " ":
            return s[i:]
    return s

def remove_trailing_whitespace(s: str) -> str:
    i = len(s) - 1
    while i >= -1:
        if s[i] != " ":
            return s[:i+1]
        i -= 1
    return s

def reverse_list(result: list[str]) -> list[str]:
    reversed_result = []
    i = len(result) - 1
    while i > -1:
        reversed_result.append(result[i])
        i -= 1
    return reversed_result



print(reverseWords("  hello   world  "))