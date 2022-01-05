

def rotate_array(nums, k):
    l, r = 0, k + 1
    for i in range(0, k):
        print(">", i)
        li = nums[l]
        ri = nums[r]
        print(li, ri, "|", l, r)
        nums[l] = ri
        nums[r] = li
        print(nums)
        l += 1
        r += 1
    return nums
