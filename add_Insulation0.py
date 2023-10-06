
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
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 110, 661, 24))
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

    def K_factor(self):
        self.material_typr = self.comboBox_2.currentIndex()
        if self.material_typr == 0:
            self.rfactor = 0.046
        elif self.material_typr == 1:
            self.rfactor = 0.048
        elif self.material_typr == 2:
            self.rfactor = 0.040
        elif self.material_typr == 3:
            self.rfactor = 0.043
        elif self.material_typr == 4:
            self.rfactor = 0.037
        elif self.material_typr == 5:
            self.rfactor = 0.039
        elif self.material_typr == 6:
            self.rfactor = 0.033
        elif self.material_typr == 7:
            self.rfactor = 0.036
        elif self.material_typr == 8:
            self.rfactor = 0.037
        elif self.material_typr == 9:
            self.rfactor = 0.035
        elif self.material_typr == 10:
            self.rfactor = 0.040
        elif self.material_typr == 11:
            self.rfactor = 0.035
        elif self.material_typr == 12:
            self.rfactor = 0.042
        elif self.material_typr == 13:
            self.rfactor = 0.072
        elif self.material_typr == 14:
            self.rfactor = 0.076
        elif self.material_typr == 15:
            self.rfactor = 0.082
        elif self.material_typr == 16:
            self.rfactor = 0.033
        elif self.material_typr == 17:
            self.rfactor = 0.035
        elif self.material_typr == 18:
            self.rfactor = 0.029
        elif self.material_typr == 19:
            self.rfactor = 0.026
        elif self.material_typr == 20:
            self.rfactor = 0.029
        elif self.material_typr == 21:
            self.rfactor = 0.029
        elif self.material_typr == 22:
            self.rfactor = 0.030
        elif self.material_typr == 23:
            self.rfactor = 0.030
        elif self.material_typr == 24:
            self.rfactor = 0.036
        elif self.material_typr == 25:
            self.rfactor = 0.035
        elif self.material_typr == 26:
            self.rfactor = 0.037
        elif self.material_typr == 27:
            self.rfactor = 0.033
        elif self.material_typr == 28:
            self.rfactor = 0.037
        elif self.material_typr == 29:
            self.rfactor = 0.033
        elif self.material_typr == 30:
            self.rfactor = 0.037
        elif self.material_typr == 31:
            self.rfactor = 0.033
        elif self.material_typr == 32:
            self.rfactor = 0.036
        elif self.material_typr == 33:
            self.rfactor = 0.039
        elif self.material_typr == 34:
            self.rfactor = 0.042
        elif self.material_typr == 35:
            self.rfactor = 0.052
        elif self.material_typr == 36:
            self.rfactor = 0.053
        elif self.material_typr == 37:
            self.rfactor = 0.052
        elif self.material_typr == 38:
            self.rfactor = 0.023
        elif self.material_typr == 39:
            self.rfactor = 0.025
        elif self.material_typr == 40:
            self.rfactor = 0.023
        elif self.material_typr == 41:
            self.rfactor = 0.023
        elif self.material_typr == 42:
            self.rfactor = 0.045
        elif self.material_typr == 43:
            self.rfactor = 0.046
        elif self.material_typr == 44:
            self.rfactor = 0.039
        elif self.material_typr == 45:
            self.rfactor = 0.040
        elif self.material_typr == 46:
            self.rfactor = 0.040
        elif self.material_typr == 47:
            self.rfactor = 0.039
        elif self.material_typr == 48:
            self.rfactor = 0.045
        elif self.material_typr == 49:
            self.rfactor = 0.052
        elif self.material_typr == 50:
            self.rfactor = 0.061
        elif self.material_typr == 51:
            self.rfactor = 0.052
        elif self.material_typr == 52:
            self.rfactor = 0.055
        elif self.material_typr == 53:
            self.rfactor = 0.049
        elif self.material_typr == 54:
            self.rfactor = 0.052
        elif self.material_typr == 55:
            self.rfactor = 0.035
        elif self.material_typr == 56:
            self.rfactor = 0.036
        elif self.material_typr == 57:
            self.rfactor = 0.049
        elif self.material_typr == 58:
            self.rfactor = 0.046
        elif self.material_typr == 59:
            self.rfactor = 0.048
        elif self.material_typr == 60:
            self.rfactor = 0.042
        elif self.material_typr == 61:
            self.rfactor = 0.068
        elif self.material_typr == 62:
            self.rfactor = 0.063
        elif self.material_typr == 63:
            self.rfactor = 0.039
        elif self.material_typr == 64:
            self.rfactor = 0.040
        elif self.material_typr == 65:
            self.rfactor = 0.042
        elif self.material_typr == 66:
            self.rfactor = 0.033
        elif self.material_typr == 67:
            self.rfactor = 0.037
        elif self.material_typr == 68:
            self.rfactor = 0.037
        elif self.material_typr == 69:
            self.rfactor = 0.042
        elif self.material_typr == 70:
            self.rfactor = 0.020
        else:
            self.rfactor = 0.029

        return self.rfactor

    def reset_insullation_material(self):
        return self.comboBox_2.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add New Building/Insulation Material"))
        self.label.setText(_translate("Dialog", "Insulationg Material :"))
        self.pushButton_9.setText(_translate("Dialog", "Clear"))
        self.pushButton_10.setText(_translate("Dialog", "Save"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Glass-fiber batts  (7.5 kg/m3)"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Glass-fiber batts  (8.2 kg/m3)"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Glass-fiber batts  (9.8 kg/m3)"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Glass-fiber batts  (12 kg/m3)"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Glass-fiber batts  (13 kg/m3)"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Glass-fiber batts  (14 kg/m3)"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "Glass-fiber batts  (22 kg/m3)"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Rock and slag wool batts  (32 kg/m3) "))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Rock and slag wool batts  (37 kg/m3) "))
        self.comboBox_2.setItemText(9, _translate("Dialog", "Rock and slag wool batts  (45 kg/m3)"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "Mineral wool, felted (16-48 kg/m3)"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Mineral wool, felted  (16-130 kg/m3)"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "Cellular glass (120 kg/m3)"))
        self.comboBox_2.setItemText(13, _translate("Dialog", "Cement fiber slabs, shredded wood with Portland cement binder (400 kg/m3)"))
        self.comboBox_2.setItemText(14, _translate("Dialog", "Cement fiber slabs, shredded wood with Portland cement binder (430 kg/m3"))
        self.comboBox_2.setItemText(15, _translate("Dialog", "Cement fiber slabs, shredded wood with Portland cement+magnesia oxysulfide (350 kg/m3"))
        self.comboBox_2.setItemText(16, _translate("Dialog", "Glass fiber board (24 kg/m3)"))
        self.comboBox_2.setItemText(17, _translate("Dialog", "Glass fiber board (96 kg/m3)"))
        self.comboBox_2.setItemText(18, _translate("Dialog", "Expanded rubber (rigid) (64 kg/m3)"))
        self.comboBox_2.setItemText(19, _translate("Dialog", "Extruded polystyrene, smooth skin aged per CAN/ULC Standard S770-2003(22 kg/m3)"))
        self.comboBox_2.setItemText(20, _translate("Dialog", "Extruded polystyrene, smooth skin aged per CAN/ULC Standard S770-2003(58kg/m3)"))
        self.comboBox_2.setItemText(21, _translate("Dialog", "Extruded polystyrene, smooth skinaged aged 180 days (22 kg/m3)"))
        self.comboBox_2.setItemText(22, _translate("Dialog", "Extruded polystyrene, smooth skinaged aged 180 days (58 kg/m3)"))
        self.comboBox_2.setItemText(23, _translate("Dialog", "Extruded polystyrene, smooth skinaged European product(30 kg/m3)"))
        self.comboBox_2.setItemText(24, _translate("Dialog", "Extruded polystyrene, smooth skin aged 5 years at 24°Ct(32 kg/m3)"))
        self.comboBox_2.setItemText(25, _translate("Dialog", "Extruded polystyrene, smooth skin aged 5 years at 24°Ct(35 kg/m3)"))
        self.comboBox_2.setItemText(26, _translate("Dialog", "Extruded polystyrene, smooth skin blown with low global warming potential"))
        self.comboBox_2.setItemText(27, _translate("Dialog", "Expanded polystyrene, molded beads(16 kg/m3)"))
        self.comboBox_2.setItemText(28, _translate("Dialog", "Expanded polystyrene, molded beads(24 kg/m3)"))
        self.comboBox_2.setItemText(29, _translate("Dialog", "Expanded polystyrene, molded beads(29 kg/m3)"))
        self.comboBox_2.setItemText(30, _translate("Dialog", "Mineral fiberboard, wet felted (160 kg/m3)"))
        self.comboBox_2.setItemText(31, _translate("Dialog", "Rock wool board floors and walls (64 kg/m3)"))
        self.comboBox_2.setItemText(32, _translate("Dialog", "Rock wool board floors and walls (130 kg/m3)"))
        self.comboBox_2.setItemText(33, _translate("Dialog", "Rock wool board roofing (160 kg/m3)"))
        self.comboBox_2.setItemText(34, _translate("Dialog", "Rock wool board roofing (180 kg/m3)"))
        self.comboBox_2.setItemText(35, _translate("Dialog", "Acoustical tile (340 kg/m3)"))
        self.comboBox_2.setItemText(36, _translate("Dialog", "Acoustical tile (370 kg/m3)"))
        self.comboBox_2.setItemText(37, _translate("Dialog", "Perlite board (140 kg/m3)"))
        self.comboBox_2.setItemText(38, _translate("Dialog", "Polyisocyanurate unfaced, aged per CAN/ULC Standard S770-2003(26 kg/m3)"))
        self.comboBox_2.setItemText(39, _translate("Dialog", "Polyisocyanurate unfaced, aged per CAN/ULC Standard S770-2003(37 kg/m3)"))
        self.comboBox_2.setItemText(40, _translate("Dialog", "Polyisocyanurate with foil facers, aged 180 days"))
        self.comboBox_2.setItemText(41, _translate("Dialog", "Phenolic foam board with facers, aged"))
        self.comboBox_2.setItemText(42, _translate("Dialog", "Cellulose fiber, loose fill attic application up to 100 mm(16 kg/m3)"))
        self.comboBox_2.setItemText(43, _translate("Dialog", "Cellulose fiber, loose fill attic application up to 100 mm(19 kg/m3)"))
        self.comboBox_2.setItemText(44, _translate("Dialog", "Cellulose fiber, loose fill attic application > 100 mm(19 kg/m3)"))
        self.comboBox_2.setItemText(45, _translate("Dialog", "Cellulose fiber, loose fill attic application > 100 mm(26 kg/m3)"))
        self.comboBox_2.setItemText(46, _translate("Dialog", "Cellulose fiber, loose fill wall application, dense packed(56 kg/m3)"))
        self.comboBox_2.setItemText(47, _translate("Dialog", "Perlite, expanded(32 kg/m3)"))
        self.comboBox_2.setItemText(48, _translate("Dialog", "Perlite, expanded(64 kg/m3)"))
        self.comboBox_2.setItemText(49, _translate("Dialog", "Perlite, expanded(120 kg/m3)"))
        self.comboBox_2.setItemText(50, _translate("Dialog", "Perlite, expanded(180 kg/m3)"))
        self.comboBox_2.setItemText(51, _translate("Dialog", "Glass fiber attics, ~100 to 600 mm(6.4 kg/m3)"))
        self.comboBox_2.setItemText(52, _translate("Dialog", "Glass fiber attics, ~100 to 600 mm(8 kg/m3)"))
        self.comboBox_2.setItemText(53, _translate("Dialog", "Glass fiber attics, ~600 to 1100 mm(8 kg/m3)"))
        self.comboBox_2.setItemText(54, _translate("Dialog", "Glass fiber attics, ~600 to 1100 mm(9.6 kg/m3)"))
        self.comboBox_2.setItemText(55, _translate("Dialog", "Glass fiber closed attic or wall cavities(29 kg/m3)"))
        self.comboBox_2.setItemText(56, _translate("Dialog", "Glass fiber closed attic or wall cavities(37 kg/m3)"))
        self.comboBox_2.setItemText(57, _translate("Dialog", "Rock and slag wool attics, ~90 to 115 mm (24-26 kg/m3)"))
        self.comboBox_2.setItemText(58, _translate("Dialog", "Rock and slag wool attics, ~125 to 430 mm (24 kg/m3)"))
        self.comboBox_2.setItemText(59, _translate("Dialog", "Rock and slag wool attics, ~125 to 430 mm (29 kg/m3)"))
        self.comboBox_2.setItemText(60, _translate("Dialog", "Rock and slag wool closed attic or wall cavities (64 kg/m3)"))
        self.comboBox_2.setItemText(61, _translate("Dialog", "Vermiculite, exfoliated(112-131 kg/m3)"))
        self.comboBox_2.setItemText(62, _translate("Dialog", "Vermiculite, exfoliated(64-96 kg/m3)"))
        self.comboBox_2.setItemText(63, _translate("Dialog", "Cellulose, sprayed into open wall cavities(26 kg/m3)"))
        self.comboBox_2.setItemText(64, _translate("Dialog", "Cellulose, sprayed into open wall cavities(42 kg/m3)"))
        self.comboBox_2.setItemText(65, _translate("Dialog", "Glass fiber, sprayed into open wall or attic cavities(16 kg/m3)"))
        self.comboBox_2.setItemText(66, _translate("Dialog", "Glass fiber, sprayed into open wall or attic cavities(29 kg/m3)"))
        self.comboBox_2.setItemText(67, _translate("Dialog", "Glass fiber, sprayed into open wall or attic cavities(37 kg/m3)"))
        self.comboBox_2.setItemText(68, _translate("Dialog", "Polyurethane foam low density, open cell (7.2 kg/m3)"))
        self.comboBox_2.setItemText(69, _translate("Dialog", "Polyurethane foam low density, open cell (10 kg/m3)"))
        self.comboBox_2.setItemText(70, _translate("Dialog", "Polyurethane foam medium density, closed cell, aged 180 days (30 kg/m3)"))
        self.comboBox_2.setItemText(71, _translate("Dialog", "Polyurethane foam medium density, closed cell, aged 180 days (51 kg/m3)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
