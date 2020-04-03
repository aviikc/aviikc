from passenger import Passengers
from bus import Busses

class TransportService():
    def __init__(self):
        self.available_busses = []
        # self.current_plying_buses = []

    def addBus(self, bus_number, seats):
        bus_available = Busses(bus_number, seats)
        self.available_busses.append(bus_available.getBusNumber())

    def getBusses(self):
        return self.available_busses
        

    # def make_current_plying_BusList(self):
    #     if len(self.current_plying_buses) != 0:
    #         for i in self.current_plying_buses:
    #             self.available_busses = self.total_number_of_busses.remove(i)
    #     else:
    #         self.available_busses = self.total_number_of_busses

    # def assign_bus(self, bus_number):
    #     if bus_number in total_number_of_busses:
    #         self.current_plying_buses.append(bus_number)
    #         self.available_busses.remove(bus_number)
    #     else:
    #         self.total_number_of_busses.append(bus_number)
    #         self.current_plying_buses.append(bus_number)
    #         self.available_busses.remove(bus_number)

    # def bus_depart(self, bus_number):
    #     if bus_number in total_number_of_busses:
    #         if bus_number in self.available_busses:
    #             self.available_busses.remove(bus_number)

    # def bus_arrive(self, bus_number):
    #     if bus_number in total_number_of_busses:
    #         if bus_number in self.available_busses:
    #             self.available_busses.append(bus_number)

        