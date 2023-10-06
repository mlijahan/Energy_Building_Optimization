
from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 480)
        Dialog.setMinimumSize(QtCore.QSize(1000, 480))
        Dialog.setMaximumSize(QtCore.QSize(1000, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(130, 90, 741, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(280)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 1001, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 28, 131, 24))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(590, 410, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 410, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(304, 24, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(490, 29, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(600, 29, 211, 24))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(850, 25, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(240, 0, 20, 71))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=Dialog)
        self.line_3.setGeometry(QtCore.QRect(460, 0, 16, 71))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 415, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 410, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 410, 111, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def total_u_factor_per_envelope(self):
        self.total_conductive_load = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.envelope_u = float(self.tableWidget.item(row, 5).text())
            self.dt = float(self.tableWidget.item(row, 2).text())
            self.fenestration_u = float(self.tableWidget.item(row, 6).text())
            self.envelpe_load = self.envelope_u * self.dt
            self.fenestration_load = self.fenestration_u * self.dt
            self.total_conductive_load_envelope = self.envelpe_load + self.fenestration_load
            self.total_conductive_load.append(self.total_conductive_load_envelope)
        self.total_conductive_all_envelopes = sum(self.total_conductive_load )
        return np.round(self.total_conductive_all_envelopes,2)

    def miscellaneous_loads(self):
        self.heat_loss = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.heat_loss.append(float(self.tableWidget.item(row, 7).text()))
        self.total_heat_losses = sum(self.heat_loss)
        return np.round(self.total_heat_losses)

    def delete_row_layers(self):
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.tableWidget.removeRow(row)

    def delete_zone_name_from(self):
        self.zone_name_delete = self.lineEdit.clear()
        return self.zone_name_delete

    def delete_total_conductive_load(self):
        self.coductive_load = self.lineEdit_2.clear()
        return self.coductive_load

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Envelopes Properties"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Envelope Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Envelope Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Dt Design Temperatur (k)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Envelope Gross Area (m2)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Total Fenestration Area (m2)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "total Envelope U factor (W/m2K) * A (m2)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "total Fenestration U factor (W/m2K) * A (m2)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Total Heat Loss Coefficient (W/m2K) * A (m2)"))
        self.label.setText(_translate("Dialog", "Zone Name :"))
        self.pushButton.setText(_translate("Dialog", "Clear"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))
        self.pushButton_3.setText(_translate("Dialog", "Add New Envelope"))
        self.label_3.setText(_translate("Dialog", "Select Envelope :"))
        self.pushButton_6.setText(_translate("Dialog", "Add to List"))
        self.label_2.setText(_translate("Dialog", "Total Conductive Load (w) :"))
        self.pushButton_5.setText(_translate("Dialog", "Calculation"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
