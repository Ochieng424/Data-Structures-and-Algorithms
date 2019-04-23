# How do you find the missing number in a given integer array of 1 to n?

num = [1, 2, 3, 4, 6, 7, 8, 9]


def findMissingNum(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sumOfA = sum(A)

    print(total-sumOfA)


findMissingNum(num)
