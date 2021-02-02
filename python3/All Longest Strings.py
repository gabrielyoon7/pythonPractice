def allLongestStrings(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    print(m)
    return r
inputArray = ["kyonggi", "university", "turtle", "project", "pype"]
print(allLongestStrings(inputArray))
