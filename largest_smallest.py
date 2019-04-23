# How do you find the largest and smallest number in an unsorted integer array?

num = [5, 3, 8, 2, 4, 7, 9, 6, ]


def findLargestSmallest(A):
    small = min(A)
    large = max(A)

    print('The smallest number is ' + str(small))
    print('The largest number is ' + str(large))


findLargestSmallest(num)
