
from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(75, 100, 491, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
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
        self.pushButton_2.setGeometry(QtCore.QRect(230, 422, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 28, 131, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 26, 71, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(470, 27, 81, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(13, 430, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 426, 81, 24))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(346, 10, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 420, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def total_u_factor_per_area(self):
        self.fenestration_area = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.fenestration_area.append(float(self.tableWidget.item(row, 1).text()))
        self.fenestration_u = []
        for row in range(self.ROW):
            self.fenestration_u.append(float(self.tableWidget.item(row, 2).text()))
        self.fenestration_u_area = np.array(self.fenestration_area) * np.array(self.fenestration_u)
        self.total_u = sum(self.fenestration_u_area)
        return np.round(self.total_u,2)

    def delete_row_fenestration(self):
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW+1):
            self.tableWidget.removeRow(row)

    def delete_envelope_name(self):
        self.envelope_name = self.lineEdit.clear()
        return self.envelope_name

    def delete_total_u(self):
        self.total_u = self.lineEdit_2.clear()
        return self.total_u

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Layers of Materials& insulation"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Fenestration Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Net Fenestration Area (m2)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "U (W/m2K) of Fenestration Area"))
        self.label.setText(_translate("Dialog", "Envelope Name :"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Calculation"))
        self.label_3.setText(_translate("Dialog", "Select Fenestration :"))
        self.pushButton_3.setText(_translate("Dialog", "Add New Fenestration"))
        self.pushButton_4.setText(_translate("Dialog", "Add to List"))
        self.label_2.setText(_translate("Dialog", "U- factor of total Area :"))
        self.pushButton_6.setText(_translate("Dialog", "Clear"))

