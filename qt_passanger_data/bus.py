from passenger import Passengers

class Busses():   

    def __init__(self, bus_number, total_seats=0):
        self.total_seats = total_seats
        self.__current_seat_number = 0
        self.bus_number = bus_number
        self.total_passengers = {}
    
    def setCurrentSeatNumber(self, seatNumber):
        self.__current_seat_number = seatNumber

    def getCurrentSeatNumber(self):
        return self.__current_seat_number

    def getBusNumber(self):
        return self.bus_number

    def addPassengers(self, firstName, lastName, phoneNumber, boarding, destination, boardingTime):
        if self.getCurrentSeatNumber()<self.total_seats:
            passenger = Passengers(firstName, lastName, phoneNumber, boarding, destination, boardingTime)
            self.total_passengers[self.getCurrentSeatNumber()] = passenger.__repr__()
            self.setCurrentSeatNumber(self.getCurrentSeatNumber()+1)
            return "Passenger added:"
        else:
            return "Bus Full"

    def getAvailableSeats(self):
        return self.total_seats - self.__current_seat_number

    # def getPassengerList(self):
    #     for passenger in self.total_passengers:
    #         return passenger



    

    
