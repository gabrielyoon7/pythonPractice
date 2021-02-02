def commonCharacterCount(s1, s2):
    global com
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)
s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))
