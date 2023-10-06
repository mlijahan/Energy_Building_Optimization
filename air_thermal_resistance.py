
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 121, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 154, 135))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 154, 135))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 144, 122))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 98, 69))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 35, 11))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 53, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 26, 8, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 220, 121, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 227, 185))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 227, 185))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 255, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 227, 154))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 133, 77))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 199, 116))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 99, 58, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(25, 20, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(240, 60, 111, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 100, 111, 24))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(241, 140, 111, 24))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 142, 161, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(240, 20, 111, 24))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def air_resistance(self):
        self.temp = self.comboBox_4.currentIndex()
        self.air_thickness = self.comboBox.currentIndex()
        self.emittance = self.comboBox_2.currentIndex()
        self.air_position = self.comboBox_3.currentIndex()
        if self.air_position == 0:
            if self.air_thickness == 0:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.17
                    else:
                        self.thermal_resistance = 0.13
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.28
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.23
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.17
                    else:
                        self.thermal_resistance = 0.13
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.28
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.3
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.3
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.26
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.26
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.18
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.20
            elif self.air_thickness == 1:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.28
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.18
                    else:
                        self.thermal_resistance = 0.13
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.24
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.17
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.19
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.21
            elif self.air_thickness == 2:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.26
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.18
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.20
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.22
            elif self.air_thickness == 3:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.28
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.21
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.23
            else:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.53
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.22
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.24

        elif self.air_position == 1:
            if self.air_thickness == 0:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.13
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.21
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.23
            elif self.air_thickness == 1:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.34
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.27
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.30
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.31
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.20
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.23
            elif self.air_thickness == 2:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.36
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.28
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.21
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.24
            elif self.air_thickness == 3:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.55
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.22
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.31
                    else:
                        self.thermal_resistance = 0.24
            else:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.54
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.20
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.53
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.21
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.24

        if self.air_position == 2:
            if self.air_thickness == 0:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.13
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.31
                    else:
                        self.thermal_resistance = 0.24
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.55
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.26
            elif self.air_thickness == 1:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.65
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.55
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.53
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.21
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.31
                    else:
                        self.thermal_resistance = 0.24
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.65
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.36
                    else:
                        self.thermal_resistance = 0.27
            elif self.air_thickness == 2:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.70
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.32
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.67
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.59
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.23
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.26
            elif self.air_thickness == 3:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.65
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.59
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.29
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.24
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.26
            else:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.38
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.35
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.23
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.54
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.21
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.53
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.32
                    else:
                        self.thermal_resistance = 0.25
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.61
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.35
                    else:
                        self.thermal_resistance = 0.27

        if self.air_position == 3:
            if self.air_thickness == 0:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.54
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.25
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.26
            elif self.air_thickness == 1:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.67
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.73
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.32
                    else:
                        self.thermal_resistance = 0.23
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.67
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.36
                    else:
                        self.thermal_resistance = 0.28
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.77
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.74
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.39
                    else:
                        self.thermal_resistance = 0.29
            elif self.air_thickness == 2:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.89
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.80
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.59
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.90
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.82
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.68
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.31
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.87
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.81
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.24
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.35
                    else:
                        self.thermal_resistance = 0.27
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.82
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.79
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.40
                    else:
                        self.thermal_resistance = 0.30
            elif self.air_thickness == 3:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.85
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.76
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.40
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.83
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.77
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.48
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.67
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.31
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.81
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.76
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.53
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.24
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.36
                    else:
                        self.thermal_resistance = 0.28
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.79
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.76
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.40
                    else:
                        self.thermal_resistance = 0.30
            else:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.865
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.78
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.24
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.68
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.64
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.43
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.87
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.80
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.19
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.75
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.71
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.32
                    else:
                        self.thermal_resistance = 0.23
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.87
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.82
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.24
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.75
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.73
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.39
                    else:
                        self.thermal_resistance = 0.29
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.87
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.83
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.41
                    else:
                        self.thermal_resistance = 0.31

        else:
            if self.air_thickness == 0:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.44
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.41
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.29
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.19
                    else:
                        self.thermal_resistance = 0.14
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.33
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.22
                    else:
                        self.thermal_resistance = 0.16
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.52
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.39
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.27
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.57
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.55
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.47
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.26
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.46
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.26
            elif self.air_thickness == 1:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.37
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.21
                    else:
                        self.thermal_resistance = 0.15
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.62
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.45
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.68
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.42
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.26
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.74
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.70
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.50
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.32
                    else:
                        self.thermal_resistance = 0.23
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.75
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.71
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.51
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.32
                    else:
                        self.thermal_resistance = 0.23
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 0.81
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.78
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.59
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.40
                    else:
                        self.thermal_resistance = 0.30
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.7
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.94
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.17
            elif self.air_thickness == 2:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.7
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.94
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.49
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.25
                    else:
                        self.thermal_resistance = 0.17
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.01
                    elif self.emittance == 1:
                        self.thermal_resistance = 0.99
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.56
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.16
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.04
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.58
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.30
                    else:
                        self.thermal_resistance = 0.20
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.24
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.13
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.69
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.39
                    else:
                        self.thermal_resistance = 0.26
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.29
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.17
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.7
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.39
                    else:
                        self.thermal_resistance = 0.27
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.36
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.27
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.84
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.50
                    else:
                        self.thermal_resistance = 0.35
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.42
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.32
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.86
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.51
                    else:
                        self.thermal_resistance = 0.35
            elif self.air_thickness == 3:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.77
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.44
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.60
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.69
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.44
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.66
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.33
                    else:
                        self.thermal_resistance = 0.21
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.96
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.72
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.92
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.68
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.86
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.43
                    else:
                        self.thermal_resistance = 0.29
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.11
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.82
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.83
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.44
                    else:
                        self.thermal_resistance = 0.29
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.05
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.85
                    elif self.emittance == 2:
                        self.thermal_resistance = 1.06
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.57
                    else:
                        self.thermal_resistance = 0.38
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.28
                    elif self.emittance == 1:
                        self.thermal_resistance = 2.03
                    elif self.emittance == 2:
                        self.thermal_resistance = 1.12
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.59
                    else:
                        self.thermal_resistance = 0.39
            else:
                if self.temp == 0:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.06
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.63
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.63
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.28
                    else:
                        self.thermal_resistance = 0.18
                elif self.temp == 1:
                    if self.emittance == 0:
                        self.thermal_resistance = 1.87
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.57
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.71
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.34
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 2:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.24
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.82
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.75
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.35
                    else:
                        self.thermal_resistance = 0.22
                elif self.temp == 3:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.13
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.84
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.90
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.44
                    else:
                        self.thermal_resistance = 0.29
                elif self.temp == 4:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.43
                    elif self.emittance == 1:
                        self.thermal_resistance = 2.05
                    elif self.emittance == 2:
                        self.thermal_resistance = 0.95
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.46
                    else:
                        self.thermal_resistance = 0.29
                elif self.temp == 5:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.19
                    elif self.emittance == 1:
                        self.thermal_resistance = 1.96
                    elif self.emittance == 2:
                        self.thermal_resistance = 1.1
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.58
                    else:
                        self.thermal_resistance = 0.39
                else:
                    if self.emittance == 0:
                        self.thermal_resistance = 2.57
                    elif self.emittance == 1:
                        self.thermal_resistance = 2.26
                    elif self.emittance == 2:
                        self.thermal_resistance = 1.18
                    elif self.emittance == 3:
                        self.thermal_resistance = 0.61
                    else:
                        self.thermal_resistance = 0.40
        return self.thermal_resistance

    def reset_air_space_temp(self):
        return self.comboBox_4.setCurrentIndex(0)

    def reset_air_apace_thickness(self):
        return self.comboBox.setCurrentIndex(0)

    def reset_effective_emittance(self):
        return self.comboBox_2.setCurrentIndex(0)

    def reset_air_position(self):
        return self.comboBox_3.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Thermal Resistance Plane of Air Space"))
        self.pushButton.setText(_translate("Dialog", "Clear"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))
        self.label.setText(_translate("Dialog", "Air Space Mean Temp(C)/Diff Temp :"))
        self.label_2.setText(_translate("Dialog", "Air Space Thickness (mm) :"))
        self.comboBox.setItemText(0, _translate("Dialog", "13"))
        self.comboBox.setItemText(1, _translate("Dialog", "20"))
        self.comboBox.setItemText(2, _translate("Dialog", "40"))
        self.comboBox.setItemText(3, _translate("Dialog", "90"))
        self.comboBox.setItemText(4, _translate("Dialog", "143"))
        self.label_3.setText(_translate("Dialog", "Effective Emittance :"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "0.03"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "0.05"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "0.2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "0.5"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "0.82"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Horiz/Up"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "45 Slop/Up"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Vertical/Horiz"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "45 Slop/Down"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "Horiz/Down"))
        self.label_4.setText(_translate("Dialog", "Air-Position/Heat-Direction :"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "32.2/5.6"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "10/16.7"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "10/5.6"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "-17.8/11.1"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "-17.8/5.6"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "-45.6/11.1"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "-45.6/5.6"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
