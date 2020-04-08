from core.passenger import Passengers

class Busses():   
    __current_seat_number = 1

    def __init__(self, bus_number, total_seats):
        self.total_seats = total_seats
        self.__bus_number = bus_number
        self.total_passengers = []
    
    def setCurrentSeatNumber(self, seatNumber):
        self.__current_seat_number = seatNumber

    def getCurrentSeatNumber(self):
        return self.__current_seat_number

    def getBusNumber(self):
        return self.__bus_number

    def addPassengers(self, firstName, lastName, phoneNumber, boarding, destination, boardingTime):
        if self.getCurrentSeatNumber()<self.total_seats:
            passenger = Passengers(firstName, lastName, phoneNumber, boarding, destination, 
                                    boardingTime, seatnumber=self.getCurrentSeatNumber)
            self.total_passengers.append(passenger)
            self.setCurrentSeatNumber(self.getCurrentSeatNumber()+1)
            return self.total_passengers
        else:
            return self.total_passengers

    def findBus(self, busNumber):
        return busNumber in self.getBusNumber()

    def getAvailableSeats(self):
        return self.total_seats - self.__current_seat_number

    # def getPassengerList(self):
    #     for passenger in self.total_passengers:
    #         return passenger



    

    
