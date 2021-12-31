import random


def sort_squares(nums):
    # if "sqr" not in nums:
    #     nums = [n*n for n in nums]
    #     nums.append("sqr")
    if not nums:
        return []
    # Sort with `quick sort` and square num during sorting
    mid = nums.pop(random.randrange(len(nums)))
    right = []
    left = []
    for n in nums:
        if n < mid:
            left.append(n)
        else:
            right.append(n)
    return sort_squares(left) + [mid*mid] + sort_squares(right)
 