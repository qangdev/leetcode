from lib.selection_sort import selection_sort


def test_case_1():
    # Input: nums = [6,5,4,3,2,1,0]
    # Output: [0,1,2,3,4,5,6]
    result = selection_sort([6,5,4,3,2,1,0])
    assert [0,1,2,3,4,5,6] == result 

