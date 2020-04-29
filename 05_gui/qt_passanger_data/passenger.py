from datetime import datetime

class Passengers():
    def __init__(self, firstName, lastName, phoneNumber, boarding, destination, boardingTime):
        self.passName = self.setfullName(firstName, lastName)
        self.boarding = boarding
        self.destination = destination
        self.phone_number = phoneNumber
        self.boarding_time = boardingTime

    def getTime(self, boardingTime):
#boarding time should be of the format '09/19/18 13:55'
        return datetime.strptime(boardingTime, '%m-%d-%y %H:%M')

    def getTimeString(self):
        return self.boarding_time.strftime("%m/%d/%Y, %H:%M")

    def setfullName(self, fName, lName):
        return fName + " " + lName

    def getFullName(self):
        return self.passName

    def __repr__(self):
        return {
            "Name":self.passName,
            "Phone Number": self.phone_number,
            "Boarding Location": self.boarding,
            "Destination": self.destination,
            "Boarding Time": self.getTimeString(),
            # "Seat Number" : self.seatNumber + 1
        }
    