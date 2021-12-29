from lib import binary_search


def test_case_2():
    assert 0 == binary_search.search([-1, 0, 3, 5, 9, 12], -1)

def test_case_3():
    assert 1 == binary_search.search([-1, 0, 3, 5, 9, 12], 0)

def test_case_4():
    assert 2 == binary_search.search([-1, 0, 3, 5, 9, 12], 3)

def test_case_5():
    assert 3 == binary_search.search([-1, 0, 3, 5, 9, 12], 5)

def test_case_6():
    assert 4 == binary_search.search([-1, 0, 3, 5, 9, 12], 9)

def test_case_7():
    assert 5 == binary_search.search([-1, 0, 3, 5, 9, 12], 12)

def test_case_8():
    assert -1 == binary_search.search([-1, 0, 3, 5, 9, 12], 2)

def test_case_9():
    assert -1 == binary_search.search([-1, 0, 3, 5, 9, 12], 4)

def test_case_10():
    assert -1 == binary_search.search([-1, 0, 3, 5, 9, 12], 8)

def test_case_11():
    assert -1 == binary_search.search([-1, 0, 3, 5, 9, 12], 13)