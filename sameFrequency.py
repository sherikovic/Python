# Given two positive integers, find out if the two numbers have the same frequency of digits.
# this method will create two dicts, one for each number and compare them, very straightforward
# sameFrequency(182,281) // true
# sameFrequency(34,14)   // false
def sameFrequency(int1, int2):
    str1 = str(int1)
    str2 = str(int2)
    if len(str1) != len(str2):
        print("Invalid input")
    else:
        unqdict1 = {}
        for st in str1:
            if st not in unqdict1.keys():
                unqdict1[st] = 1
            else:
                unqdict1[st] += 1
        unqdict2 = {}
        for st in str2:
            if st not in unqdict2.keys():
                unqdict2[st] = 1
            else:
                unqdict2[st] += 1
        if unqdict1 == unqdict2:
            print("True")
        else:
            print("False")

sameFrequency(121826,126122)