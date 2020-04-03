#main modules
import sys,os
#local modules
from run_service import TransportService
from bus import Busses
from passenger import Passengers
#pyqt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDateTime
#ui imports
from passenger_dialog import Ui_Dialog as passDialog
from add_bus import Ui_Dialog as busDialog
from primary_dialog01 import Ui_Dialog as primDialog 


class ApplicationWindow(QDialog):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = primDialog()
        self.ui.setupUi(self)
        self.busList = {}
        self.current_available_seats = 0
        self.disable_buttons_when_noBus()
        self.ui.comboBox.addItems(self.busList)
        self.ui.pushButton.clicked.connect(self.addPassanger)
        self.ui.pushButton_3.clicked.connect(self.addBus)
        self.ui.comboBox.currentIndexChanged.connect(self.availableSeatsPopulate)

    
    def disable_buttons_when_noBus(self):
        # self.ui.comboBox.currentText()
        if self.ui.comboBox.currentText() == "" or int(self.ui.label_seat_available.text()) == 0:
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)            
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            # self.disable_buttons_when_noBus()

    # def disable_buttons_when_noSeats(self):
    #     # print(int(self.ui.label_seat_available.text())>0)
    #     if int(self.ui.label_seat_available.text())>0:
    #         self.ui.pushButton.setEnabled(True)
    #         # self.disable_buttons_when_noBus()
    #     else:
    #         self.ui.pushButton.setEnabled(False)
    #         # self.disable_buttons_when_noBus()
                   
    def availableSeatsPopulate(self):
        self.current_available_seats = self.busList[str(self.ui.comboBox.currentText())]
        self.ui.label_seat_available.setText(str(self.current_available_seats ))
        if int(self.busList[self.ui.comboBox.currentText()])-1 > 0:
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)

    def addPassanger(self):
        self.current_bus_number = self.ui.comboBox.currentText()
        self.newWindow = AddPassengerDialog()
        self.newWindow.passanger_info.connect(self.passenger_info_gather)
        if self.newWindow.exec_() == QDialog.accepted:
            print("wwwww")
    
    def addBus(self):
        self.newWindow = AddBusDialog()
        self.newWindow.bus_number.connect(self.myEvent)
        # self.newWindow.bus_seats.connect(self.myEvent)
        if self.newWindow.exec_() == QDialog.accepted:
            print("ok")


    @pyqtSlot(dict)
    def myEvent(self, n):
        self.busList.update(n)
        for key, value in n.items():
            self.ui.comboBox.addItem(key)
        self.disable_buttons_when_noBus()

    @pyqtSlot(dict)
    def passenger_info_gather(self, m):
        #self.disable_buttons_when_noSeats()
        get_bus_number = self.ui.comboBox.currentText()
        if int(self.busList[get_bus_number])-1 > 0:
            self.busList[get_bus_number] = self.busList[get_bus_number] - 1
            available_seats = self.busList[get_bus_number]
            self.current_available_seats = available_seats
            self.ui.label_seat_available.setText(str(self.current_available_seats ))
        else:
            self.ui.pushButton.setEnabled(False)
        print(self.busList)
        print(m)

class AddPassengerDialog(QDialog):
    passanger_info = pyqtSignal(dict)
    def __init__(self):
        super(AddPassengerDialog, self).__init__()
        self.ui = passDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.addPassenger)

    def addPassenger(self):
        fname = self.ui.lineEdit.text()
        lname = self.ui.lineEdit_2.text()
        phone_number = self.ui.lineEdit_5.text()
        boarding = self.ui.lineEdit_3.text()
        dest = self.ui.lineEdit_4.text()
        boarding_time = self.ui.dateTimeEdit.dateTime().toPyDateTime()
        passenger = Passengers(fname, lname, phone_number, boarding, dest, boarding_time)
        self.passanger_info.emit(passenger.__repr__())

class AddBusDialog(QDialog):
    bus_number = pyqtSignal(dict)

    def __init__(self):
        super(AddBusDialog, self).__init__()
        self.ui = busDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.addNewBus)

    def addNewBus(self):
        newBusNumber = self.ui.lineEdit.text()
        total_seats = int(self.ui.spinBox.value())
        self.bus_number.emit({newBusNumber: total_seats})
        self.close()

def main():
    app = QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()