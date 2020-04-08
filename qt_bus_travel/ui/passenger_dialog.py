# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passenger_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 268)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_firstName = QtWidgets.QLabel(Dialog)
        self.label_firstName.setGeometry(QtCore.QRect(20, 31, 101, 16))
        self.label_firstName.setObjectName("label_firstName")
        self.label_lastName = QtWidgets.QLabel(Dialog)
        self.label_lastName.setGeometry(QtCore.QRect(20, 64, 101, 16))
        self.label_lastName.setObjectName("label_lastName")
        self.label_Boarding_Location = QtWidgets.QLabel(Dialog)
        self.label_Boarding_Location.setGeometry(QtCore.QRect(20, 97, 101, 16))
        self.label_Boarding_Location.setObjectName("label_Boarding_Location")
        self.label_dest = QtWidgets.QLabel(Dialog)
        self.label_dest.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_dest.setObjectName("label_dest")
        self.label_phn = QtWidgets.QLabel(Dialog)
        self.label_phn.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_phn.setObjectName("label_phn")
        self.label_Boarding_time = QtWidgets.QLabel(Dialog)
        self.label_Boarding_time.setGeometry(QtCore.QRect(20, 190, 101, 16))
        self.label_Boarding_time.setObjectName("label_Boarding_time")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 271, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 271, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 90, 271, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 120, 271, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 150, 181, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(160, 190, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_firstName.setText(_translate("Dialog", "First Name"))
        self.label_lastName.setText(_translate("Dialog", "Last Name"))
        self.label_Boarding_Location.setText(_translate("Dialog", "Boarding Location"))
        self.label_dest.setText(_translate("Dialog", "Destination"))
        self.label_phn.setText(_translate("Dialog", "Phone Number"))
        self.label_Boarding_time.setText(_translate("Dialog", "Boarding Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
