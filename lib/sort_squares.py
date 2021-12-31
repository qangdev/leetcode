import random


def find_smallest(nums):
    sml_idx = 0
    sml_item = nums[sml_idx]
    for idx, n in enumerate(nums):
        if n < sml_item:
            sml_idx = idx
            sml_item = nums[idx]
    return sml_idx


def sort_squares(nums):
    result = []
    sqr_nums = [n*n for n in nums]
    for _ in range(len(nums)):
        sml_idx = find_smallest(sqr_nums)
        result.append(sqr_nums.pop(sml_idx))
    return result
 