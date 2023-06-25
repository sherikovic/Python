# This function takes in two strings and checks whether the characters in the first string form a subsequence 
# of the characters in the second string.
# In other words, the function should check whether the characters in the first string appear somewhere 
# in the second string, without their order changing.
# isSubsequence('hello', 'hello world'); // true
# isSubsequence('sing', 'sting'); // true
# isSubsequence('abc', 'abracadabra'); // true
# isSubsequence('abc', 'acb'); // false (order matters)
# Multiple pointers O(N + M)
def isSubsequence(str1, str2):
    i = 0
    for j in range(len(str2)):
        if str1[i] == str2[j]: 
            i += 1
        if i == len(str1):
            return True
    return False
  
print(isSubsequence("str", "srting"))
