"""
Write a Python function to find a distinct pair of numbers
whose product is odd from a sequence of integer values.
"""


def get_odd_pairs(nums):
    result = []
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            num1 = nums[x]
            num2 = nums[y]
            if num1 * num2 % 2 == 1:
                result.append((num1, num2))

