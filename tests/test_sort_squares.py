from lib.sort_squares import sort_squares


def test_case_0():
    # Input: nums = [4,7,1,8,0,3]
    # Output: [0,1,3,4,7,8]
    result = sort_squares([4,7,1,8,0,3])
    assert [0,1,9,16,49,64] == result


def test_case_1():
    # Input: nums = [-4,-1,0,3,10]
    # Output: [0,1,9,16,100]
    result = sort_squares([-4,-1,0,3,10])
    assert [0,1,9,16,100] == result
