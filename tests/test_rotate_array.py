from lib.rotate_array import rotate_array


def test_case_1():
    '''
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    '''
    result = rotate_array([1,2,3,4,5,6,7], 3)
    assert [5,6,7,1,2,3,4] == result
