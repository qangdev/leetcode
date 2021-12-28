
from lib.first_bad_version import first_bad_version


def test_case_1():
    # [G,G,G,B,B]
    assert 4 == first_bad_version(5, [4,5])
    