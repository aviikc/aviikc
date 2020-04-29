import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal, pyqtSlot


from core.run_service import TransportService
#ui imports
from ui.passenger_dialog import Ui_Dialog as passDialog
from ui.add_bus import Ui_Dialog as busDialog
from ui.primary_dialog01 import Ui_Dialog as primDialog 



class ApplicationWindow(QDialog):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = primDialog()
        self.ui.setupUi(self)
        self.disable_buttons_when_noBus()
        self.ui.pushButton.clicked.connect(self.addPassanger)
        self.ui.pushButton_3.clicked.connect(self.addBus)

    def disable_buttons_when_noBus(self):
        if self.ui.comboBox.currentText() == "":
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)            
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)

    def updateBusDropDown(self, bus_number):
        self.ui.comboBox.addItem(bus_number)

    def addPassanger(self):
        self.current_bus_number = self.ui.comboBox.currentText()
        self.newWindow = AddPassengerDialog()

    def addBus(self):
        self.newWindow = AddBusDialog()
        self.newWindow.bus_info.connect(self.busInfoBridge)
        if self.newWindow.exec_() != 1:
            print("ok")    

    @pyqtSlot(dict)
    def busInfoBridge(self, m):
        print(m)

class AddPassengerDialog(QDialog):
    # passanger_info = pyqtSignal(dict)
    def __init__(self):
        super(AddPassengerDialog, self).__init__()
        self.ui = passDialog()
        self.ui.setupUi(self)

class AddBusDialog(QDialog):
    bus_info = pyqtSignal(dict)

    def __init__(self):
        super(AddBusDialog, self).__init__()
        self.ui = busDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.addNewBus)

    def addNewBus(self):
        newBusNumber = self.ui.lineEdit.text()
        total_seats = int(self.ui.spinBox.value())
        self.bus_info.emit({newBusNumber: total_seats})


def main():
    app = QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()