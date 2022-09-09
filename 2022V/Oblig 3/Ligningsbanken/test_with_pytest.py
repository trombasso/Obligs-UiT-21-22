# test_with_pytest.py
import ligningsbanken

# from ligningsbanken import eq2text, make_eq, make_n_eqs, make_test, ok


class Test_collection:
    def test_eq2text(self):
        assert ligningsbanken.eq2text([1, 2, 3, 4]) == "x + 2 = 3x + 4"

    def test_make_eq(self):
        assert len(ligningsbanken.make_eq()) == 4

    def test_make_n_eqs(self):
        assert len(ligningsbanken.make_n_eqs(4)) == 4

    def test_ok(self):
        assert ligningsbanken.ok([0, 2, 3, 4]) is False
        assert ligningsbanken.ok([1, 0, 3, 4]) is False
        assert ligningsbanken.ok([1, 2, 0, 4]) is False
        assert ligningsbanken.ok([1, 2, 3, 0]) is False
        assert ligningsbanken.ok([1, 2, 1, 4]) is False
        assert ligningsbanken.ok([1, 2, 3, 2]) is False
        assert ligningsbanken.ok([1, 2, 3, 4]) is True

    def test_make_tests(self):
        students = ["Erik", "Laila"]
        dict = ligningsbanken.make_test(students, 1)
        for i in dict.keys():
            assert i == "Erik" or "Laila"


if __name__ == "__main__":
    pass
