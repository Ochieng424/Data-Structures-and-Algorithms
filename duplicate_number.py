# How do you find the duplicate number on a given integer array?

from collections import Counter

num = [1, 2, 4, 4, 4, 5, 6, 6, 8, 9, 10, 10]


def findDuplicateNum(A):
    count = Counter(A)
    for key, value in count.items():
        if value > 1:
            print('The number ' + str(key) + ' appears ' + str(value) + ' times')


findDuplicateNum(num)


