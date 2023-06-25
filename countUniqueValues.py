######### MULTIPLE POINTERS #########
# This function will use that method to decrease the number of iterations to find the unique values in a sorted list
# THe main twist here is to SORT the args first and then work on the items as pairs
def countUniqueValues(listOfValues):
    if listOfValues != sorted(listOfValues):
        print("List is not sorted")
    else:
        i = 0
        for j in range(i+1, len(listOfValues)):
            if listOfValues[i] is not listOfValues[j]:
                i += 1
                listOfValues[i] = listOfValues[j]
        return i

print(countUniqueValues([1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 99]))
