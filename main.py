# AddTwo Sum Integers

"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
If no two numbers sum up to the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array:
you can't add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers summing up to the target sum.
"""
# Redone Algorithms for understanding

# Solution 1 - With a hashTable
def addTwoSum(array, targetSum):
    hashTable = {}
    for num in array:
        if targetSum - num in hashTable:
            return [targetSum - num, num]
        else:
            hashTable[num] = True
    return []


# Solution 2 - Left/Right Pointers
def addTwoSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left != right:
        currentSum = array[left] + array[right]
        if currentSum > targetSum:
            right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            return [array[left], array[right]]
    return []

