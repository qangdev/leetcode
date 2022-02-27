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


def test_case_2():
    '''
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    '''
    result = rotate_array([-1,-100,3,99], 2)
    assert [3,99,-1,-100] == result