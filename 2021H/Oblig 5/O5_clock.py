class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, min=0, sec=0):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        self.sec = sec

    def set_clock(self, day, month, year, hour, min, sec):  # behaves as __init__
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = min
        self.sec = sec

    def inc_second(self):  # increment seconds by ONE
        if self.sec <= 58:
            self.sec += 1
        else:
            self.inc_minutes()
            self.sec = 0

    def inc_minutes(self):  # ..by ONE
        if self.min <= 58:
            self.min += 1
        else:
            self.inc_hour()
            self.min = 0

    def inc_hour(self):  # etc..
        if self.hour <= 22:
            self.hour += 1
        else:
            self.inc_day()
            self.hour = 0

    def inc_day(self):  # ...you know the drill.
        if self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                if self.day <= 28:
                    self.day += 1
                else:
                    self.inc_month()
                    self.day = 1
            else:
                if self.day <= 27:
                    self.day += 1
                else:
                    self.inc_month()
                    self.day = 1
        elif (
            self.month == 1
            or self.month == 3
            or self.month == 5
            or self.month == 7
            or self.month == 8
            or self.month == 10
            or self.month == 12
        ):
            if self.day <= 30:
                self.day += 1
            else:
                self.inc_month()
                self.day = 1
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            if self.day <= 29:
                self.day += 1
            else:
                self.inc_month()
                self.day = 1

    def inc_month(self):  # ...bla bla bla.
        if self.month < 11:
            self.month += 1
        else:
            self.inc_year()
            self.month = 1

    def inc_year(self):
        self.year += 1

    def clock_as_string(self):
        return str(f"{self.day:02d}.{self.month:02d}.{self.year:04d} kl:{self.hour:02d}.{self.min:02d}.{self.sec:02d}")


if __name__ == "__main__":
    ...
