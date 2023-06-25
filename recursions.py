def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

# print(power(2, 4))


def factorial(num):
    if num <=1:
        return 1
    else:
        return num * factorial(num-1)

# print(factorial(4))


def productOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1, 2, 3, 4, 5]))

def recursiveRange(num):
    if num == 0:
        return 0
    else:
        return num + recursiveRange(num-1)

# print(recursiveRange(3))


# returns the nth number in the Fibonacci sequence
# fib(4) // 3
# fib(10) // 55 add 9th and 10th
# fib(28) // 317811
# fib(35) // 9227465
# O(2^N) - so not good
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

# O(N)
def fib_memo(n):
    def recurse(n, memo={}):
        if n in memo: return memo[n]
        if n <= 2: return 1
        memo[n] = recurse(n-1, memo) + recurse(n-2, memo)
        return memo[n]
    return recurse(n)

print(fib_memo(100))

# reverse('awesome') // 'emosewa'
def reverse(str):
    if str == "":
        return ""
    else:
        return str[len(str)-1] + reverse(str[:-1])

# print(reverse("awesome"))

def isPalindrome(str):
    if str == "":
        return ""
    else:
        if len(str) == 1:
            return True
        else:
            if str[len(str)-1] == str[0]:
                isPalindrome(str[1:-1])
                return True
            else:
                return False

# print(isPalindrome("awesome"))
# print(isPalindrome("tacocat"))

arr=[2, 5, 3, 1, 23, 14]
# arr.sort()
# print(sorted([2, 5, 3, 1, 23, 14]))
# print(sorted(["alosd", "fbad", "bsad", "zinda", "cdfsg"]))