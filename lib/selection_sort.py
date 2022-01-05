
def find_smallest(nums):
    sml_idx = 0
    sml_item = nums[sml_idx]
    for idx, n in enumerate(nums):
        if n < sml_item:
            sml_idx = idx 
            sml_item = n
    return sml_idx


def selection_sort(nums):
    result = []
    for _ in range(len(nums)):
        sml_idx = find_smallest(nums)
        result.append(nums.pop(sml_idx))
    return result   
