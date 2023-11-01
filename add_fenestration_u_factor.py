
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 350)
        Dialog.setMinimumSize(QtCore.QSize(680, 350))
        Dialog.setMaximumSize(QtCore.QSize(680, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 10, 297, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 250, 121, 41))
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
        self.pushButton_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 250, 121, 41))
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
        self.pushButton_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 52, 541, 24))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 162, 531, 24))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def u_factor_installation_func(self):
        self.glazing_types = self.comboBox.currentIndex()
        self.installation_type = self.comboBox_2.currentIndex()
        if self.glazing_types == 0:
            if self.installation_type == 0:
                self.ufactor_installation = 7.01
            elif self.installation_type == 1:
                self.ufactor_installation = 6.08
            elif self.installation_type == 2:
                self.ufactor_installation = 5.27
            elif self.installation_type == 3:
                self.ufactor_installation = 5.2
            elif self.installation_type == 4:
                self.ufactor_installation = 4.83
            elif self.installation_type == 5:
                self.ufactor_installation = 6.38
            elif self.installation_type == 6:
                self.ufactor_installation = 6.06
            elif self.installation_type == 7:
                self.ufactor_installation = 5.58
            elif self.installation_type == 8:
                self.ufactor_installation = 5.58
            elif self.installation_type == 9:
                self.ufactor_installation = 5.40
            elif self.installation_type == 10:
                self.ufactor_installation = 14.21
            elif self.installation_type == 11:
                self.ufactor_installation = 11.94
            elif self.installation_type == 12:
                self.ufactor_installation = 6.86
            elif self.installation_type == 13:
                self.ufactor_installation = 6.27
            elif self.installation_type == 14:
                self.ufactor_installation = 6.27
            elif self.installation_type == 15:
                self.ufactor_installation = 6.76
            elif self.installation_type == 16:
                self.ufactor_installation = 6.76
            elif self.installation_type == 17:
                self.ufactor_installation = 10.03
            elif self.installation_type == 18:
                self.ufactor_installation = 9.68
            elif self.installation_type == 19:
                self.ufactor_installation = 9.16
            elif self.installation_type == 20:
                self.ufactor_installation = 8.05
            elif self.installation_type == 21:
                self.ufactor_installation = 7.66
            elif self.installation_type == 22:
                self.ufactor_installation = 7.64
            else:
                self.ufactor_installation = 7.10

        elif self.glazing_types == 1:
            if self.installation_type == 0:
                self.ufactor_installation = 6.23
            elif self.installation_type == 1:
                self.ufactor_installation = 5.35
            elif self.installation_type == 2:
                self.ufactor_installation = 4.59
            elif self.installation_type == 3:
                self.ufactor_installation = 4.52
            elif self.installation_type == 4:
                self.ufactor_installation = 4.18
            elif self.installation_type == 5:
                self.ufactor_installation = 5.55
            elif self.installation_type == 6:
                self.ufactor_installation = 5.23
            elif self.installation_type == 7:
                self.ufactor_installation = 4.77
            elif self.installation_type == 8:
                self.ufactor_installation = 4.77
            elif self.installation_type == 9:
                self.ufactor_installation = 4.61
            elif self.installation_type == 10:
                self.ufactor_installation = 12.70
            elif self.installation_type == 11:
                self.ufactor_installation = 10.42
            elif self.installation_type == 12:
                self.ufactor_installation = 6.03
            elif self.installation_type == 13:
                self.ufactor_installation = 5.44
            elif self.installation_type == 14:
                self.ufactor_installation = 5.44
            elif self.installation_type == 15:
                self.ufactor_installation = 5.85
            elif self.installation_type == 16:
                self.ufactor_installation = 5.85
            elif self.installation_type == 17:
                self.ufactor_installation = 9.09
            elif self.installation_type == 18:
                self.ufactor_installation = 8.74
            elif self.installation_type == 19:
                self.ufactor_installation = 8.23
            elif self.installation_type == 20:
                self.ufactor_installation = 7.45
            elif self.installation_type == 21:
                self.ufactor_installation = 6.83
            elif self.installation_type == 22:
                self.ufactor_installation = 6.8
            else:
                self.ufactor_installation = 6.27

        elif self.glazing_types == 2:
            if self.installation_type == 0:
                self.ufactor_installation = 6.62
            elif self.installation_type == 1:
                self.ufactor_installation = 5.72
            elif self.installation_type == 2:
                self.ufactor_installation = 4.93
            elif self.installation_type == 3:
                self.ufactor_installation = 4.86
            elif self.installation_type == 4:
                self.ufactor_installation = 4.51
            elif self.installation_type == 5:
                self.ufactor_installation = 5.96
            elif self.installation_type == 6:
                self.ufactor_installation = 5.64
            elif self.installation_type == 7:
                self.ufactor_installation = 5.18
            elif self.installation_type == 8:
                self.ufactor_installation = 5.18
            elif self.installation_type == 9:
                self.ufactor_installation = 5.01
            elif self.installation_type == 10:
                self.ufactor_installation = 13.45
            elif self.installation_type == 11:
                self.ufactor_installation =11.48
            elif self.installation_type == 12:
                self.ufactor_installation = 6.44
            elif self.installation_type == 13:
                self.ufactor_installation = 5.86
            elif self.installation_type == 14:
                self.ufactor_installation = 5.86
            elif self.installation_type == 15:
                self.ufactor_installation = 6.30
            elif self.installation_type == 16:
                self.ufactor_installation = 6.30
            elif self.installation_type == 17:
                self.ufactor_installation = 9.56
            elif self.installation_type == 18:
                self.ufactor_installation = 9.21
            elif self.installation_type == 19:
                self.ufactor_installation = 8.7
            elif self.installation_type == 20:
                self.ufactor_installation = 7.89
            elif self.installation_type == 21:
                self.ufactor_installation = 7.24
            elif self.installation_type == 22:
                self.ufactor_installation = 7.22
            else:
                self.ufactor_installation = 6.68

        elif self.glazing_types == 3:
            if self.installation_type == 0:
                self.ufactor_installation = 4.62
            elif self.installation_type == 1:
                self.ufactor_installation = 3.61
            elif self.installation_type == 2:
                self.ufactor_installation = 3.24
            elif self.installation_type == 3:
                self.ufactor_installation = 3.14
            elif self.installation_type == 4:
                self.ufactor_installation = 2.84
            elif self.installation_type == 5:
                self.ufactor_installation = 3.88
            elif self.installation_type == 6:
                self.ufactor_installation = 3.52
            elif self.installation_type == 7:
                self.ufactor_installation = 3.18
            elif self.installation_type == 8:
                self.ufactor_installation = 3.16
            elif self.installation_type == 9:
                self.ufactor_installation = 3.04
            elif self.installation_type == 10:
                self.ufactor_installation = 9.78
            elif self.installation_type == 11:
                self.ufactor_installation = 7.5
            elif self.installation_type == 12:
                self.ufactor_installation = 4.38
            elif self.installation_type == 13:
                self.ufactor_installation = 3.79
            elif self.installation_type == 14:
                self.ufactor_installation = 3.56
            elif self.installation_type == 15:
                self.ufactor_installation = 3.29
            elif self.installation_type == 16:
                self.ufactor_installation = 3.75
            elif self.installation_type == 17:
                self.ufactor_installation = 6.26
            elif self.installation_type == 18:
                self.ufactor_installation = 5.46
            elif self.installation_type == 19:
                self.ufactor_installation = 5.21
            elif self.installation_type == 20:
                self.ufactor_installation = 4.79
            elif self.installation_type == 21:
                self.ufactor_installation = 4.54
            elif self.installation_type == 22:
                self.ufactor_installation = 4.71
            else:
                self.ufactor_installation = 3.75

        elif self.glazing_types == 4:
            if self.installation_type == 0:
                self.ufactor_installation = 4.3
            elif self.installation_type == 1:
                self.ufactor_installation = 3.31
            elif self.installation_type == 2:
                self.ufactor_installation = 2.96
            elif self.installation_type == 3:
                self.ufactor_installation = 2.86
            elif self.installation_type == 4:
                self.ufactor_installation = 2.58
            elif self.installation_type == 5:
                self.ufactor_installation = 3.54
            elif self.installation_type == 6:
                self.ufactor_installation = 3.18
            elif self.installation_type == 7:
                self.ufactor_installation = 2.85
            elif self.installation_type == 8:
                self.ufactor_installation = 2.83
            elif self.installation_type == 9:
                self.ufactor_installation = 2.72
            elif self.installation_type == 10:
                self.ufactor_installation = 9.19
            elif self.installation_type == 11:
                self.ufactor_installation = 6.92
            elif self.installation_type == 12:
                self.ufactor_installation = 4.03
            elif self.installation_type == 13:
                self.ufactor_installation = 3.45
            elif self.installation_type == 14:
                self.ufactor_installation = 3.22
            elif self.installation_type == 15:
                self.ufactor_installation = 3.24
            elif self.installation_type == 16:
                self.ufactor_installation = 3.71
            elif self.installation_type == 17:
                self.ufactor_installation = 6.17
            elif self.installation_type == 18:
                self.ufactor_installation = 5.41
            elif self.installation_type == 19:
                self.ufactor_installation = 5.16
            elif self.installation_type == 20:
                self.ufactor_installation = 4.74
            elif self.installation_type == 21:
                self.ufactor_installation =4.49
            elif self.installation_type == 22:
                self.ufactor_installation = 4.68
            else:
                self.ufactor_installation = 3.70

        elif self.glazing_types == 5:
            if self.installation_type == 0:
                self.ufactor_installation = 4.43
            elif self.installation_type == 1:
                self.ufactor_installation = 3.44
            elif self.installation_type == 2:
                self.ufactor_installation = 3.08
            elif self.installation_type == 3:
                self.ufactor_installation = 2.98
            elif self.installation_type == 4:
                self.ufactor_installation = 2.69
            elif self.installation_type == 5:
                self.ufactor_installation = 3.68
            elif self.installation_type == 6:
                self.ufactor_installation = 3.33
            elif self.installation_type == 7:
                self.ufactor_installation = 3
            elif self.installation_type == 8:
                self.ufactor_installation = 2.98
            elif self.installation_type == 9:
                self.ufactor_installation = 2.86
            elif self.installation_type == 10:
                self.ufactor_installation = 9.44
            elif self.installation_type == 11:
                self.ufactor_installation = 7.17
            elif self.installation_type == 12:
                self.ufactor_installation = 4.18
            elif self.installation_type == 13:
                self.ufactor_installation = 3.6
            elif self.installation_type == 14:
                self.ufactor_installation = 3.37
            elif self.installation_type == 15:
                self.ufactor_installation = 3.01
            elif self.installation_type == 16:
                self.ufactor_installation = 3.56
            elif self.installation_type == 17:
                self.ufactor_installation = 5.96
            elif self.installation_type == 18:
                self.ufactor_installation = 5.19
            elif self.installation_type == 19:
                self.ufactor_installation = 4.94
            elif self.installation_type == 20:
                self.ufactor_installation = 4.54
            elif self.installation_type == 21:
                self.ufactor_installation = 4.3
            elif self.installation_type == 22:
                self.ufactor_installation = 4.52
            else:
                self.ufactor_installation = 3.51

        elif self.glazing_types == 6:
            if self.installation_type == 0:
                self.ufactor_installation = 4.16
            elif self.installation_type == 1:
                self.ufactor_installation = 3.18
            elif self.installation_type == 2:
                self.ufactor_installation = 2.84
            elif self.installation_type == 3:
                self.ufactor_installation = 2.74
            elif self.installation_type == 4:
                self.ufactor_installation = 2.46
            elif self.installation_type == 5:
                self.ufactor_installation = 3.39
            elif self.installation_type == 6:
                self.ufactor_installation = 3.04
            elif self.installation_type == 7:
                self.ufactor_installation = 2.71
            elif self.installation_type == 8:
                self.ufactor_installation = 2.69
            elif self.installation_type == 9:
                self.ufactor_installation = 2.58
            elif self.installation_type == 10:
                self.ufactor_installation = 8.94
            elif self.installation_type == 11:
                self.ufactor_installation = 6.67
            elif self.installation_type == 12:
                self.ufactor_installation = 3.89
            elif self.installation_type == 13:
                self.ufactor_installation = 3.30
            elif self.installation_type == 14:
                self.ufactor_installation = 3.07
            elif self.installation_type == 15:
                self.ufactor_installation = 3.01
            elif self.installation_type == 16:
                self.ufactor_installation = 3.56
            elif self.installation_type == 17:
                self.ufactor_installation = 5.96
            elif self.installation_type == 18:
                self.ufactor_installation = 5.19
            elif self.installation_type == 19:
                self.ufactor_installation = 4.94
            elif self.installation_type == 20:
                self.ufactor_installation = 4.54
            elif self.installation_type == 21:
                self.ufactor_installation = 4.3
            elif self.installation_type == 22:
                self.ufactor_installation = 4.52
            else:
                self.ufactor_installation = 3.51

        elif self.glazing_types == 7:
            if self.installation_type == 0:
                self.ufactor_installation = 4.48
            elif self.installation_type == 1:
                self.ufactor_installation = 3.48
            elif self.installation_type == 2:
                self.ufactor_installation = 3.12
            elif self.installation_type == 3:
                self.ufactor_installation = 3.02
            elif self.installation_type == 4:
                self.ufactor_installation = 2.73
            elif self.installation_type == 5:
                self.ufactor_installation = 3.73
            elif self.installation_type == 6:
                self.ufactor_installation = 3.38
            elif self.installation_type == 7:
                self.ufactor_installation = 3.04
            elif self.installation_type == 8:
                self.ufactor_installation = 3.02
            elif self.installation_type == 9:
                self.ufactor_installation = 2.9
            elif self.installation_type == 10:
                self.ufactor_installation = 9.53
            elif self.installation_type == 11:
                self.ufactor_installation = 7.52
            elif self.installation_type == 12:
                self.ufactor_installation = 4.23
            elif self.installation_type == 13:
                self.ufactor_installation = 3.65
            elif self.installation_type == 14:
                self.ufactor_installation =3.41
            elif self.installation_type == 15:
                self.ufactor_installation = 3.07
            elif self.installation_type == 16:
                self.ufactor_installation = 3.6
            elif self.installation_type == 17:
                self.ufactor_installation =6.01
            elif self.installation_type == 18:
                self.ufactor_installation = 5.24
            elif self.installation_type == 19:
                self.ufactor_installation = 4.99
            elif self.installation_type == 20:
                self.ufactor_installation = 4.59
            elif self.installation_type == 21:
                self.ufactor_installation = 4.35
            elif self.installation_type == 22:
                self.ufactor_installation = 4.56
            else:
                self.ufactor_installation = 3.55

        elif self.glazing_types == 8:
            if self.installation_type == 0:
                self.ufactor_installation = 4.11
            elif self.installation_type == 1:
                self.ufactor_installation = 3.14
            elif self.installation_type == 2:
                self.ufactor_installation = 2.8
            elif self.installation_type == 3:
                self.ufactor_installation = 2.7
            elif self.installation_type == 4:
                self.ufactor_installation = 2.42
            elif self.installation_type == 5:
                self.ufactor_installation = 3.34
            elif self.installation_type == 6:
                self.ufactor_installation = 2.99
            elif self.installation_type == 7:
                self.ufactor_installation = 2.67
            elif self.installation_type == 8:
                self.ufactor_installation = 2.65
            elif self.installation_type == 9:
                self.ufactor_installation = 2.53
            elif self.installation_type == 10:
                self.ufactor_installation = 8.86
            elif self.installation_type == 11:
                self.ufactor_installation = 6.58
            elif self.installation_type == 12:
                self.ufactor_installation = 3.84
            elif self.installation_type == 13:
                self.ufactor_installation = 3.25
            elif self.installation_type == 14:
                self.ufactor_installation = 3.02
            elif self.installation_type == 15:
                self.ufactor_installation = 3.01
            elif self.installation_type == 16:
                self.ufactor_installation = 3.56
            elif self.installation_type == 17:
                self.ufactor_installation = 5.96
            elif self.installation_type == 18:
                self.ufactor_installation = 5.19
            elif self.installation_type == 19:
                self.ufactor_installation = 4.94
            elif self.installation_type == 20:
                self.ufactor_installation = 4.54
            elif self.installation_type == 21:
                self.ufactor_installation = 4.30
            elif self.installation_type == 22:
                self.ufactor_installation = 4.52
            else:
                self.ufactor_installation = 3.51

        elif self.glazing_types == 9:
            if self.installation_type == 0:
                self.ufactor_installation = 4.25
            elif self.installation_type == 1:
                self.ufactor_installation = 3.27
            elif self.installation_type == 2:
                self.ufactor_installation =2.92
            elif self.installation_type == 3:
                self.ufactor_installation = 2.82
            elif self.installation_type == 4:
                self.ufactor_installation = 2.54
            elif self.installation_type == 5:
                self.ufactor_installation = 3.49
            elif self.installation_type == 6:
                self.ufactor_installation = 3.13
            elif self.installation_type == 7:
                self.ufactor_installation = 2.81
            elif self.installation_type == 8:
                self.ufactor_installation = 2.79
            elif self.installation_type == 9:
                self.ufactor_installation = 2.67
            elif self.installation_type == 10:
                self.ufactor_installation = 9.11
            elif self.installation_type == 11:
                self.ufactor_installation = 6.84
            elif self.installation_type == 12:
                self.ufactor_installation = 3.99
            elif self.installation_type == 13:
                self.ufactor_installation = 3.40
            elif self.installation_type == 14:
                self.ufactor_installation = 3.17
            elif self.installation_type == 15:
                self.ufactor_installation = 2.78
            elif self.installation_type == 16:
                self.ufactor_installation = 3.40
            elif self.installation_type == 17:
                self.ufactor_installation = 5.74
            elif self.installation_type == 18:
                self.ufactor_installation = 4.97
            elif self.installation_type == 19:
                self.ufactor_installation = 4.72
            elif self.installation_type == 20:
                self.ufactor_installation = 4.34
            elif self.installation_type == 21:
                self.ufactor_installation = 4.10
            elif self.installation_type == 22:
                self.ufactor_installation = 4.37
            else:
                self.ufactor_installation = 3.31

        elif self.glazing_types == 10:
            if self.installation_type == 0:
                self.ufactor_installation = 3.98
            elif self.installation_type == 1:
                self.ufactor_installation = 3.01
            elif self.installation_type == 2:
                self.ufactor_installation = 2.68
            elif self.installation_type == 3:
                self.ufactor_installation = 2.58
            elif self.installation_type == 4:
                self.ufactor_installation = 2.31
            elif self.installation_type == 5:
                self.ufactor_installation =3.20
            elif self.installation_type == 6:
                self.ufactor_installation = 2.84
            elif self.installation_type == 7:
                self.ufactor_installation = 2.52
            elif self.installation_type == 8:
                self.ufactor_installation = 2.5
            elif self.installation_type == 9:
                self.ufactor_installation = 2.39
            elif self.installation_type == 10:
                self.ufactor_installation = 8.61
            elif self.installation_type == 11:
                self.ufactor_installation = 6.33
            elif self.installation_type == 12:
                self.ufactor_installation = 3.69
            elif self.installation_type == 13:
                self.ufactor_installation = 3.11
            elif self.installation_type == 14:
                self.ufactor_installation = 2.88
            elif self.installation_type == 15:
                self.ufactor_installation = 2.78
            elif self.installation_type == 16:
                self.ufactor_installation = 3.4
            elif self.installation_type == 17:
                self.ufactor_installation = 5.74
            elif self.installation_type == 18:
                self.ufactor_installation = 4.97
            elif self.installation_type == 19:
                self.ufactor_installation = 4.72
            elif self.installation_type == 20:
                self.ufactor_installation = 4.34
            elif self.installation_type == 21:
                self.ufactor_installation = 4.10
            elif self.installation_type == 22:
                self.ufactor_installation = 4.37
            else:
                self.ufactor_installation = 3.31

        elif self.glazing_types == 11:
            if self.installation_type == 0:
                self.ufactor_installation = 4.34
            elif self.installation_type == 1:
                self.ufactor_installation = 3.35
            elif self.installation_type == 2:
                self.ufactor_installation = 3
            elif self.installation_type == 3:
                self.ufactor_installation = 2.9
            elif self.installation_type == 4:
                self.ufactor_installation = 2.61
            elif self.installation_type == 5:
                self.ufactor_installation = 3.59
            elif self.installation_type == 6:
                self.ufactor_installation = 3.23
            elif self.installation_type == 7:
                self.ufactor_installation = 2.9
            elif self.installation_type == 8:
                self.ufactor_installation = 2.88
            elif self.installation_type == 9:
                self.ufactor_installation = 2.77
            elif self.installation_type == 10:
                self.ufactor_installation = 9.28
            elif self.installation_type == 11:
                self.ufactor_installation = 7
            elif self.installation_type == 12:
                self.ufactor_installation = 4.08
            elif self.installation_type == 13:
                self.ufactor_installation = 3.5
            elif self.installation_type == 14:
                self.ufactor_installation = 3.27
            elif self.installation_type == 15:
                self.ufactor_installation = 2.9
            elif self.installation_type == 16:
                self.ufactor_installation = 3.48
            elif self.installation_type == 17:
                self.ufactor_installation = 5.85
            elif self.installation_type == 18:
                self.ufactor_installation = 5.08
            elif self.installation_type == 19:
                self.ufactor_installation = 4.83
            elif self.installation_type == 20:
                self.ufactor_installation = 4.44
            elif self.installation_type == 21:
                self.ufactor_installation = 4.20
            elif self.installation_type == 22:
                self.ufactor_installation = 4.45
            else:
                self.ufactor_installation = 3.41

        elif self.glazing_types == 12:
            if self.installation_type == 0:
                self.ufactor_installation = 3.93
            elif self.installation_type == 1:
                self.ufactor_installation = 2.96
            elif self.installation_type == 2:
                self.ufactor_installation = 2.64
            elif self.installation_type == 3:
                self.ufactor_installation = 2.54
            elif self.installation_type == 4:
                self.ufactor_installation = 2.27
            elif self.installation_type == 5:
                self.ufactor_installation = 3.15
            elif self.installation_type == 6:
                self.ufactor_installation = 2.79
            elif self.installation_type == 7:
                self.ufactor_installation = 2.48
            elif self.installation_type == 8:
                self.ufactor_installation = 2.46
            elif self.installation_type == 9:
                self.ufactor_installation = 2.35
            elif self.installation_type == 10:
                self.ufactor_installation = 8.52
            elif self.installation_type == 11:
                self.ufactor_installation = 6.25
            elif self.installation_type == 12:
                self.ufactor_installation = 3.64
            elif self.installation_type == 13:
                self.ufactor_installation = 3.06
            elif self.installation_type == 14:
                self.ufactor_installation = 2.83
            elif self.installation_type == 15:
                self.ufactor_installation = 2.84
            elif self.installation_type == 16:
                self.ufactor_installation = 3.44
            elif self.installation_type == 17:
                self.ufactor_installation = 5.79
            elif self.installation_type == 18:
                self.ufactor_installation = 5.02
            elif self.installation_type == 19:
                self.ufactor_installation = 4.78
            elif self.installation_type == 20:
                self.ufactor_installation = 4.39
            elif self.installation_type == 21:
                self.ufactor_installation = 4.15
            elif self.installation_type == 22:
                self.ufactor_installation = 4.41
            else:
                self.ufactor_installation = 3.36

        elif self.glazing_types == 13:
            if self.installation_type == 0:
                self.ufactor_installation = 4.07
            elif self.installation_type == 1:
                self.ufactor_installation = 3.09
            elif self.installation_type == 2:
                self.ufactor_installation = 2.76
            elif self.installation_type == 3:
                self.ufactor_installation = 2.66
            elif self.installation_type == 4:
                self.ufactor_installation = 2.38
            elif self.installation_type == 5:
                self.ufactor_installation = 3.3
            elif self.installation_type == 6:
                self.ufactor_installation = 2.94
            elif self.installation_type == 7:
                self.ufactor_installation = 2.62
            elif self.installation_type == 8:
                self.ufactor_installation = 2.60
            elif self.installation_type == 9:
                self.ufactor_installation = 2.49
            elif self.installation_type == 10:
                self.ufactor_installation = 8.77
            elif self.installation_type == 11:
                self.ufactor_installation = 6.50
            elif self.installation_type == 12:
                self.ufactor_installation = 3.79
            elif self.installation_type == 13:
                self.ufactor_installation = 3.21
            elif self.installation_type == 14:
                self.ufactor_installation = 2.97
            elif self.installation_type == 15:
                self.ufactor_installation = 2.50
            elif self.installation_type == 16:
                self.ufactor_installation = 3.20
            elif self.installation_type == 17:
                self.ufactor_installation = 5.46
            elif self.installation_type == 18:
                self.ufactor_installation = 4.69
            elif self.installation_type == 19:
                self.ufactor_installation = 4.45
            elif self.installation_type == 20:
                self.ufactor_installation = 4.09
            elif self.installation_type == 21:
                self.ufactor_installation = 3.86
            elif self.installation_type == 22:
                self.ufactor_installation = 4.17
            else:
                self.ufactor_installation = 3.07

        elif self.glazing_types == 14:
            if self.installation_type == 0:
                self.ufactor_installation = 3.75
            elif self.installation_type == 1:
                self.ufactor_installation = 2.79
            elif self.installation_type == 2:
                self.ufactor_installation = 2.48
            elif self.installation_type == 3:
                self.ufactor_installation = 2.38
            elif self.installation_type == 4:
                self.ufactor_installation = 2.11
            elif self.installation_type == 5:
                self.ufactor_installation = 2.95
            elif self.installation_type == 6:
                self.ufactor_installation = 2.60
            elif self.installation_type == 7:
                self.ufactor_installation = 2.29
            elif self.installation_type == 8:
                self.ufactor_installation = 2.27
            elif self.installation_type == 9:
                self.ufactor_installation = 2.16
            elif self.installation_type == 10:
                self.ufactor_installation = 8.18
            elif self.installation_type == 11:
                self.ufactor_installation = 5.91
            elif self.installation_type == 12:
                self.ufactor_installation = 3.45
            elif self.installation_type == 13:
                self.ufactor_installation = 2.86
            elif self.installation_type == 14:
                self.ufactor_installation = 2.63
            elif self.installation_type == 15:
                self.ufactor_installation = 2.61
            elif self.installation_type == 16:
                self.ufactor_installation = 3.28
            elif self.installation_type == 17:
                self.ufactor_installation = 5.57
            elif self.installation_type == 18:
                self.ufactor_installation = 4.8
            elif self.installation_type == 19:
                self.ufactor_installation = 4.56
            elif self.installation_type == 20:
                self.ufactor_installation = 4.19
            elif self.installation_type == 21:
                self.ufactor_installation = 3.96
            elif self.installation_type == 22:
                self.ufactor_installation = 4.25
            else:
                self.ufactor_installation = 3.17

        elif self.glazing_types == 15:
            if self.installation_type == 0:
                self.ufactor_installation = 4.16
            elif self.installation_type == 1:
                self.ufactor_installation = 3.18
            elif self.installation_type == 2:
                self.ufactor_installation = 2.84
            elif self.installation_type == 3:
                self.ufactor_installation = 2.74
            elif self.installation_type == 4:
                self.ufactor_installation = 2.46
            elif self.installation_type == 5:
                self.ufactor_installation = 3.39
            elif self.installation_type == 6:
                self.ufactor_installation = 3.04
            elif self.installation_type == 7:
                self.ufactor_installation = 2.71
            elif self.installation_type == 8:
                self.ufactor_installation = 2.69
            elif self.installation_type == 9:
                self.ufactor_installation = 2.58
            elif self.installation_type == 10:
                self.ufactor_installation = 8.94
            elif self.installation_type == 11:
                self.ufactor_installation = 6.67
            elif self.installation_type == 12:
                self.ufactor_installation = 3.89
            elif self.installation_type == 13:
                self.ufactor_installation = 3.30
            elif self.installation_type == 14:
                self.ufactor_installation = 3.07
            elif self.installation_type == 15:
                self.ufactor_installation = 2.61
            elif self.installation_type == 16:
                self.ufactor_installation = 3.28
            elif self.installation_type == 17:
                self.ufactor_installation = 5.57
            elif self.installation_type == 18:
                self.ufactor_installation = 4.8
            elif self.installation_type == 19:
                self.ufactor_installation = 4.56
            elif self.installation_type == 20:
                self.ufactor_installation = 4.19
            elif self.installation_type == 21:
                self.ufactor_installation = 3.96
            elif self.installation_type == 22:
                self.ufactor_installation = 4.25
            else:
                self.ufactor_installation = 3.17

        elif self.glazing_types == 16:
            if self.installation_type == 0:
                self.ufactor_installation = 3.7
            elif self.installation_type == 1:
                self.ufactor_installation = 2.75
            elif self.installation_type == 2:
                self.ufactor_installation = 2.44
            elif self.installation_type == 3:
                self.ufactor_installation = 2.34
            elif self.installation_type == 4:
                self.ufactor_installation = 2.07
            elif self.installation_type == 5:
                self.ufactor_installation = 2.91
            elif self.installation_type == 6:
                self.ufactor_installation = 2.55
            elif self.installation_type == 7:
                self.ufactor_installation = 2.24
            elif self.installation_type == 8:
                self.ufactor_installation = 2.22
            elif self.installation_type == 9:
                self.ufactor_installation = 2.12
            elif self.installation_type == 10:
                self.ufactor_installation = 8.10
            elif self.installation_type == 11:
                self.ufactor_installation = 5.82
            elif self.installation_type == 12:
                self.ufactor_installation = 3.4
            elif self.installation_type == 13:
                self.ufactor_installation = 2.81
            elif self.installation_type == 14:
                self.ufactor_installation = 2.58
            elif self.installation_type == 15:
                self.ufactor_installation = 2.61
            elif self.installation_type == 16:
                self.ufactor_installation = 3.28
            elif self.installation_type == 17:
                self.ufactor_installation = 5.57
            elif self.installation_type == 18:
                self.ufactor_installation = 4.80
            elif self.installation_type == 19:
                self.ufactor_installation = 4.56
            elif self.installation_type == 20:
                self.ufactor_installation = 4.19
            elif self.installation_type == 21:
                self.ufactor_installation = 3.96
            elif self.installation_type == 22:
                self.ufactor_installation = 4.25
            else:
                self.ufactor_installation = 3.17

        elif self.glazing_types == 17:
            if self.installation_type == 0:
                self.ufactor_installation = 3.84
            elif self.installation_type == 1:
                self.ufactor_installation = 2.88
            elif self.installation_type == 2:
                self.ufactor_installation = 2.56
            elif self.installation_type == 3:
                self.ufactor_installation = 2.46
            elif self.installation_type == 4:
                self.ufactor_installation = 2.19
            elif self.installation_type == 5:
                self.ufactor_installation = 3.05
            elif self.installation_type == 6:
                self.ufactor_installation = 2.70
            elif self.installation_type == 7:
                self.ufactor_installation = 2.38
            elif self.installation_type == 8:
                self.ufactor_installation = 2.36
            elif self.installation_type == 9:
                self.ufactor_installation = 2.26
            elif self.installation_type == 10:
                self.ufactor_installation = 8.35
            elif self.installation_type == 11:
                self.ufactor_installation = 6.08
            elif self.installation_type == 12:
                self.ufactor_installation = 3.54
            elif self.installation_type == 13:
                self.ufactor_installation = 2.96
            elif self.installation_type == 14:
                self.ufactor_installation = 2.73
            elif self.installation_type == 15:
                self.ufactor_installation = 2.22
            elif self.installation_type == 16:
                self.ufactor_installation = 3
            elif self.installation_type == 17:
                self.ufactor_installation = 5.19
            elif self.installation_type == 18:
                self.ufactor_installation = 4.42
            elif self.installation_type == 19:
                self.ufactor_installation = 4.18
            elif self.installation_type == 20:
                self.ufactor_installation = 3.84
            elif self.installation_type == 21:
                self.ufactor_installation = 3.61
            elif self.installation_type == 22:
                self.ufactor_installation = 3.98
            else:
                self.ufactor_installation = 2.83

        elif self.glazing_types == 18:
            if self.installation_type == 0:
                self.ufactor_installation = 3.47
            elif self.installation_type == 1:
                self.ufactor_installation = 2.53
            elif self.installation_type == 2:
                self.ufactor_installation = 2.24
            elif self.installation_type == 3:
                self.ufactor_installation = 2.14
            elif self.installation_type == 4:
                self.ufactor_installation = 2.18
            elif self.installation_type == 5:
                self.ufactor_installation = 2.66
            elif self.installation_type == 6:
                self.ufactor_installation = 2.30
            elif self.installation_type == 7:
                self.ufactor_installation = 2
            elif self.installation_type == 8:
                self.ufactor_installation = 1.98
            elif self.installation_type == 9:
                self.ufactor_installation = 1.88
            elif self.installation_type == 10:
                self.ufactor_installation = 7.67
            elif self.installation_type == 11:
                self.ufactor_installation = 5.39
            elif self.installation_type == 12:
                self.ufactor_installation = 3.15
            elif self.installation_type == 13:
                self.ufactor_installation = 2.56
            elif self.installation_type == 14:
                self.ufactor_installation = 2.33
            elif self.installation_type == 15:
                self.ufactor_installation = 2.27
            elif self.installation_type == 16:
                self.ufactor_installation = 3.04
            elif self.installation_type == 17:
                self.ufactor_installation = 5.24
            elif self.installation_type == 18:
                self.ufactor_installation = 4.47
            elif self.installation_type == 19:
                self.ufactor_installation = 4.24
            elif self.installation_type == 20:
                self.ufactor_installation = 3.89
            elif self.installation_type == 21:
                self.ufactor_installation = 3.66
            elif self.installation_type == 22:
                self.ufactor_installation = 4.02
            else:
                self.ufactor_installation = 2.88

        elif self.glazing_types == 19:
            if self.installation_type == 0:
                self.ufactor_installation = 4.02
            elif self.installation_type == 1:
                self.ufactor_installation = 3.05
            elif self.installation_type == 2:
                self.ufactor_installation = 2.72
            elif self.installation_type == 3:
                self.ufactor_installation = 2.62
            elif self.installation_type == 4:
                self.ufactor_installation = 2.34
            elif self.installation_type == 5:
                self.ufactor_installation = 3.25
            elif self.installation_type == 6:
                self.ufactor_installation = 2.89
            elif self.installation_type == 7:
                self.ufactor_installation = 2.57
            elif self.installation_type == 8:
                self.ufactor_installation = 2.55
            elif self.installation_type == 9:
                self.ufactor_installation = 2.44
            elif self.installation_type == 10:
                self.ufactor_installation = 8.69
            elif self.installation_type == 11:
                self.ufactor_installation = 6.42
            elif self.installation_type == 12:
                self.ufactor_installation = 3.74
            elif self.installation_type == 13:
                self.ufactor_installation = 3.16
            elif self.installation_type == 14:
                self.ufactor_installation = 2.92
            elif self.installation_type == 15:
                self.ufactor_installation = 2.50
            elif self.installation_type == 16:
                self.ufactor_installation = 3.20
            elif self.installation_type == 17:
                self.ufactor_installation = 5.46
            elif self.installation_type == 18:
                self.ufactor_installation = 4.69
            elif self.installation_type == 19:
                self.ufactor_installation = 4.45
            elif self.installation_type == 20:
                self.ufactor_installation = 4.09
            elif self.installation_type == 21:
                self.ufactor_installation = 3.86
            elif self.installation_type == 22:
                self.ufactor_installation = 4.18
            else:
                self.ufactor_installation = 3.07

        elif self.glazing_types == 20:
            if self.installation_type == 0:
                self.ufactor_installation = 3.56
            elif self.installation_type == 1:
                self.ufactor_installation = 2.62
            elif self.installation_type == 2:
                self.ufactor_installation = 2.32
            elif self.installation_type == 3:
                self.ufactor_installation = 2.22
            elif self.installation_type == 4:
                self.ufactor_installation = 1.96
            elif self.installation_type == 5:
                self.ufactor_installation = 2.76
            elif self.installation_type == 6:
                self.ufactor_installation = 2.40
            elif self.installation_type == 7:
                self.ufactor_installation = 2.10
            elif self.installation_type == 8:
                self.ufactor_installation = 2.08
            elif self.installation_type == 9:
                self.ufactor_installation = 1.98
            elif self.installation_type == 10:
                self.ufactor_installation = 7.84
            elif self.installation_type == 11:
                self.ufactor_installation = 5.57
            elif self.installation_type == 12:
                self.ufactor_installation = 3.25
            elif self.installation_type == 13:
                self.ufactor_installation = 2.66
            elif self.installation_type == 14:
                self.ufactor_installation = 2.43
            elif self.installation_type == 15:
                self.ufactor_installation = 2.5
            elif self.installation_type == 16:
                self.ufactor_installation = 3.20
            elif self.installation_type == 17:
                self.ufactor_installation = 5.46
            elif self.installation_type == 18:
                self.ufactor_installation = 4.69
            elif self.installation_type == 19:
                self.ufactor_installation = 4.45
            elif self.installation_type == 20:
                self.ufactor_installation = 4.09
            elif self.installation_type == 21:
                self.ufactor_installation = 3.86
            elif self.installation_type == 22:
                self.ufactor_installation = 4.18
            else:
                self.ufactor_installation = 3.07

        elif self.glazing_types == 21:
            if self.installation_type == 0:
                self.ufactor_installation = 3.7
            elif self.installation_type == 1:
                self.ufactor_installation = 2.75
            elif self.installation_type == 2:
                self.ufactor_installation = 2.44
            elif self.installation_type == 3:
                self.ufactor_installation = 2.34
            elif self.installation_type == 4:
                self.ufactor_installation = 2.07
            elif self.installation_type == 5:
                self.ufactor_installation = 2.91
            elif self.installation_type == 6:
                self.ufactor_installation = 2.55
            elif self.installation_type == 7:
                self.ufactor_installation = 2.24
            elif self.installation_type == 8:
                self.ufactor_installation = 2.22
            elif self.installation_type == 9:
                self.ufactor_installation = 2.12
            elif self.installation_type == 10:
                self.ufactor_installation = 8.10
            elif self.installation_type == 11:
                self.ufactor_installation = 5.82
            elif self.installation_type == 12:
                self.ufactor_installation = 3.40
            elif self.installation_type == 13:
                self.ufactor_installation = 2.81
            elif self.installation_type == 14:
                self.ufactor_installation = 2.58
            elif self.installation_type == 15:
                self.ufactor_installation = 2.04
            elif self.installation_type == 16:
                self.ufactor_installation = 2.88
            elif self.installation_type == 17:
                self.ufactor_installation = 5.02
            elif self.installation_type == 18:
                self.ufactor_installation = 4.25
            elif self.installation_type == 19:
                self.ufactor_installation = 4.02
            elif self.installation_type == 20:
                self.ufactor_installation = 3.69
            elif self.installation_type == 21:
                self.ufactor_installation = 3.46
            elif self.installation_type == 22:
                self.ufactor_installation = 3.86
            else:
                self.ufactor_installation = 2.68

        elif self.glazing_types == 22:
            if self.installation_type == 0:
                self.ufactor_installation = 3.33
            elif self.installation_type == 1:
                self.ufactor_installation = 2.40
            elif self.installation_type == 2:
                self.ufactor_installation = 2.12
            elif self.installation_type == 3:
                self.ufactor_installation = 2.02
            elif self.installation_type == 4:
                self.ufactor_installation = 1.76
            elif self.installation_type == 5:
                self.ufactor_installation = 2.51
            elif self.installation_type == 6:
                self.ufactor_installation = 2.16
            elif self.installation_type == 7:
                self.ufactor_installation = 1.86
            elif self.installation_type == 8:
                self.ufactor_installation = 1.84
            elif self.installation_type == 9:
                self.ufactor_installation = 1.74
            elif self.installation_type == 10:
                self.ufactor_installation = 7.41
            elif self.installation_type == 11:
                self.ufactor_installation = 5.14
            elif self.installation_type == 12:
                self.ufactor_installation = 3
            elif self.installation_type == 13:
                self.ufactor_installation = 2.42
            elif self.installation_type == 14:
                self.ufactor_installation = 2.18
            elif self.installation_type == 15:
                self.ufactor_installation = 2.16
            elif self.installation_type == 16:
                self.ufactor_installation = 2.96
            elif self.installation_type == 17:
                self.ufactor_installation = 5.13
            elif self.installation_type == 18:
                self.ufactor_installation = 4.36
            elif self.installation_type == 19:
                self.ufactor_installation = 4.13
            elif self.installation_type == 20:
                self.ufactor_installation = 3.79
            elif self.installation_type == 21:
                self.ufactor_installation = 3.56
            elif self.installation_type == 22:
                self.ufactor_installation = 3.94
            else:
                self.ufactor_installation = 2.78

        elif self.glazing_types == 23:
            if self.installation_type == 0:
                self.ufactor_installation = 3.98
            elif self.installation_type == 1:
                self.ufactor_installation = 3.01
            elif self.installation_type == 2:
                self.ufactor_installation = 2.68
            elif self.installation_type == 3:
                self.ufactor_installation = 2.58
            elif self.installation_type == 4:
                self.ufactor_installation = 2.31
            elif self.installation_type == 5:
                self.ufactor_installation = 3.20
            elif self.installation_type == 6:
                self.ufactor_installation = 2.84
            elif self.installation_type == 7:
                self.ufactor_installation = 2.52
            elif self.installation_type == 8:
                self.ufactor_installation = 2.50
            elif self.installation_type == 9:
                self.ufactor_installation = 2.39
            elif self.installation_type == 10:
                self.ufactor_installation = 8.61
            elif self.installation_type == 11:
                self.ufactor_installation = 6.33
            elif self.installation_type == 12:
                self.ufactor_installation = 3.69
            elif self.installation_type == 13:
                self.ufactor_installation = 3.11
            elif self.installation_type == 14:
                self.ufactor_installation = 2.88
            elif self.installation_type == 15:
                self.ufactor_installation = 2.39
            elif self.installation_type == 16:
                self.ufactor_installation = 3.12
            elif self.installation_type == 17:
                self.ufactor_installation = 5.35
            elif self.installation_type == 18:
                self.ufactor_installation = 4.58
            elif self.installation_type == 19:
                self.ufactor_installation = 4.34
            elif self.installation_type == 20:
                self.ufactor_installation = 3.99
            elif self.installation_type == 21:
                self.ufactor_installation = 3.76
            elif self.installation_type == 22:
                self.ufactor_installation = 4.10
            else:
                self.ufactor_installation = 2.97

        elif self.glazing_types == 24:
            if self.installation_type == 0:
                self.ufactor_installation = 3.47
            elif self.installation_type == 1:
                self.ufactor_installation = 2.53
            elif self.installation_type == 2:
                self.ufactor_installation = 2.24
            elif self.installation_type == 3:
                self.ufactor_installation = 2.14
            elif self.installation_type == 4:
                self.ufactor_installation = 1.88
            elif self.installation_type == 5:
                self.ufactor_installation = 2.66
            elif self.installation_type == 6:
                self.ufactor_installation = 2.30
            elif self.installation_type == 7:
                self.ufactor_installation = 2
            elif self.installation_type == 8:
                self.ufactor_installation = 1.98
            elif self.installation_type == 9:
                self.ufactor_installation = 1.88
            elif self.installation_type == 10:
                self.ufactor_installation = 7.67
            elif self.installation_type == 11:
                self.ufactor_installation = 5.39
            elif self.installation_type == 12:
                self.ufactor_installation = 3.15
            elif self.installation_type == 13:
                self.ufactor_installation = 2.56
            elif self.installation_type == 14:
                self.ufactor_installation = 2.33
            elif self.installation_type == 15:
                self.ufactor_installation = 2.44
            elif self.installation_type == 16:
                self.ufactor_installation = 3.16
            elif self.installation_type == 17:
                self.ufactor_installation = 5.41
            elif self.installation_type == 18:
                self.ufactor_installation = 4.64
            elif self.installation_type == 19:
                self.ufactor_installation = 4.40
            elif self.installation_type == 20:
                self.ufactor_installation = 4.04
            elif self.installation_type == 21:
                self.ufactor_installation = 3.81
            elif self.installation_type == 22:
                self.ufactor_installation = 4.14
            else:
                self.ufactor_installation = 3.02

        elif self.glazing_types == 25:
            if self.installation_type == 0:
                self.ufactor_installation = 3.61
            elif self.installation_type == 1:
                self.ufactor_installation = 2.66
            elif self.installation_type == 2:
                self.ufactor_installation = 2.36
            elif self.installation_type == 3:
                self.ufactor_installation = 2.26
            elif self.installation_type == 4:
                self.ufactor_installation = 2
            elif self.installation_type == 5:
                self.ufactor_installation = 2.81
            elif self.installation_type == 6:
                self.ufactor_installation = 2.45
            elif self.installation_type == 7:
                self.ufactor_installation = 2.15
            elif self.installation_type == 8:
                self.ufactor_installation = 2.12
            elif self.installation_type == 9:
                self.ufactor_installation = 2.02
            elif self.installation_type == 10:
                self.ufactor_installation = 7.93
            elif self.installation_type == 11:
                self.ufactor_installation = 5.56
            elif self.installation_type == 12:
                self.ufactor_installation = 3.3
            elif self.installation_type == 13:
                self.ufactor_installation = 2.71
            elif self.installation_type == 14:
                self.ufactor_installation = 2.48
            elif self.installation_type == 15:
                self.ufactor_installation = 1.93
            elif self.installation_type == 16:
                self.ufactor_installation = 2.79
            elif self.installation_type == 17:
                self.ufactor_installation = 4.91
            elif self.installation_type == 18:
                self.ufactor_installation = 4.14
            elif self.installation_type == 19:
                self.ufactor_installation = 3.91
            elif self.installation_type == 20:
                self.ufactor_installation = 3.58
            elif self.installation_type == 21:
                self.ufactor_installation = 3.37
            elif self.installation_type == 22:
                self.ufactor_installation = 3.37
            else:
                self.ufactor_installation = 2.58

        elif self.glazing_types == 26:
            if self.installation_type == 0:
                self.ufactor_installation = 3.24
            elif self.installation_type == 1:
                self.ufactor_installation = 2.31
            elif self.installation_type == 2:
                self.ufactor_installation = 2.04
            elif self.installation_type == 3:
                self.ufactor_installation = 1.94
            elif self.installation_type == 4:
                self.ufactor_installation = 1.69
            elif self.installation_type == 5:
                self.ufactor_installation = 2.42
            elif self.installation_type == 6:
                self.ufactor_installation = 2.06
            elif self.installation_type == 7:
                self.ufactor_installation = 1.76
            elif self.installation_type == 8:
                self.ufactor_installation = 1.74
            elif self.installation_type == 9:
                self.ufactor_installation = 1.65
            elif self.installation_type == 10:
                self.ufactor_installation = 7.24
            elif self.installation_type == 11:
                self.ufactor_installation = 4.96
            elif self.installation_type == 12:
                self.ufactor_installation = 2.9
            elif self.installation_type == 13:
                self.ufactor_installation = 2.32
            elif self.installation_type == 14:
                self.ufactor_installation = 2.09
            elif self.installation_type == 15:
                self.ufactor_installation = 2.04
            elif self.installation_type == 16:
                self.ufactor_installation = 2.88
            elif self.installation_type == 17:
                self.ufactor_installation = 5.02
            elif self.installation_type == 18:
                self.ufactor_installation = 4.25
            elif self.installation_type == 19:
                self.ufactor_installation = 4.02
            elif self.installation_type == 20:
                self.ufactor_installation = 3.69
            elif self.installation_type == 21:
                self.ufactor_installation = 3.46
            elif self.installation_type == 22:
                self.ufactor_installation = 3.86
            else:
                self.ufactor_installation = 2.68

        elif self.glazing_types == 27:
            if self.installation_type == 0:
                self.ufactor_installation = 3.78
            elif self.installation_type == 1:
                self.ufactor_installation = 2.78
            elif self.installation_type == 2:
                self.ufactor_installation = 2.46
            elif self.installation_type == 3:
                self.ufactor_installation = 2.42
            elif self.installation_type == 4:
                self.ufactor_installation = 2.17
            elif self.installation_type == 5:
                self.ufactor_installation = 3.02
            elif self.installation_type == 6:
                self.ufactor_installation = 2.68
            elif self.installation_type == 7:
                self.ufactor_installation = 2.36
            elif self.installation_type == 8:
                self.ufactor_installation = 2.36
            elif self.installation_type == 9:
                self.ufactor_installation = 2.25
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.48
            elif self.installation_type == 13:
                self.ufactor_installation = 2.91
            elif self.installation_type == 14:
                self.ufactor_installation = 2.62
            elif self.installation_type == 15:
                self.ufactor_installation = 2.22
            elif self.installation_type == 16:
                self.ufactor_installation = 3
            elif self.installation_type == 17:
                self.ufactor_installation = 5.13
            elif self.installation_type == 18:
                self.ufactor_installation = 4.24
            elif self.installation_type == 19:
                self.ufactor_installation = 4.03
            elif self.installation_type == 20:
                self.ufactor_installation = 3.63
            elif self.installation_type == 21:
                self.ufactor_installation = 3.55
            elif self.installation_type == 22:
                self.ufactor_installation = 3.92
            else:
                self.ufactor_installation = 2.70

        elif self.glazing_types == 28:
            if self.installation_type == 0:
                self.ufactor_installation = 3.46
            elif self.installation_type == 1:
                self.ufactor_installation = 2.47
            elif self.installation_type == 2:
                self.ufactor_installation = 2.18
            elif self.installation_type == 3:
                self.ufactor_installation = 2.14
            elif self.installation_type == 4:
                self.ufactor_installation = 1.9
            elif self.installation_type == 5:
                self.ufactor_installation = 2.68
            elif self.installation_type == 6:
                self.ufactor_installation = 2.34
            elif self.installation_type == 7:
                self.ufactor_installation = 2.03
            elif self.installation_type == 8:
                self.ufactor_installation = 2.03
            elif self.installation_type == 9:
                self.ufactor_installation = 1.92
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.14
            elif self.installation_type == 13:
                self.ufactor_installation = 2.57
            elif self.installation_type == 14:
                self.ufactor_installation = 2.27
            elif self.installation_type == 15:
                self.ufactor_installation = 2.04
            elif self.installation_type == 16:
                self.ufactor_installation = 2.88
            elif self.installation_type == 17:
                self.ufactor_installation = 4.96
            elif self.installation_type == 18:
                self.ufactor_installation = 4.07
            elif self.installation_type == 19:
                self.ufactor_installation = 3.87
            elif self.installation_type == 20:
                self.ufactor_installation = 3.48
            elif self.installation_type == 21:
                self.ufactor_installation = 3.40
            elif self.installation_type == 22:
                self.ufactor_installation = 3.80
            else:
                self.ufactor_installation = 2.56

        elif self.glazing_types == 29:
            if self.installation_type == 0:
                self.ufactor_installation = 3.60
            elif self.installation_type == 1:
                self.ufactor_installation = 2.60
            elif self.installation_type == 2:
                self.ufactor_installation = 2.30
            elif self.installation_type == 3:
                self.ufactor_installation = 2.26
            elif self.installation_type == 4:
                self.ufactor_installation = 2.02
            elif self.installation_type == 5:
                self.ufactor_installation = 2.82
            elif self.installation_type == 6:
                self.ufactor_installation = 2.49
            elif self.installation_type == 7:
                self.ufactor_installation = 2.17
            elif self.installation_type == 8:
                self.ufactor_installation = 2.17
            elif self.installation_type == 9:
                self.ufactor_installation = 2.06
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.28
            elif self.installation_type == 13:
                self.ufactor_installation = 2.71
            elif self.installation_type == 14:
                self.ufactor_installation = 2.42
            elif self.installation_type == 15:
                self.ufactor_installation = 1.99
            elif self.installation_type == 16:
                self.ufactor_installation = 2.83
            elif self.installation_type == 17:
                self.ufactor_installation = 4.91
            elif self.installation_type == 18:
                self.ufactor_installation = 4.01
            elif self.installation_type == 19:
                self.ufactor_installation = 3.81
            elif self.installation_type == 20:
                self.ufactor_installation = 3.43
            elif self.installation_type == 21:
                self.ufactor_installation = 3.35
            elif self.installation_type == 22:
                self.ufactor_installation = 3.76
            else:
                self.ufactor_installation = 2.51

        elif self.glazing_types == 30:
            if self.installation_type == 0:
                self.ufactor_installation = 3.36
            elif self.installation_type == 1:
                self.ufactor_installation = 2.39
            elif self.installation_type == 2:
                self.ufactor_installation = 2.10
            elif self.installation_type == 3:
                self.ufactor_installation = 2.06
            elif self.installation_type == 4:
                self.ufactor_installation = 1.83
            elif self.installation_type == 5:
                self.ufactor_installation = 2.58
            elif self.installation_type == 6:
                self.ufactor_installation = 2.24
            elif self.installation_type == 7:
                self.ufactor_installation = 1.93
            elif self.installation_type == 8:
                self.ufactor_installation = 1.93
            elif self.installation_type == 9:
                self.ufactor_installation = 1.83
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.04
            elif self.installation_type == 13:
                self.ufactor_installation = 2.47
            elif self.installation_type == 14:
                self.ufactor_installation = 2.17
            elif self.installation_type == 15:
                self.ufactor_installation = 1.87
            elif self.installation_type == 16:
                self.ufactor_installation = 2.75
            elif self.installation_type == 17:
                self.ufactor_installation = 4.8
            elif self.installation_type == 18:
                self.ufactor_installation = 3.9
            elif self.installation_type == 19:
                self.ufactor_installation = 3.7
            elif self.installation_type == 20:
                self.ufactor_installation = 3.33
            elif self.installation_type == 21:
                self.ufactor_installation = 3.25
            elif self.installation_type == 22:
                self.ufactor_installation = 3.68
            else:
                self.ufactor_installation = 2.4

        elif self.glazing_types == 31:
            if self.installation_type == 0:
                self.ufactor_installation = 3.55
            elif self.installation_type == 1:
                self.ufactor_installation = 2.56
            elif self.installation_type == 2:
                self.ufactor_installation = 2.26
            elif self.installation_type == 3:
                self.ufactor_installation = 2.22
            elif self.installation_type == 4:
                self.ufactor_installation = 1.98
            elif self.installation_type == 5:
                self.ufactor_installation = 2.78
            elif self.installation_type == 6:
                self.ufactor_installation = 2.44
            elif self.installation_type == 7:
                self.ufactor_installation = 2.12
            elif self.installation_type == 8:
                self.ufactor_installation = 2.12
            elif self.installation_type == 9:
                self.ufactor_installation = 2.01
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.23
            elif self.installation_type == 13:
                self.ufactor_installation = 2.66
            elif self.installation_type == 14:
                self.ufactor_installation = 2.37
            elif self.installation_type == 15:
                self.ufactor_installation = 1.93
            elif self.installation_type == 16:
                self.ufactor_installation = 2.79
            elif self.installation_type == 17:
                self.ufactor_installation = 4.85
            elif self.installation_type == 18:
                self.ufactor_installation = 3.96
            elif self.installation_type == 19:
                self.ufactor_installation = 3.76
            elif self.installation_type == 20:
                self.ufactor_installation = 3.38
            elif self.installation_type == 21:
                self.ufactor_installation = 3.3
            elif self.installation_type == 22:
                self.ufactor_installation = 3.72
            else:
                self.ufactor_installation = 2.46

        elif self.glazing_types == 32:
            if self.installation_type == 0:
                self.ufactor_installation = 3.18
            elif self.installation_type == 1:
                self.ufactor_installation = 2.21
            elif self.installation_type == 2:
                self.ufactor_installation = 1.94
            elif self.installation_type == 3:
                self.ufactor_installation = 1.9
            elif self.installation_type == 4:
                self.ufactor_installation = 1.67
            elif self.installation_type == 5:
                self.ufactor_installation = 2.38
            elif self.installation_type == 6:
                self.ufactor_installation = 2.05
            elif self.installation_type == 7:
                self.ufactor_installation = 1.74
            elif self.installation_type == 8:
                self.ufactor_installation = 1.74
            elif self.installation_type == 9:
                self.ufactor_installation = 1.64
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.84
            elif self.installation_type == 13:
                self.ufactor_installation = 2.27
            elif self.installation_type == 14:
                self.ufactor_installation = 1.97
            elif self.installation_type == 15:
                self.ufactor_installation = 1.76
            elif self.installation_type == 16:
                self.ufactor_installation = 2.67
            elif self.installation_type == 17:
                self.ufactor_installation = 4.68
            elif self.installation_type == 18:
                self.ufactor_installation = 3.79
            elif self.installation_type == 19:
                self.ufactor_installation = 3.59
            elif self.installation_type == 20:
                self.ufactor_installation = 3.22
            elif self.installation_type == 21:
                self.ufactor_installation = 3.16
            elif self.installation_type == 22:
                self.ufactor_installation = 3.59
            else:
                self.ufactor_installation = 2.31

        elif self.glazing_types == 33:
            if self.installation_type == 0:
                self.ufactor_installation = 3.32
            elif self.installation_type == 1:
                self.ufactor_installation = 2.34
            elif self.installation_type == 2:
                self.ufactor_installation = 2.06
            elif self.installation_type == 3:
                self.ufactor_installation = 2.02
            elif self.installation_type == 4:
                self.ufactor_installation = 1.79
            elif self.installation_type == 5:
                self.ufactor_installation = 2.53
            elif self.installation_type == 6:
                self.ufactor_installation = 2.20
            elif self.installation_type == 7:
                self.ufactor_installation = 1.89
            elif self.installation_type == 8:
                self.ufactor_installation = 1.89
            elif self.installation_type == 9:
                self.ufactor_installation = 1.78
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.99
            elif self.installation_type == 13:
                self.ufactor_installation = 2.42
            elif self.installation_type == 14:
                self.ufactor_installation = 2.12
            elif self.installation_type == 15:
                self.ufactor_installation = 1.59
            elif self.installation_type == 16:
                self.ufactor_installation = 2.54
            elif self.installation_type == 17:
                self.ufactor_installation = 4.52
            elif self.installation_type == 18:
                self.ufactor_installation = 3.63
            elif self.installation_type == 19:
                self.ufactor_installation = 3.43
            elif self.installation_type == 20:
                self.ufactor_installation = 3.07
            elif self.installation_type == 21:
                self.ufactor_installation = 3.01
            elif self.installation_type == 22:
                self.ufactor_installation = 3.47
            else:
                self.ufactor_installation = 2.17

        elif self.glazing_types == 34:
            if self.installation_type == 0:
                self.ufactor_installation = 3.04
            elif self.installation_type == 1:
                self.ufactor_installation = 2.08
            elif self.installation_type == 2:
                self.ufactor_installation = 1.82
            elif self.installation_type == 3:
                self.ufactor_installation = 1.78
            elif self.installation_type == 4:
                self.ufactor_installation = 1.55
            elif self.installation_type == 5:
                self.ufactor_installation = 2.24
            elif self.installation_type == 6:
                self.ufactor_installation = 1.9
            elif self.installation_type == 7:
                self.ufactor_installation = 1.6
            elif self.installation_type == 8:
                self.ufactor_installation = 1.6
            elif self.installation_type == 9:
                self.ufactor_installation = 1.5
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.69
            elif self.installation_type == 13:
                self.ufactor_installation = 2.12
            elif self.installation_type == 14:
                self.ufactor_installation = 1.83
            elif self.installation_type == 15:
                self.ufactor_installation = 1.53
            elif self.installation_type == 16:
                self.ufactor_installation = 2.49
            elif self.installation_type == 1:
                self.ufactor_installation = 4.46
            elif self.installation_type == 18:
                self.ufactor_installation = 3.57
            elif self.installation_type == 19:
                self.ufactor_installation = 3.57
            elif self.installation_type == 20:
                self.ufactor_installation = 3.02
            elif self.installation_type == 21:
                self.ufactor_installation = 2.96
            elif self.installation_type == 22:
                self.ufactor_installation = 3.43
            else:
                self.ufactor_installation = 2.12

        elif self.glazing_types == 35:
            if self.installation_type == 0:
                self.ufactor_installation = 3.36
            elif self.installation_type == 1:
                self.ufactor_installation = 2.39
            elif self.installation_type == 2:
                self.ufactor_installation = 2.10
            elif self.installation_type == 3:
                self.ufactor_installation = 2.06
            elif self.installation_type == 4:
                self.ufactor_installation = 1.83
            elif self.installation_type == 5:
                self.ufactor_installation = 2.58
            elif self.installation_type == 6:
                self.ufactor_installation = 2.24
            elif self.installation_type == 7:
                self.ufactor_installation = 1.93
            elif self.installation_type == 8:
                self.ufactor_installation = 1.93
            elif self.installation_type == 9:
                self.ufactor_installation = 1.83
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 3.04
            elif self.installation_type == 13:
                self.ufactor_installation = 2.47
            elif self.installation_type == 14:
                self.ufactor_installation = 2.17
            elif self.installation_type == 15:
                self.ufactor_installation = 1.65
            elif self.installation_type == 16:
                self.ufactor_installation = 2.58
            elif self.installation_type == 17:
                self.ufactor_installation = 4.57
            elif self.installation_type == 18:
                self.ufactor_installation = 3.68
            elif self.installation_type == 19:
                self.ufactor_installation = 3.48
            elif self.installation_type == 20:
                self.ufactor_installation = 3.12
            elif self.installation_type == 21:
                self.ufactor_installation = 3.06
            elif self.installation_type == 22:
                self.ufactor_installation = 3.51
            else:
                self.ufactor_installation = 2.22

        elif self.glazing_types == 36:
            if self.installation_type == 0:
                self.ufactor_installation = 2.95
            elif self.installation_type == 1:
                self.ufactor_installation = 1.99
            elif self.installation_type == 2:
                self.ufactor_installation = 1.74
            elif self.installation_type == 3:
                self.ufactor_installation = 1.69
            elif self.installation_type == 4:
                self.ufactor_installation = 1.48
            elif self.installation_type == 5:
                self.ufactor_installation = 2.14
            elif self.installation_type == 6:
                self.ufactor_installation = 1.80
            elif self.installation_type == 7:
                self.ufactor_installation = 1.50
            elif self.installation_type == 8:
                self.ufactor_installation = 1.50
            elif self.installation_type == 9:
                self.ufactor_installation = 1.40
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.59
            elif self.installation_type == 13:
                self.ufactor_installation = 2.02
            elif self.installation_type == 14:
                self.ufactor_installation = 1.73
            elif self.installation_type == 15:
                self.ufactor_installation = 1.53
            elif self.installation_type == 16:
                self.ufactor_installation = 2.49
            elif self.installation_type == 17:
                self.ufactor_installation = 4.46
            elif self.installation_type == 18:
                self.ufactor_installation = 3.57
            elif self.installation_type == 19:
                self.ufactor_installation = 3.57
            elif self.installation_type == 20:
                self.ufactor_installation = 3.02
            elif self.installation_type == 21:
                self.ufactor_installation = 2.96
            elif self.installation_type == 22:
                self.ufactor_installation = 3.43
            else:
                self.ufactor_installation = 2.12

        elif self.glazing_types == 37:
            if self.installation_type == 0:
                self.ufactor_installation = 3.09
            elif self.installation_type == 1:
                self.ufactor_installation = 2.12
            elif self.installation_type == 2:
                self.ufactor_installation = 1.86
            elif self.installation_type == 3:
                self.ufactor_installation = 1.82
            elif self.installation_type == 4:
                self.ufactor_installation = 1.59
            elif self.installation_type == 5:
                self.ufactor_installation = 2.29
            elif self.installation_type == 6:
                self.ufactor_installation = 1.95
            elif self.installation_type == 7:
                self.ufactor_installation = 1.65
            elif self.installation_type == 8:
                self.ufactor_installation = 1.65
            elif self.installation_type == 9:
                self.ufactor_installation = 1.55
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.47
            elif self.installation_type == 13:
                self.ufactor_installation = 2.17
            elif self.installation_type == 14:
                self.ufactor_installation = 1.87
            elif self.installation_type == 15:
                self.ufactor_installation = 1.36
            elif self.installation_type == 16:
                self.ufactor_installation = 2.36
            elif self.installation_type == 17:
                self.ufactor_installation = 4.29
            elif self.installation_type == 18:
                self.ufactor_installation = 3.40
            elif self.installation_type == 19:
                self.ufactor_installation = 3.21
            elif self.installation_type == 20:
                self.ufactor_installation = 2.86
            elif self.installation_type == 21:
                self.ufactor_installation = 2.81
            elif self.installation_type == 22:
                self.ufactor_installation = 3.3
            else:
                self.ufactor_installation = 1.97

        elif self.glazing_types == 38:
            if self.installation_type == 0:
                self.ufactor_installation = 2.81
            elif self.installation_type == 1:
                self.ufactor_installation = 1.86
            elif self.installation_type == 2:
                self.ufactor_installation = 1.62
            elif self.installation_type == 3:
                self.ufactor_installation = 1.57
            elif self.installation_type == 4:
                self.ufactor_installation = 1.36
            elif self.installation_type == 5:
                self.ufactor_installation = 1.99
            elif self.installation_type == 6:
                self.ufactor_installation = 1.65
            elif self.installation_type == 7:
                self.ufactor_installation = 1.36
            elif self.installation_type == 8:
                self.ufactor_installation = 1.36
            elif self.installation_type == 9:
                self.ufactor_installation = 1.26
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.44
            elif self.installation_type == 13:
                self.ufactor_installation = 1.87
            elif self.installation_type == 14:
                self.ufactor_installation = 1.58
            elif self.installation_type == 15:
                self.ufactor_installation = 1.25
            elif self.installation_type == 16:
                self.ufactor_installation = 2.28
            elif self.installation_type == 17:
                self.ufactor_installation = 4.18
            elif self.installation_type == 18:
                self.ufactor_installation = 3.29
            elif self.installation_type == 19:
                self.ufactor_installation = 3.10
            elif self.installation_type == 20:
                self.ufactor_installation = 2.76
            elif self.installation_type == 21:
                self.ufactor_installation = 2.71
            elif self.installation_type == 22:
                self.ufactor_installation = 3.22
            else:
                self.ufactor_installation = 1.87

        elif self.glazing_types == 39:
            if self.installation_type == 0:
                self.ufactor_installation = 3.27
            elif self.installation_type == 1:
                self.ufactor_installation = 2.30
            elif self.installation_type == 2:
                self.ufactor_installation = 2.02
            elif self.installation_type == 3:
                self.ufactor_installation = 1.98
            elif self.installation_type == 4:
                self.ufactor_installation = 1.75
            elif self.installation_type == 5:
                self.ufactor_installation = 2.48
            elif self.installation_type == 6:
                self.ufactor_installation = 2.15
            elif self.installation_type == 7:
                self.ufactor_installation = 1.84
            elif self.installation_type == 8:
                self.ufactor_installation = 1.84
            elif self.installation_type == 9:
                self.ufactor_installation = 1.73
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.94
            elif self.installation_type == 13:
                self.ufactor_installation = 2.37
            elif self.installation_type == 14:
                self.ufactor_installation = 2.07
            elif self.installation_type == 15:
                self.ufactor_installation = 1.53
            elif self.installation_type == 16:
                self.ufactor_installation = 2.49
            elif self.installation_type == 17:
                self.ufactor_installation = 4.46
            elif self.installation_type == 18:
                self.ufactor_installation = 3.57
            elif self.installation_type == 19:
                self.ufactor_installation = 3.37
            elif self.installation_type == 20:
                self.ufactor_installation = 3.02
            elif self.installation_type == 21:
                self.ufactor_installation = 2.96
            elif self.installation_type == 22:
                self.ufactor_installation = 3.43
            else:
                self.ufactor_installation = 2.12

        elif self.glazing_types == 40:
            if self.installation_type == 0:
                self.ufactor_installation = 2.85
            elif self.installation_type == 1:
                self.ufactor_installation = 1.9
            elif self.installation_type == 2:
                self.ufactor_installation = 1.66
            elif self.installation_type == 3:
                self.ufactor_installation = 1.61
            elif self.installation_type == 4:
                self.ufactor_installation = 1.4
            elif self.installation_type == 5:
                self.ufactor_installation = 2.04
            elif self.installation_type == 6:
                self.ufactor_installation = 1.7
            elif self.installation_type == 7:
                self.ufactor_installation = 1.41
            elif self.installation_type == 8:
                self.ufactor_installation = 1.41
            elif self.installation_type == 9:
                self.ufactor_installation = 1.31
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.49
            elif self.installation_type == 13:
                self.ufactor_installation = 1.92
            elif self.installation_type == 14:
                self.ufactor_installation = 1.63
            elif self.installation_type == 15:
                self.ufactor_installation = 1.42
            elif self.installation_type == 16:
                self.ufactor_installation = 2.41
            elif self.installation_type == 17:
                self.ufactor_installation = 4.35
            elif self.installation_type == 18:
                self.ufactor_installation = 3.46
            elif self.installation_type == 19:
                self.ufactor_installation = 3.27
            elif self.installation_type == 20:
                self.ufactor_installation = 2.91
            elif self.installation_type == 21:
                self.ufactor_installation = 2.86
            elif self.installation_type == 22:
                self.ufactor_installation = 3.34
            else:
                self.ufactor_installation = 2.02

        elif self.glazing_types == 41:
            if self.installation_type == 0:
                self.ufactor_installation = 2.99
            elif self.installation_type == 1:
                self.ufactor_installation = 2.04
            elif self.installation_type == 2:
                self.ufactor_installation = 1.78
            elif self.installation_type == 3:
                self.ufactor_installation = 1.73
            elif self.installation_type == 4:
                self.ufactor_installation = 1.52
            elif self.installation_type == 5:
                self.ufactor_installation = 2.19
            elif self.installation_type == 6:
                self.ufactor_installation = 1.85
            elif self.installation_type == 7:
                self.ufactor_installation = 1.55
            elif self.installation_type == 8:
                self.ufactor_installation = 1.55
            elif self.installation_type == 9:
                self.ufactor_installation = 1.45
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.64
            elif self.installation_type == 13:
                self.ufactor_installation = 2.07
            elif self.installation_type == 14:
                self.ufactor_installation = 1.78
            elif self.installation_type == 15:
                self.ufactor_installation = 1.19
            elif self.installation_type == 16:
                self.ufactor_installation = 2.23
            elif self.installation_type == 17:
                self.ufactor_installation = 4.13
            elif self.installation_type == 18:
                self.ufactor_installation = 3.24
            elif self.installation_type == 19:
                self.ufactor_installation = 3.04
            elif self.installation_type == 20:
                self.ufactor_installation = 2.71
            elif self.installation_type == 21:
                self.ufactor_installation = 2.66
            elif self.installation_type == 22:
                self.ufactor_installation = 3.18
            else:
                self.ufactor_installation = 1.82

        elif self.glazing_types == 42:
            if self.installation_type == 0:
                self.ufactor_installation = 2.67
            elif self.installation_type == 1:
                self.ufactor_installation = 1.73
            elif self.installation_type == 2:
                self.ufactor_installation = 1.49
            elif self.installation_type == 3:
                self.ufactor_installation = 1.45
            elif self.installation_type == 4:
                self.ufactor_installation = 1.24
            elif self.installation_type == 5:
                self.ufactor_installation = 1.84
            elif self.installation_type == 6:
                self.ufactor_installation = 1.52
            elif self.installation_type == 7:
                self.ufactor_installation = 1.22
            elif self.installation_type == 8:
                self.ufactor_installation = 1.22
            elif self.installation_type == 9:
                self.ufactor_installation = 1.12
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.29
            elif self.installation_type == 13:
                self.ufactor_installation = 1.72
            elif self.installation_type == 14:
                self.ufactor_installation = 1.43
            elif self.installation_type == 15:
                self.ufactor_installation = 1.14
            elif self.installation_type == 16:
                self.ufactor_installation = 2.19
            elif self.installation_type == 17:
                self.ufactor_installation = 4.07
            elif self.installation_type == 18:
                self.ufactor_installation = 3.18
            elif self.installation_type == 19:
                self.ufactor_installation = 2.99
            elif self.installation_type == 20:
                self.ufactor_installation = 2.66
            elif self.installation_type == 21:
                self.ufactor_installation = 2.61
            elif self.installation_type == 22:
                self.ufactor_installation = 3.13
            else:
                self.ufactor_installation = 1.77

        elif self.glazing_types == 43:
            if self.installation_type == 0:
                self.ufactor_installation = 3.04
            elif self.installation_type == 1:
                self.ufactor_installation = 2.08
            elif self.installation_type == 2:
                self.ufactor_installation = 1.82
            elif self.installation_type == 3:
                self.ufactor_installation = 1.78
            elif self.installation_type == 4:
                self.ufactor_installation = 1.55
            elif self.installation_type == 5:
                self.ufactor_installation = 2.24
            elif self.installation_type == 6:
                self.ufactor_installation = 1.9
            elif self.installation_type == 7:
                self.ufactor_installation = 1.6
            elif self.installation_type == 8:
                self.ufactor_installation = 1.6
            elif self.installation_type == 9:
                self.ufactor_installation = 1.5
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.69
            elif self.installation_type == 13:
                self.ufactor_installation = 2.12
            elif self.installation_type == 14:
                self.ufactor_installation = 1.83
            elif self.installation_type == 15:
                self.ufactor_installation = 1.25
            elif self.installation_type == 16:
                self.ufactor_installation = 2.28
            elif self.installation_type == 17:
                self.ufactor_installation = 4.18
            elif self.installation_type == 18:
                self.ufactor_installation = 3.29
            elif self.installation_type == 19:
                self.ufactor_installation = 3.10
            elif self.installation_type == 20:
                self.ufactor_installation = 2.76
            elif self.installation_type == 21:
                self.ufactor_installation = 2.71
            elif self.installation_type == 22:
                self.ufactor_installation = 3.22
            else:
                self.ufactor_installation = 1.87

        elif self.glazing_types == 44:
            if self.installation_type == 0:
                self.ufactor_installation = 2.71
            elif self.installation_type == 1:
                self.ufactor_installation = 1.77
            elif self.installation_type == 2:
                self.ufactor_installation = 1.54
            elif self.installation_type == 3:
                self.ufactor_installation = 1.49
            elif self.installation_type == 4:
                self.ufactor_installation = 1.28
            elif self.installation_type == 5:
                self.ufactor_installation = 1.89
            elif self.installation_type == 6:
                self.ufactor_installation = 1.55
            elif self.installation_type == 7:
                self.ufactor_installation = 1.26
            elif self.installation_type == 8:
                self.ufactor_installation = 1.26
            elif self.installation_type == 9:
                self.ufactor_installation = 1.17
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.34
            elif self.installation_type == 13:
                self.ufactor_installation = 1.77
            elif self.installation_type == 14:
                self.ufactor_installation = 1.48
            elif self.installation_type == 15:
                self.ufactor_installation = 1.08
            elif self.installation_type == 16:
                self.ufactor_installation = 2.14
            elif self.installation_type == 17:
                self.ufactor_installation = 4.02
            elif self.installation_type == 18:
                self.ufactor_installation = 3.12
            elif self.installation_type == 19:
                self.ufactor_installation = 2.93
            elif self.installation_type == 20:
                self.ufactor_installation = 2.60
            elif self.installation_type == 21:
                self.ufactor_installation = 2.56
            elif self.installation_type == 22:
                self.ufactor_installation = 3.09
            else:
                self.ufactor_installation = 1.72

        elif self.glazing_types == 45:
            if self.installation_type == 0:
                self.ufactor_installation = 2.81
            elif self.installation_type == 1:
                self.ufactor_installation = 1.87
            elif self.installation_type == 2:
                self.ufactor_installation = 1.62
            elif self.installation_type == 3:
                self.ufactor_installation = 1.57
            elif self.installation_type == 4:
                self.ufactor_installation = 1.36
            elif self.installation_type == 5:
                self.ufactor_installation = 1.99
            elif self.installation_type == 6:
                self.ufactor_installation = 1.65
            elif self.installation_type == 7:
                self.ufactor_installation = 1.36
            elif self.installation_type == 8:
                self.ufactor_installation = 1.36
            elif self.installation_type == 9:
                self.ufactor_installation = 1.26
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.44
            elif self.installation_type == 13:
                self.ufactor_installation = 1.87
            elif self.installation_type == 14:
                self.ufactor_installation = 1.58
            elif self.installation_type == 15:
                self.ufactor_installation = 1.02
            elif self.installation_type == 16:
                self.ufactor_installation = 2.10
            elif self.installation_type == 17:
                self.ufactor_installation = 3.96
            elif self.installation_type == 18:
                self.ufactor_installation = 3.07
            elif self.installation_type == 19:
                self.ufactor_installation = 2.88
            elif self.installation_type == 20:
                self.ufactor_installation = 2.55
            elif self.installation_type == 21:
                self.ufactor_installation = 2.51
            elif self.installation_type == 22:
                self.ufactor_installation = 3.05
            else:
                self.ufactor_installation = 1.67

        elif self.glazing_types == 46:
            if self.installation_type == 0:
                self.ufactor_installation = 2.57
            elif self.installation_type == 1:
                self.ufactor_installation = 1.64
            elif self.installation_type == 2:
                self.ufactor_installation = 1.41
            elif self.installation_type == 3:
                self.ufactor_installation = 1.37
            elif self.installation_type == 4:
                self.ufactor_installation = 1.16
            elif self.installation_type == 5:
                self.ufactor_installation = 1.74
            elif self.installation_type == 6:
                self.ufactor_installation = 1.41
            elif self.installation_type == 7:
                self.ufactor_installation = 1.12
            elif self.installation_type == 8:
                self.ufactor_installation = 1.12
            elif self.installation_type == 9:
                self.ufactor_installation = 1.03
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.19
            elif self.installation_type == 13:
                self.ufactor_installation = 1.62
            elif self.installation_type == 14:
                self.ufactor_installation = 1.33
            elif self.installation_type == 15:
                self.ufactor_installation = 0.91
            elif self.installation_type == 16:
                self.ufactor_installation = 2.01
            elif self.installation_type == 17:
                self.ufactor_installation = 3.85
            elif self.installation_type == 18:
                self.ufactor_installation = 2.96
            elif self.installation_type == 19:
                self.ufactor_installation = 2.77
            elif self.installation_type == 20:
                self.ufactor_installation = 2.45
            elif self.installation_type == 21:
                self.ufactor_installation = 2.41
            elif self.installation_type == 22:
                self.ufactor_installation = 2.96
            else:
                self.ufactor_installation = 1.58

                
        else:
            if self.installation_type == 0:
                self.ufactor_installation = 2.57
            elif self.installation_type == 1:
                self.ufactor_installation = 1.64
            elif self.installation_type == 2:
                self.ufactor_installation = 1.41
            elif self.installation_type == 3:
                self.ufactor_installation = 1.37
            elif self.installation_type == 4:
                self.ufactor_installation = 1.16
            elif self.installation_type == 5:
                self.ufactor_installation = 1.74
            elif self.installation_type == 6:
                self.ufactor_installation = 1.41
            elif self.installation_type == 7:
                self.ufactor_installation = 1.12
            elif self.installation_type == 8:
                self.ufactor_installation = 1.12
            elif self.installation_type == 9:
                self.ufactor_installation = 1.03
            elif self.installation_type == 10:
                self.ufactor_installation = 1
            elif self.installation_type == 11:
                self.ufactor_installation = 1
            elif self.installation_type == 12:
                self.ufactor_installation = 2.19
            elif self.installation_type == 13:
                self.ufactor_installation = 1.62
            elif self.installation_type == 14:
                self.ufactor_installation = 1.33
            elif self.installation_type == 15:
                self.ufactor_installation = 0.74
            elif self.installation_type == 16:
                self.ufactor_installation = 1.87
            elif self.installation_type == 17:
                self.ufactor_installation = 3.68
            elif self.installation_type == 18:
                self.ufactor_installation = 2.79
            elif self.installation_type == 19:
                self.ufactor_installation = 2.60
            elif self.installation_type == 20:
                self.ufactor_installation = 2.29
            elif self.installation_type == 21:
                self.ufactor_installation = 2.26
            elif self.installation_type == 22:
                self.ufactor_installation = 2.83
            else:
                self.ufactor_installation = 1.43
        return self.ufactor_installation

    def reset_fenestration_u_factor_installation(self):
        return self.comboBox_2.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Fenestration Area Properties"))
        self.label_4.setText(_translate("Dialog", "Glazing Type :"))
        self.label_2.setText(_translate("Dialog", "Installation Type :"))
        self.pushButton_9.setText(_translate("Dialog", "Close"))
        self.pushButton_10.setText(_translate("Dialog", "Save"))
        self.comboBox.setItemText(0, _translate("Dialog", "Single Glazing-3.2 mm glass"))
        self.comboBox.setItemText(1, _translate("Dialog", "Single Glazing-6 mm acrylic/polycarb"))
        self.comboBox.setItemText(2, _translate("Dialog", "Single Glazing-3.2 mm acrylic/polycarb"))
        self.comboBox.setItemText(3, _translate("Dialog", "Double Glazing-6 mm airspace"))
        self.comboBox.setItemText(4, _translate("Dialog", "Double Glazing-13 mm airspace"))
        self.comboBox.setItemText(5, _translate("Dialog", "Double Glazing-6 mm argon space"))
        self.comboBox.setItemText(6, _translate("Dialog", "Double Glazing-13 mm argon space"))
        self.comboBox.setItemText(7, _translate("Dialog", "Double Glazing, e = 0.60 on surface 2 or 3 -6 mm airspace"))
        self.comboBox.setItemText(8, _translate("Dialog", "Double Glazing, e = 0.60 on surface 2 or 3 -13 mm airspace"))
        self.comboBox.setItemText(9, _translate("Dialog", "Double Glazing, e = 0.60 on surface 2 or 3 -6 mm argon space"))
        self.comboBox.setItemText(10, _translate("Dialog", "Double Glazing, e = 0.60 on surface 2 or 3 -13 mm argon space"))
        self.comboBox.setItemText(11, _translate("Dialog", "Double Glazing, e = 0.40 on surface 2 or 3- 6 mm airspace"))
        self.comboBox.setItemText(12, _translate("Dialog", "Double Glazing, e = 0.40 on surface 2 or 3- 13 mm airspace"))
        self.comboBox.setItemText(13, _translate("Dialog", "Double Glazing, e = 0.40 on surface 2 or 3-6 mm argon space"))
        self.comboBox.setItemText(14, _translate("Dialog", "Double Glazing, e = 0.40 on surface 2 or 3-13 mm argon space"))
        self.comboBox.setItemText(15, _translate("Dialog", "Double Glazing, e = 0.20 on surface 2 or 3- 6 mm airspace"))
        self.comboBox.setItemText(16, _translate("Dialog", "Double Glazing, e = 0.20 on surface 2 or 3- 13 mm airspace"))
        self.comboBox.setItemText(17, _translate("Dialog", "Double Glazing, e = 0.20 on surface 2 or 3-6 mm argon space"))
        self.comboBox.setItemText(18, _translate("Dialog", "Double Glazing, e = 0.20 on surface 2 or 3-13 mm argon space"))
        self.comboBox.setItemText(19, _translate("Dialog", "Double Glazing, e = 0.10 on surface 2 or 3-6 mm airspace"))
        self.comboBox.setItemText(20, _translate("Dialog", "Double Glazing, e = 0.10 on surface 2 or 3-13 mm airspace"))
        self.comboBox.setItemText(21, _translate("Dialog", "Double Glazing, e = 0.10 on surface 2 or 3-6 mm argon space"))
        self.comboBox.setItemText(22, _translate("Dialog", "Double Glazing, e = 0.10 on surface 2 or 3-13 mm argon space"))
        self.comboBox.setItemText(23, _translate("Dialog", "Double Glazing, e = 0.05 on surface 2 or 3-6 mm airspace"))
        self.comboBox.setItemText(24, _translate("Dialog", "Double Glazing, e = 0.05 on surface 2 or 3-13 mm airspace"))
        self.comboBox.setItemText(25, _translate("Dialog", "Double Glazing, e = 0.05 on surface 2 or 3-6 mm argon space"))
        self.comboBox.setItemText(26, _translate("Dialog", "Double Glazing, e = 0.05 on surface 2 or 3-13 mm argon space"))
        self.comboBox.setItemText(27, _translate("Dialog", "Triple Glazing-6 mm airspace"))
        self.comboBox.setItemText(28, _translate("Dialog", "Triple Glazing-13 mm airspace"))
        self.comboBox.setItemText(29, _translate("Dialog", "Triple Glazing-6 mm argon space"))
        self.comboBox.setItemText(30, _translate("Dialog", "Triple Glazing-13 mm argon space"))
        self.comboBox.setItemText(31, _translate("Dialog", "Triple Glazing, e = 0.20 on surface 2, 3, 4, or 5-6 mm airspace"))
        self.comboBox.setItemText(32, _translate("Dialog", "Triple Glazing, e = 0.20 on surface 2, 3, 4, or 5-13 mm airspace"))
        self.comboBox.setItemText(33, _translate("Dialog", "Triple Glazing, e = 0.20 on surface 2, 3, 4, or 5-6 mm argon space"))
        self.comboBox.setItemText(34, _translate("Dialog", "Triple Glazing, e = 0.20 on surface 2, 3, 4, or 5-13 mm argon space"))
        self.comboBox.setItemText(35, _translate("Dialog", "Triple Glazing, e = 0.20 on surfaces 2 or 3 and 4 or 5-6 mm airspace"))
        self.comboBox.setItemText(36, _translate("Dialog", "Triple Glazing, e = 0.20 on surfaces 2 or 3 and 4 or 5-13 mm airspace"))
        self.comboBox.setItemText(37, _translate("Dialog", "Triple Glazing, e = 0.20 on surfaces 2 or 3 and 4 or 5- 6 mm argon space"))
        self.comboBox.setItemText(38, _translate("Dialog", "Triple Glazing, e = 0.20 on surfaces 2 or 3 and 4 or 5 -13 mm argon space"))
        self.comboBox.setItemText(39, _translate("Dialog", "Triple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-6 mm airspace"))
        self.comboBox.setItemText(40, _translate("Dialog", "Triple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-13 mm airspace"))
        self.comboBox.setItemText(41, _translate("Dialog", "Triple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-6 mm argon space"))
        self.comboBox.setItemText(42, _translate("Dialog", "Triple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-13 mm argon space"))
        self.comboBox.setItemText(43, _translate("Dialog", "Quadruple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-6 mm airspace"))
        self.comboBox.setItemText(44, _translate("Dialog", "Quadruple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-13 mm airspace"))
        self.comboBox.setItemText(45, _translate("Dialog", "Quadruple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-6 mm argon space"))
        self.comboBox.setItemText(46, _translate("Dialog", "Quadruple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-13 mm argon space"))
        self.comboBox.setItemText(47, _translate("Dialog", "Quadruple Glazing, e = 0.10 on surfaces 2 or 3 and 4 or 5-6 mm krypton spaces"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Vertical-Operable-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Vertical-Operable-Aluminum With Thermal Break"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Vertical-Operable-Aluminum Reinforced Vinyl/Aluminum Clad Wood"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Vertical-Operable-Wood/Viny"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Vertical-Operable-Insulated Fiberglass/Vinyl"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Vertical-Fixed-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "Vertical-Fixed-Aluminum With Thermal Break"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Vertical-Fixed-Aluminum Reinforced Vinyl/Aluminum Clad Wood"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Vertical-Fixed-Wood/Viny"))
        self.comboBox_2.setItemText(9, _translate("Dialog", "Vertical-Fixed-Insulated Fiberglass/Vinyl"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "Vertical-Garden Windows-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Vertical-Garden Windows-Wood/Viny"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "Vertical-Curtainwall-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(13, _translate("Dialog", "Vertical-Curtainwall-Aluminum With Thermal Break"))
        self.comboBox_2.setItemText(14, _translate("Dialog", "Vertical-Curtainwall-Structural Glazing"))
        self.comboBox_2.setItemText(15, _translate("Dialog", "Sloped-Glass Only (Skylights)-Center of Glass"))
        self.comboBox_2.setItemText(16, _translate("Dialog", "Sloped-Glass Only (Skylights)-Edger of Glass"))
        self.comboBox_2.setItemText(17, _translate("Dialog", "Sloped-Manufactured Skylight-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(18, _translate("Dialog", "Sloped-Manufactured Skylight-Aluminum With Thermal Break"))
        self.comboBox_2.setItemText(19, _translate("Dialog", "Sloped-Manufactured Skylight-Reinforced Vinyl/Aluminum Clad Wood"))
        self.comboBox_2.setItemText(20, _translate("Dialog", "Sloped-Manufactured Skylight-Wood/Vinyl"))
        self.comboBox_2.setItemText(21, _translate("Dialog", "Sloped-Site-Assembled Sloped/Overhead Glazing-Aluminum Without Thermal Break"))
        self.comboBox_2.setItemText(22, _translate("Dialog", "Sloped-Site-Assembled Sloped/Overhead Glazing-Aluminum With Thermal Break"))
        self.comboBox_2.setItemText(23, _translate("Dialog", "Sloped-Site-Assembled Sloped/Overhead Glazing-Structural Glazing"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
