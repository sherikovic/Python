# Accepts a string and returns the length of the longest substring with all distinct characters.
# findLongestSubstring('') // 0
# findLongestSubstring('rithmschool') // 7
# findLongestSubstring('thisisawesome') // 6
# findLongestSubstring('thecatinthehat') // 7
# findLongestSubstring('bbbbbb') // 1
def findLongestSubstring(string):
    i = 0
    j = 0
    maxLen = 0
    strdict = {}
    while (j < len(string)):
        if string[i] not in strdict.keys():
            strdict[string[i]] = 1
            if i is not len(string)-1:
                i += 1
        else:
            maxLen = max(maxLen, abs(j-i))
            strdict = {}
            j += 1
            i = j
    print(maxLen)

findLongestSubstring('')
findLongestSubstring('rithmschool')
findLongestSubstring('thisisawesome')
findLongestSubstring('thecatinthehat')
findLongestSubstring('bbbbbb')
