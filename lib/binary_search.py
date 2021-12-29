from typing import List


def search(nums: List[int], target: int) -> int:
    _nums = nums.copy()
    while _nums:
        mid = int(len(_nums)/2)
        if _nums[mid] == target:
            return nums.index(_nums[mid])
        elif _nums[mid] > target:
            _nums = _nums[:mid]
        else:
            _nums = _nums[mid+1:]
    return -1
