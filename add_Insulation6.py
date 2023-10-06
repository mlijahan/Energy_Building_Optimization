
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 300)
        Dialog.setMinimumSize(QtCore.QSize(850, 300))
        Dialog.setMaximumSize(QtCore.QSize(850, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 30, 297, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 230, 121, 41))
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
        self.pushButton_10.setGeometry(QtCore.QRect(520, 230, 121, 41))
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
        self.comboBox_7 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(180, 110, 651, 24))
        self.comboBox_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def K_factor(self):
        self.material_typr = self.comboBox_7.currentIndex()
        if self.material_typr == 0:
            self.rfactor = 1.47
        elif self.material_typr == 1:
            self.rfactor = 1.3
        elif self.material_typr == 2:
            self.rfactor = 1.12
        elif self.material_typr == 3:
            self.rfactor = 0.98
        elif self.material_typr == 4:
            self.rfactor = 0.85
        elif self.material_typr == 5:
            self.rfactor = 0.74
        elif self.material_typr == 6:
            self.rfactor = 0.62
        elif self.material_typr == 7:
            self.rfactor = 0.53
        elif self.material_typr == 8:
            self.rfactor = 0.45
        elif self.material_typr == 9:
            self.rfactor = 0
        elif self.material_typr == 10:
            self.rfactor = 0
        elif self.material_typr == 11:
            self.rfactor = 0
        elif self.material_typr == 12:
            self.rfactor = 0
        elif self.material_typr == 13:
            self.rfactor = 0
        elif self.material_typr == 14:
            self.rfactor = 0
        elif self.material_typr == 15:
            self.rfactor = 0.2
        elif self.material_typr == 16:
            self.rfactor = 0.22
        elif self.material_typr == 17:
            self.rfactor = 0
        elif self.material_typr == 18:
            self.rfactor = 0
        elif self.material_typr == 19:
            self.rfactor = 0
        elif self.material_typr == 20:
            self.rfactor = 0
        elif self.material_typr == 21:
            self.rfactor = 0
        elif self.material_typr == 22:
            self.rfactor = 0
        elif self.material_typr == 23:
            self.rfactor = 0
        elif self.material_typr == 24:
            self.rfactor = 0
        elif self.material_typr == 25:
            self.rfactor = 0
        elif self.material_typr == 26:
            self.rfactor = 0
        elif self.material_typr == 27:
            self.rfactor = 0
        elif self.material_typr == 28:
            self.rfactor = 0
        elif self.material_typr == 29:
            self.rfactor = 0
        elif self.material_typr == 30:
            self.rfactor = 0
        elif self.material_typr == 31:
            self.rfactor = 0
        elif self.material_typr == 32:
            self.rfactor = 0
        elif self.material_typr == 33:
            self.rfactor = 0
        elif self.material_typr == 34:
            self.rfactor = 0
        elif self.material_typr == 35:
            self.rfactor = 0
        elif self.material_typr == 36:
            self.rfactor = 0
        elif self.material_typr == 37:
            self.rfactor = 0
        elif self.material_typr == 38:
            self.rfactor = 0
        elif self.material_typr == 39:
            self.rfactor = 0
        elif self.material_typr == 40:
            self.rfactor = 10.4
        elif self.material_typr == 41:
            self.rfactor = 6.2
        elif self.material_typr == 42:
            self.rfactor = 3.46
        elif self.material_typr == 43:
            self.rfactor = 1.88
        elif self.material_typr == 44:
            self.rfactor = 4.33
        elif self.material_typr == 45:
            self.rfactor = 3.17
        elif self.material_typr == 46:
            self.rfactor = 2.31
        elif self.material_typr == 47:
            self.rfactor = 1.59
        elif self.material_typr == 48:
            self.rfactor = 1.15
        elif self.material_typr == 49:
            self.rfactor = 0
        elif self.material_typr == 50:
            self.rfactor = 0
        elif self.material_typr == 51:
            self.rfactor = 0
        elif self.material_typr == 52:
            self.rfactor = 0.57
        elif self.material_typr == 53:
            self.rfactor = 0.93
        elif self.material_typr == 54:
            self.rfactor = 2.9
        elif self.material_typr == 55:
            self.rfactor = 2.6
        elif self.material_typr == 56:
            self.rfactor = 1.9
        elif self.material_typr == 57:
            self.rfactor = 1.3
        elif self.material_typr == 58:
            self.rfactor = 0.89
        elif self.material_typr == 59:
            self.rfactor = 0.59
        elif self.material_typr == 60:
            self.rfactor = 0.36
        elif self.material_typr == 61:
            self.rfactor = 0.18
        elif self.material_typr == 62:
            self.rfactor = 0.24
        elif self.material_typr == 63:
            self.rfactor = 1.4
        elif self.material_typr == 64:
            self.rfactor = 0.97
        elif self.material_typr == 65:
            self.rfactor = 0.65
        elif self.material_typr == 66:
            self.rfactor = 0.27
        elif self.material_typr == 67:
            self.rfactor = 0.22
        elif self.material_typr == 68:
            self.rfactor = 0.16
        elif self.material_typr == 69:
            self.rfactor = 0.12
        elif self.material_typr == 70:
            self.rfactor = 0.75
        elif self.material_typr == 71:
            self.rfactor = 0.60
        elif self.material_typr == 72:
            self.rfactor = 0.44
        elif self.material_typr == 73:
            self.rfactor = 0.36
        elif self.material_typr == 74:
            self.rfactor = 0.30
        elif self.material_typr == 75:
            self.rfactor = 0.20
        elif self.material_typr == 76:
            self.rfactor = 0.12
        elif self.material_typr == 77:
            self.rfactor = 0.20
        elif self.material_typr == 78:
            self.rfactor = 0.37
        elif self.material_typr == 79:
            self.rfactor = 1.64
        elif self.material_typr == 80:
            self.rfactor = 1.03
        elif self.material_typr == 81:
            self.rfactor = 0.78
        elif self.material_typr == 82:
            self.rfactor = 0.22
        elif self.material_typr == 83:
            self.rfactor = 0.32
        else:
            self.rfactor = 45
        return self.rfactor

    def R_factor(self):
        self.material_typr = self.comboBox_7.currentIndex()
        if self.material_typr == 0:
            self.rfactor = 0
        elif self.material_typr == 1:
            self.rfactor = 0
        elif self.material_typr == 2:
            self.rfactor = 0
        elif self.material_typr == 3:
            self.rfactor = 0
        elif self.material_typr == 4:
            self.rfactor = 0
        elif self.material_typr == 5:
            self.rfactor = 0
        elif self.material_typr == 6:
            self.rfactor = 0
        elif self.material_typr == 7:
            self.rfactor = 0
        elif self.material_typr == 8:
            self.rfactor = 0
        elif self.material_typr == 9:
            self.rfactor = 0.14
        elif self.material_typr == 10:
            self.rfactor = 0.20
        elif self.material_typr == 11:
            self.rfactor = 0.27
        elif self.material_typr == 12:
            self.rfactor = 0.33
        elif self.material_typr == 13:
            self.rfactor = 0.39
        elif self.material_typr == 14:
            self.rfactor = 0.44
        elif self.material_typr == 15:
            self.rfactor = 0
        elif self.material_typr == 16:
            self.rfactor = 0
        elif self.material_typr == 17:
            self.rfactor = 0.37
        elif self.material_typr == 18:
            self.rfactor = 0.65
        elif self.material_typr == 19:
            self.rfactor = 0.17
        elif self.material_typr == 20:
            self.rfactor = 0.35
        elif self.material_typr == 21:
            self.rfactor = 0.24
        elif self.material_typr == 22:
            self.rfactor = 0.217
        elif self.material_typr == 23:
            self.rfactor = 0.22
        elif self.material_typr == 24:
            self.rfactor = 0.41
        elif self.material_typr == 25:
            self.rfactor = 0.58
        elif self.material_typr == 26:
            self.rfactor = 0.56
        elif self.material_typr == 27:
            self.rfactor = 0.47
        elif self.material_typr == 28:
            self.rfactor = 0.29
        elif self.material_typr == 29:
            self.rfactor = 0.74
        elif self.material_typr == 30:
            self.rfactor = 0.53
        elif self.material_typr == 31:
            self.rfactor = 0.33
        elif self.material_typr == 32:
            self.rfactor = 0.77
        elif self.material_typr == 33:
            self.rfactor = 0.69
        elif self.material_typr == 34:
            self.rfactor = 0.85
        elif self.material_typr == 35:
            self.rfactor = 0.79
        elif self.material_typr == 36:
            self.rfactor = 0.62
        elif self.material_typr == 37:
            self.rfactor = 0.40
        elif self.material_typr == 38:
            self.rfactor = 1.1
        elif self.material_typr == 39:
            self.rfactor = 1
        elif self.material_typr == 40:
            self.rfactor = 0
        elif self.material_typr == 41:
            self.rfactor = 0
        elif self.material_typr == 42:
            self.rfactor = 0
        elif self.material_typr == 43:
            self.rfactor = 0
        elif self.material_typr == 44:
            self.rfactor = 0
        elif self.material_typr == 45:
            self.rfactor = 0
        elif self.material_typr == 46:
            self.rfactor = 0
        elif self.material_typr == 47:
            self.rfactor = 0
        elif self.material_typr == 48:
            self.rfactor = 0
        elif self.material_typr == 49:
            self.rfactor = 0.222
        elif self.material_typr == 50:
            self.rfactor = 0.238
        elif self.material_typr == 51:
            self.rfactor = 0.294
        elif self.material_typr == 52:
            self.rfactor = 0
        elif self.material_typr == 53:
            self.rfactor = 0
        elif self.material_typr == 54:
            self.rfactor = 0
        elif self.material_typr == 55:
            self.rfactor = 0
        elif self.material_typr == 56:
            self.rfactor = 0
        elif self.material_typr == 57:
            self.rfactor = 0
        elif self.material_typr == 58:
            self.rfactor = 0
        elif self.material_typr == 59:
            self.rfactor = 0
        elif self.material_typr == 60:
            self.rfactor = 0
        elif self.material_typr == 61:
            self.rfactor = 0
        elif self.material_typr == 62:
            self.rfactor = 0
        elif self.material_typr == 63:
            self.rfactor = 0
        elif self.material_typr == 64:
            self.rfactor = 0
        elif self.material_typr == 65:
            self.rfactor = 0
        elif self.material_typr == 66:
            self.rfactor = 0
        elif self.material_typr == 67:
            self.rfactor = 0
        elif self.material_typr == 68:
            self.rfactor = 0
        elif self.material_typr == 69:
            self.rfactor = 0
        elif self.material_typr == 70:
            self.rfactor = 0
        elif self.material_typr == 71:
            self.rfactor = 0
        elif self.material_typr == 72:
            self.rfactor = 0
        elif self.material_typr == 73:
            self.rfactor = 0
        elif self.material_typr == 74:
            self.rfactor = 0
        elif self.material_typr == 75:
            self.rfactor = 0
        elif self.material_typr == 76:
            self.rfactor = 0
        elif self.material_typr == 77:
            self.rfactor = 0
        elif self.material_typr == 78:
            self.rfactor = 0
        elif self.material_typr == 79:
            self.rfactor = 0
        elif self.material_typr == 80:
            self.rfactor = 0
        elif self.material_typr == 81:
            self.rfactor = 0
        elif self.material_typr == 82:
            self.rfactor = 0
        elif self.material_typr == 83:
            self.rfactor = 0
        else:
            self.rfactor = 0
        return self.rfactor

    def reset_masonry_material(self):
        return self.comboBox_7.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add New Building/Insulation Material"))
        self.label_10.setText(_translate("Dialog", "Masonry Materials Type :"))
        self.pushButton_9.setText(_translate("Dialog", "Clear"))
        self.pushButton_10.setText(_translate("Dialog", "Save"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "Brick, fired clay (2400 kg/m3)"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "Brick, fired clay (2240 kg/m3)"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "Brick, fired clay (2080 kg/m3)"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "Brick, fired clay (1920 kg/m3)"))
        self.comboBox_7.setItemText(4, _translate("Dialog", "Brick, fired clay (1760 kg/m3)"))
        self.comboBox_7.setItemText(5, _translate("Dialog", "Brick, fired clay (1600 kg/m3)"))
        self.comboBox_7.setItemText(6, _translate("Dialog", "Brick, fired clay (1440 kg/m3)"))
        self.comboBox_7.setItemText(7, _translate("Dialog", "Brick, fired clay (1280 kg/m3)"))
        self.comboBox_7.setItemText(8, _translate("Dialog", "Brick, fired clay (1120 kg/m3)"))
        self.comboBox_7.setItemText(9, _translate("Dialog", "Clay tile, hollow 1 cell deep 75 mm"))
        self.comboBox_7.setItemText(10, _translate("Dialog", "Clay tile, hollow 1 cell deep 100 mm"))
        self.comboBox_7.setItemText(11, _translate("Dialog", "Clay tile, hollow 2 cell deep 150 mm"))
        self.comboBox_7.setItemText(12, _translate("Dialog", "Clay tile, hollow 2 cell deep 200 mm"))
        self.comboBox_7.setItemText(13, _translate("Dialog", "Clay tile, hollow 2 cell deep 250 mm"))
        self.comboBox_7.setItemText(14, _translate("Dialog", "Clay tile, hollow 3 cell deep 300 mm"))
        self.comboBox_7.setItemText(15, _translate("Dialog", "Lightweight brick (800 kg/m3) "))
        self.comboBox_7.setItemText(16, _translate("Dialog", "Lightweight brick (770 kg/m3)"))
        self.comboBox_7.setItemText(17, _translate("Dialog", "Concrete blocks Limestone aggregate ~200 mm, 16.3 kg, 2200 kg/m3 concrete, 2 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(18, _translate("Dialog", "Concrete blocks Limestone aggregate ~300 mm, 25 kg, 2200 kg/m3 concrete, 2 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(19, _translate("Dialog", "Concrete blocks Normal-weight aggregate (sand and gravel) ~200 mm, 16 kg, 2100 kg/m3 concrete, 2 or 3 cores"))
        self.comboBox_7.setItemText(20, _translate("Dialog", "Concrete blocks Normal-weight aggregate (sand and gravel) ~200 mm, 16 kg, 2100 kg/m3 concrete, 2 or 3 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(21, _translate("Dialog", "Concrete blocks Normal-weight aggregate (sand and gravel) ~200 mm, 16 kg, 2100 kg/m3 concrete, 2 or 3 cores with vermiculite-filled cores"))
        self.comboBox_7.setItemText(22, _translate("Dialog", "Concrete blocks Normal-weight aggregate (sand and gravel) ~300 mm, 22.7 kg, 2000 kg/m3 concrete, 2 cores"))
        self.comboBox_7.setItemText(23, _translate("Dialog", "Concrete blocks Medium-weight aggregate (combinations of normal and lightweight aggregate) ~200 mm, 13 kg, 1550 to 1800 kg/m3 concrete, 2 or 3 cores"))
        self.comboBox_7.setItemText(24, _translate("Dialog", "Concrete blocks Medium-weight aggregate (combinations of normal and lightweight aggregate)~200 mm, 13 kg, 1550 to 1800 kg/m3 concrete, 2 or 3 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(25, _translate("Dialog", "Concrete blocks Medium-weight aggregate (combinations of normal and lightweight aggregate)~200 mm, 13 kg, 1550 to 1800 kg/m3 concrete, 2 or 3 coreswith with vermiculite-filled cores"))
        self.comboBox_7.setItemText(26, _translate("Dialog", "Concrete blocks Medium-weight aggregate (combinations of normal and lightweight aggregate)~200 mm, 13 kg, 1550 to 1800 kg/m3 concrete, 2 or 3 coreswith with molded-EPS-filled (beads) cores"))
        self.comboBox_7.setItemText(27, _translate("Dialog", "Concrete blocks Medium-weight aggregate (combinations of normal and lightweight aggregate)~200 mm, 13 kg, 1550 to 1800 kg/m3 concrete, 2 or 3 coreswith with molded EPS inserts in cores"))
        self.comboBox_7.setItemText(28, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) ~150 mm, 7 1/2 kg, 1400 kg/m2 concrete, 2 or 3 cores"))
        self.comboBox_7.setItemText(29, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) ~150 mm, 7 1/2 kg, 1400 kg/m2 concrete, 2 or 3 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(30, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) ~150 mm, 7 1/2 kg, 1400 kg/m2 concrete, 2 or 3 cores with vermiculite-filled cores"))
        self.comboBox_7.setItemText(31, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete"))
        self.comboBox_7.setItemText(32, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete with perlite-filled cores"))
        self.comboBox_7.setItemText(33, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete with vermiculite-filled cores"))
        self.comboBox_7.setItemText(34, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete with molded-EPS-filled (beads) cores"))
        self.comboBox_7.setItemText(35, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete with UF foam-filled cores"))
        self.comboBox_7.setItemText(36, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 200 mm, 8 to 10 kg, 1150 to 1380 kg/m2 concrete with molded EPS inserts in cores"))
        self.comboBox_7.setItemText(37, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 300 mm, 16 kg, 1400 kg/m3, concrete, 2 or 3 cores"))
        self.comboBox_7.setItemText(38, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 300 mm, 16 kg, 1400 kg/m3, concrete, 2 or 3 cores with perlite-filled cores"))
        self.comboBox_7.setItemText(39, _translate("Dialog", "Concrete blocks Low-mass aggregate (expanded shale, clay, slate or slag, pumice) 300 mm, 16 kg, 1400 kg/m3, concrete, 2 or 3 cores with vermiculite-filled cores"))
        self.comboBox_7.setItemText(40, _translate("Dialog", "Concrete blocks Stone, lime, or sand (2880 kg/m3)"))
        self.comboBox_7.setItemText(41, _translate("Dialog", "Concrete blocks Quartzitic and sandstone (2560 kg/m3)"))
        self.comboBox_7.setItemText(42, _translate("Dialog", "Concrete blocks Quartzitic and sandstone (2240 kg/m3)"))
        self.comboBox_7.setItemText(43, _translate("Dialog", "Concrete blocksQuartzitic and sandstone (1920 kg/m3)"))
        self.comboBox_7.setItemText(44, _translate("Dialog", "Concrete blocks Calcitic, dolomitic, limestone, marble, and granite (2880 kg/m3)"))
        self.comboBox_7.setItemText(45, _translate("Dialog", "Concrete blocks Calcitic, dolomitic, limestone, marble, and granite (2560 kg/m3)"))
        self.comboBox_7.setItemText(46, _translate("Dialog", "Concrete blocks Calcitic, dolomitic, limestone, marble, and granite (2240 kg/m3)"))
        self.comboBox_7.setItemText(47, _translate("Dialog", "Concrete blocks Calcitic, dolomitic, limestone, marble, and granite (1920 kg/m3)"))
        self.comboBox_7.setItemText(48, _translate("Dialog", "Concrete blocks Calcitic, dolomitic, limestone, marble, and granite (1600 kg/m3)"))
        self.comboBox_7.setItemText(49, _translate("Dialog", "Concrete blocks Gypsum partition tile 75 by 300 by 760 mm, solid"))
        self.comboBox_7.setItemText(50, _translate("Dialog", "Concrete blocks Gypsum partition tile 4 cells "))
        self.comboBox_7.setItemText(51, _translate("Dialog", "Concrete blocks Gypsum partition tile 100 by 300 by 760 mm, 3 cells"))
        self.comboBox_7.setItemText(52, _translate("Dialog", "Concrete blocks Limestone (2400 kg/m3)"))
        self.comboBox_7.setItemText(53, _translate("Dialog", "Concrete blocks Limestone (2600 kg/m3)"))
        self.comboBox_7.setItemText(54, _translate("Dialog", "Concrete, Sand and gravel or stone aggregate concretes (2400 kg/m3)"))
        self.comboBox_7.setItemText(55, _translate("Dialog", "Concrete, Sand and gravel or stone aggregate concretes (2240 kg/m3)"))
        self.comboBox_7.setItemText(56, _translate("Dialog", "Concrete, Sand and gravel or stone aggregate concretes (2080 kg/m3)"))
        self.comboBox_7.setItemText(57, _translate("Dialog", "Concrete,Low-mass aggregate or limestone concretes (1920 kg/m3)"))
        self.comboBox_7.setItemText(58, _translate("Dialog", "Concrete,Low-mass aggregate or limestone concretes (1600 kg/m3)"))
        self.comboBox_7.setItemText(59, _translate("Dialog", "Concrete,Low-mass aggregate or limestone concretes (1280 kg/m3)"))
        self.comboBox_7.setItemText(60, _translate("Dialog", "Concrete,Low-mass aggregate or limestone concretes (960 kg/m3)"))
        self.comboBox_7.setItemText(61, _translate("Dialog", "Concrete,Low-mass aggregate or limestone concretes (640 kg/m3)"))
        self.comboBox_7.setItemText(62, _translate("Dialog", "Concrete,Gypsum/fiber concrete (87.5% gypsum, 12.5% wood chips) (800 kg/m3)"))
        self.comboBox_7.setItemText(63, _translate("Dialog", "Concrete,Cement/lime, mortar, and stucco (1920 kg/m3)"))
        self.comboBox_7.setItemText(64, _translate("Dialog", "Concrete,Cement/lime, mortar, and stucco (1600 kg/m3)"))
        self.comboBox_7.setItemText(65, _translate("Dialog", "Concrete,Cement/lime, mortar, and stucco (1280 kg/m3)"))
        self.comboBox_7.setItemText(66, _translate("Dialog", "Concretes, Perlite, vermiculite, and polystyrene beads (800 kg/m3)"))
        self.comboBox_7.setItemText(67, _translate("Dialog", "Concretes, Perlite, vermiculite, and polystyrene beads (640 kg/m3)"))
        self.comboBox_7.setItemText(68, _translate("Dialog", "Concretes, Perlite, vermiculite, and polystyrene beads (480 kg/m3)"))
        self.comboBox_7.setItemText(69, _translate("Dialog", "Concretes, Perlite, vermiculite, and polystyrene beads (320 kg/m3)"))
        self.comboBox_7.setItemText(70, _translate("Dialog", "Concretes, Foam concretes (1920 kg/m3)"))
        self.comboBox_7.setItemText(71, _translate("Dialog", "Concretes, Foam concretes (1600 kg/m3)"))
        self.comboBox_7.setItemText(72, _translate("Dialog", "Concretes, Foam concretes (1280 kg/m3)"))
        self.comboBox_7.setItemText(73, _translate("Dialog", "Concretes, Foam concretes (1120 kg/m3)"))
        self.comboBox_7.setItemText(74, _translate("Dialog", "Concretes, Foam concretes and cellular concretes (960 kg/m3)"))
        self.comboBox_7.setItemText(75, _translate("Dialog", "Concretes, Foam concretes and cellular concretes (640 kg/m3)"))
        self.comboBox_7.setItemText(76, _translate("Dialog", "Concretes, Foam concretes and cellular concretes (320 kg/m3)"))
        self.comboBox_7.setItemText(77, _translate("Dialog", "Concretes, Aerated concrete (oven-dried) (430-800 kg/m3)"))
        self.comboBox_7.setItemText(78, _translate("Dialog", "Concretes, Polystyrene concrete (oven-dried) (255-800 kg/m3)"))
        self.comboBox_7.setItemText(79, _translate("Dialog", "Concretes, Polymer concrete (1950 kg/m3)"))
        self.comboBox_7.setItemText(80, _translate("Dialog", "Concretes, Polymer concrete (2200 kg/m3)"))
        self.comboBox_7.setItemText(81, _translate("Dialog", "Concretes, Polymer cement (1870 kg/m3)"))
        self.comboBox_7.setItemText(82, _translate("Dialog", "Concretes, Slag concrete (960 kg/m3)"))
        self.comboBox_7.setItemText(83, _translate("Dialog", "Concretes, Slag concrete (1280 kg/m3)"))
        self.comboBox_7.setItemText(84, _translate("Dialog", "Steel"))
        self.comboBox_7.setItemText(85, _translate("Dialog", "Other"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
