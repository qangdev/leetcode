from lib.search_insert_position import search_insert_position



def test_case_1():
    assert 2 == search_insert_position([1,3,5,6], 5)


def test_case_2():
    assert 1 == search_insert_position([1,3,5,6], 2)


def test_case_3():
    assert 4 == search_insert_position([1,3,5,6], 7)


def test_case_4():
    assert 0 == search_insert_position([], 2)


def test_case_5():
    assert 0 == search_insert_position([1,3,5,6], 0)


def test_case_6():
    assert 1 == search_insert_position([1,3,5,6], 3)


def test_case_7():
    assert 3 == search_insert_position([1,3,5,6], 6)


def test_case_8():
    assert 1 == search_insert_position([1,3], 2)


def test_case_9():
    assert 2 == search_insert_position([1,3,5], 4)


def test_case_10():
    assert 1 == search_insert_position([1,3,5], 2)


def test_case_11():
    assert 3 == search_insert_position([1,3,5,7], 6)