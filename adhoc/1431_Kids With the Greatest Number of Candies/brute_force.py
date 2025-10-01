def kidsWithCandies(candies: [int], extraCandies: int) -> [bool]:
    result = []
    cutoff = max(candies)
    for candy in candies:
        if candy + extraCandies >= cutoff:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies([2,3,5,1,3], 3))