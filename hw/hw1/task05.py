"""Homework 1.5.

Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""

from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Find the maximum sum of elements of a sub-array of a given length k.

    Args:
        nums: array
        k: sub-array length

    Returns:
        The return value. maximum sum sub-array
    """
    length = k
    max_sum = -float("inf")
    while length > 0:
        for i in range(len(nums) + 1 - k):
            sum_subset = sum(nums[0 + i : k + i])
            if sum_subset > max_sum:
                max_sum = sum_subset
        length -= 1
    return max_sum
