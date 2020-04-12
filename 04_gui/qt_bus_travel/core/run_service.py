from core.passenger import Passengers
from core.bus import Busses

class TransportService():
    def __init__(self):
        self.__available_busses = []
        # self.current_plying_buses = []

    def getAvailableBuses(self):
        return self.__available_busses

    def addBus(self, bus_number, seats):
        bus_available = Busses(bus_number, seats)
        self.__available_busses.append(bus_available)

    def loadBus(self, bus_number, **kwargs):
        for key in kwargs:
            if key == "firstName" or key == "lastName" or key == "phoneNumber"  or key =="boarding"  or key =="destination"  or key =="boardingTime"  or key =="seatnumber":
                for i in i in self.getAvailableBuses():
                    if i.getBusNumber == bus_number:
                        newDict={}
                        newDict.update(key = kwargs[key])
            i.addPassengers(**newDict)
        return 1



        

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

        