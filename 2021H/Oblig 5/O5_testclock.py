from O5_clock import Clock  # The code to test
import unittest  # The test framework


class Test_Clock(unittest.TestCase):
    def setUp(self):
        self.__clock = Clock()

    def test_inc_sec_from_default_values(self):
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:00.00.01")

    def test_inc_min_from_default_values(self):
        self.__clock.inc_minutes()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:00.01.00")

    def test_inc_hour_from_default_values(self):
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:01.00.00")

    def test_inc_day_from_default_values(self):
        self.__clock.inc_day()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:00.00.00")

    def test_inc_month_from_default_values(self):
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "00.01.0000 kl:00.00.00")

    def test_inc_year_from_default_values(self):
        self.__clock.inc_year()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0001 kl:00.00.00")

    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01.02.2021 kl:00.00.00")

    def test_inc_sec_from_midnight_desember(self):
        self.__clock = Clock(31, 12, 2000, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01.01.2001 kl:00.00.00")

    def test_inc_sec_from_midnight_february_leap_year_2000(self):
        self.__clock = Clock(28, 2, 2000, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "29.02.2000 kl:00.00.00")

    def test_inc_sec_from_midnight_february_leap_year_2024(self):
        self.__clock = Clock(28, 2, 2024, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "29.02.2024 kl:00.00.00")

    def test_inc_sec_from_midnight_february_leap_year_2100(self):
        self.__clock = Clock(28, 2, 2100, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01.03.2100 kl:00.00.00")


if __name__ == "__main__":
    unittest.main()
