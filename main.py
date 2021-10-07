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
# Soultion 1 with HashTable

def addTwoSum(array, targetSum):
    hashtable = {}
    for num in array:
        if targetSum - num in hashtable:
            return [targetSum - num, num]
        else:
            hashtable[num] = True
    return []


# Solution  2 with Left/Right Pointesr
def addTwoSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left != right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return[array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []

