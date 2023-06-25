# Return the number of total permutations of the provided string that don't have repeated consecutive letters. 
# Assume that all characters in the provided string are each unique.
# For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), 
# but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.
def permuteNums(nums):
    result = []

    if (len(nums) == 1):
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permuteNums(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result

# print(permuteNums([1, 2, 3]))


def permuteStr(str):
    result = []

    if (len(str) == 1):
        return str

    for i in range(len(str)):
        s = str[0]
        str = str[i+1:]
        perms = permuteStr(str)

        for perm in perms:
            perms = s + perm
        result.append(perms)
        str += s

    return result

print(permuteStr("string"))


# s t r i n g
# g n i r t s
# 
# 
# 
# 
# 

# [1 2 3]

# for 0 1 2
#     n = 1
#     permute([2 3])
#     for 0 1
#  0      n = 2
#         permute([3]) = [[3]]
#         for 0
#             [3, 2]
#         [[3, 2]]
#         [3, 2]
#  1      n = 3
#         permute([2]) = [[2]]
#         for 0
#             [2, 3]
#         [[3, 2], [2, 3]]
#         [2, 3]
#     [[3, 2, 1], [2, 3, 1]]
#     [2, 3, 1]
#     then pop 2 and work on [3, 1]
