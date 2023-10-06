
from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 100, 501, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 641, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 28, 85, 24))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 420, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 420, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(225, 27, 111, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 26, 71, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(450, 27, 101, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 430, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 426, 81, 24))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(340, 10, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 420, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def total_r_factor_per_layer(self):
        self.r_factor = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            if self.tableWidget.item(row, 5) != 0:
                self.r_factor.append(float(self.tableWidget.item(row, 5).text()))
            else:
                self.r_factor.append(0)
        self.total_r = sum(self.r_factor)

        self.k_d_factor = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            if self.tableWidget.item(row, 4) != 0:
                self.k_factor = float(self.tableWidget.item(row, 4).text())
                self.thickness = float(self.tableWidget.item(row, 2).text())
                if self.k_factor != 0:
                    self.calculated_d_k = self.thickness / self.k_factor
                    self.k_d_factor.append(self.calculated_d_k)
            else:
                self.k_d_factor.append(0)

        self.total_d_k = sum(self.k_d_factor)
        self.r_totally = self.total_d_k + self.total_r
        return np.round(self.r_totally,2)

    def delete_row_layers(self):
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.tableWidget.removeRow(row)

    def delete_envelope_name(self):
        self.envelope_name = self.lineEdit.clear()
        return self.envelope_name

    def delete_total_r(self):
        self.total_r = self.lineEdit_2.clear()
        return self.total_r

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Layers of Materials& insulation"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Layer Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Layer Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Layer Thickness (mm)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Material Type"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "K (W/mK)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "R (m2K/W)"))
        self.label.setText(_translate("Dialog", "Envelope Name :"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.label_3.setText(_translate("Dialog", "Select the Layer :"))
        self.pushButton_3.setText(_translate("Dialog", "Add New Layer"))
        self.pushButton_4.setText(_translate("Dialog", "Add to List"))
        self.label_2.setText(_translate("Dialog", "Total Thermal Resistance :"))
        self.pushButton_5.setText(_translate("Dialog", "Calculation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
