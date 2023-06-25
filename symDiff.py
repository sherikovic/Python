#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference
#This function should return the intersection between two lists or more
def resolveArrays(*lists):
    if len(lists)<=1:
        print("Input has to be more than one list")
    else:
        C = []
        for i in range(len(lists)):
            A = C
            B = lists[i]
            C = []
            [C.append(x) for x in A if x not in B]
            [C.append(x) for x in B if x not in A]
        #remove duplicates
        D = []
        for c in C:
            if c not in D:
                 D.append(c)

#        C = list(set(C))
        print(sorted(D))
"""         for c in range(len(C)):
            if c is not len(C):
                if C[c] in C[c+1:]:
                    del C[c] """

resolveArrays([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
