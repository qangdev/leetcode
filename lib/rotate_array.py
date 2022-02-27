

def rotate_array(nums, k):
    for _ in range(0, k):
        x = nums.pop()
        nums.insert(0, x)
    return nums
