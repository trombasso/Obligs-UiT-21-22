from datetime import datetime


# Main class, containing all input data. Single Flight info.
class Flight:
    def __init__(self, flight_number, departure_time, arrival_time):
        self.__flight_number = flight_number
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time

    @property  # getter
    def flight_number(self):
        return self.__flight_number

    @property  # getter
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property  # getter
    def arrival_time(self):
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value

    # Calculating total flight time for single flight.
    def get_flight_time(self):
        hour_s, min_s, sec_s = self.departure_time.hour, self.departure_time.minute, self.departure_time.second
        hour_e, min_e, sec_e = self.arrival_time.hour, self.arrival_time.minute, self.arrival_time.second

        total_flight_time = ((hour_e - hour_s) * 60) + (min_e - min_s) + (sec_e - sec_s)

        return int(total_flight_time)


# Handling data from all flights, travel-time and flight-time.
class Itinerary:
    def __init__(self, flights):
        self.flights = flights

    def get_total_travel_time(self):
        latest_arrival = 0.0
        earliest_departure = 1440.1

        # Find the earliest and latest flight by adding up h.m.s comparing all flights.
        for i in range(0, len(self.flights)):
            lis1 = self.flights[i]
            hour_dep, min_dep, sec_dep = (
                lis1.departure_time.hour,
                lis1.departure_time.minute,
                lis1.departure_time.second,
            )
            hour_arr, min_arr, sec_arr = (
                lis1.arrival_time.hour,
                lis1.arrival_time.minute,
                lis1.arrival_time.second,
            )
            departure_time = hour_dep * 60 + min_dep + sec_dep / 60
            arrival_time = hour_arr * 60 + min_arr + sec_arr / 60

            if departure_time < earliest_departure:
                earliest_departure = departure_time

            if arrival_time > latest_arrival:
                latest_arrival = arrival_time

        # calculate total travel time and return result
        return int(latest_arrival - earliest_departure)

    # Total flight-time from class Flights, def get_flight-time.
    # List comp, iterating over all flights.
    def get_total_flight_time(self):
        minutes_flight_time = [Flight.get_flight_time(self.flights[i]) for i in range(0, len(self.flights))]
        return sum(minutes_flight_time)


def main():
    # Input from assignement.
    flights = []
    flights.append(Flight("US230", datetime(2014, 4, 5, 5, 5, 0), datetime(2014, 4, 5, 6, 15, 0)))
    flights.append(Flight("US235", datetime(2014, 4, 5, 6, 55, 0), datetime(2014, 4, 5, 7, 45, 0)))
    flights.append(Flight("US237", datetime(2014, 4, 5, 9, 35, 0), datetime(2014, 4, 5, 12, 55, 0)))
    itinerary = Itinerary(flights)

    print(f"Total travel time: {itinerary.get_total_travel_time()}")
    print(f"Total flight time: {itinerary.get_total_flight_time()}\n")


if __name__ == "__main__":
    main()
