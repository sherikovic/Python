######### FREQUENCY COUNTER #########
# This method would avoid nested loops and break them down to two loops instead, create dicts from each loop 
# and compare them
# This function checks the frequency of:
#   1. if numbers: each number in the input list has to be squared in the output list while having the same frequency
#   2. if strings: each char in the input string has to exist in the output string as well, the order doesn't matter, also while keeping the frequency (anagrams)
def same(inpList, oupList):
    if len(inpList) is not len(oupList):
        print("The two arrays don't match in length!")
    else:
        if all([isinstance(item, int) for item in inpList]):
            inpFreq = {}
            oupFreq = {}
            for num in inpList:
                if num in inpFreq.keys():
                    inpFreq[num] += 1
                else:
                    inpFreq[num] = 1
            for num in oupList:
                if num in oupFreq.keys():
                    oupFreq[num] += 1
                else:
                    oupFreq[num] = 1
            for key in inpFreq.keys():
                if key*key not in oupFreq.keys():
                    return False
                if inpFreq[key] is not oupFreq[key*key]:
                    return False
            return True
        elif all([isinstance(item, str) for item in inpList]):
            for i in range(len(inpList)):
                inpstr = inpList[i]
                oupstr = oupList[i]
                if len(inpstr) is not len(oupstr) or list(oupstr).sort() != list(inpstr).sort():
                    return False
            return True

# this is just a helper function, not used
def getItemCountInAList(userList, item):
    itemsCount = {}
    for i in range(len(userList)):
        if userList[i] in itemsCount:
            itemsCount[userList[i]] += 1
        else:
            itemsCount[userList[i]] = 1
    return itemsCount[item]

print(same(["sherif", "amr"], ["sehirf", "arm"]))
print(same([2, 4, 5, 2], [25, 4, 16, 4]))
