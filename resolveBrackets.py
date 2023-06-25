# scan the string
# stack = [{[]
# if in opening add them to stack
# if in closing, pop from stack
# and compare if those are at the same indexes
def resolveBrackets(str):
    opening_brackets = tuple('([{')
    closing_brackets = tuple(')]}')
    i = 0
    stack = []
    while i < len(str):
        if str[i] in opening_brackets:
            stack.append(str[i])
            i += 1
        elif str[i] in closing_brackets:
            if opening_brackets.index(stack.pop()) == closing_brackets.index(str[i]):
                i += 1
            else:
                return False
    if stack:
        return False
    else:
        return True


# solution with a dict
# dict = {'(' : ')', 
#         '[' : ']',
#         '{' : '}'
#        }
def resolveBrackets_dict(str):
    opening_brackets = tuple('([{')
    closing_brackets = tuple(')]}')
    brktdict = dict(zip(closing_brackets, opening_brackets))
    stack = []
    for st in str:
        if st in opening_brackets:
            stack.append(st)
        elif st in closing_brackets:
            if not stack or brktdict[st] != stack.pop():
                return False
    if stack:
        return False
    else:
        return True


str = "{[]{()}}"
print(resolveBrackets_dict(str))
