# Accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in
# Implement it with both the frequency counter pattern and multiple pointers
# areThereDuplicates(1, 2, 3) // false
# areThereDuplicates(1, 2, 2) // true
# areThereDuplicates('a', 'b', 'c', 'a') // true

def areThereDuplicates_FC(*args):
    if len(args) == 1:
        print("Invalid input")
    else:
        lookup = {}
        for arg in args:
            if arg in lookup.keys():
                lookup[arg] += 1
            else:
                lookup[arg] = 1
        if any([value > 1 for value in lookup.values()]):
            return True
        else:
            return False

print(areThereDuplicates_FC(1, 4, 4, 3, 5))
print(areThereDuplicates_FC('a', 'c', 'b'))


def areThereDuplicates_MP(*args):
    if len(args) == 1:
        print("Invalid input")
    else:
        args = sorted(list(args))
        i = 0
        for j in range(i+1, len(args)):
            if args[i] is not args[j]:
                i += 1
            else:
                return True
        return False

print(areThereDuplicates_MP(1, 4, 4, 3, 5))
print(areThereDuplicates_MP('a', 'c', 'b'))


#ONE LINER
def areThereDuplicates_OL(*args):
    return not sorted(list(args)) == sorted(set(list(args)))

print(areThereDuplicates_OL(1, 4, 4, 3, 5))
print(areThereDuplicates_OL('a', 'c', 'b'))
