# Bit Hacks – Part 1 (Basic)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Check if an integer is odd or even
def checkIfNumIsEvenOrOdd(num):
    if num & 1 != 0:
        print("Num is odd")
    else:
        print("Num is even")


# num = 23
# checkIfNumIsEvenOrOdd(num)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Detect if two integers have opposite signs or not
def detectIfTwoNumsHaveOppositeSigns(num1, num2):
    if num1 ^ num2 < 0:
        print("Opposite signs")
    else:
        print("Similar signs")


# detectIfTwoNumsHaveOppositeSigns(4, -8)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Add 1 to an integer
def addOneToANum(num):
    print(-~num)


# addOneToANum(3)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Swap two numbers without using any third variable
def swapNumbers(num1, num2):
    print(num1, num2)
    print("..became..")
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print(num1, num2)


# swapNumbers(5, 1)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
