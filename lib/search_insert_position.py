

def search_insert_position(nums, target):
    # Find the position of `target` in `nums` and then return if not then tell which position it will it was added
    _nums = nums.copy()
    target_pos = None
    target_ppos = -1 if nums else 0
    while _nums:
        mid = int(len(_nums)/2)
        if _nums[mid] == target:
            target_pos = nums.index(_nums[mid])
            break
        elif _nums[mid] < target:
            target_ppos = nums.index(_nums[mid]) + 1
            _nums = _nums[mid+1:]
        else:
            target_ppos = nums.index(_nums[mid])
            _nums = _nums[0:mid]
        target_ppos = target_ppos if target_ppos > 0 else 0
            
    if target_pos is not None:
        return target_pos
    elif target_ppos is not None:
        return target_ppos
    return None
