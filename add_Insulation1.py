

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
        self.comboBox_2.setGeometry(QtCore.QRect(260, 110, 571, 24))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def R_factor(self):
        self.material_typr = self.comboBox_2.currentIndex()
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
            self.rfactor = 0.011
        elif self.material_typr == 8:
            self.rfactor = 0.012
        elif self.material_typr == 9:
            self.rfactor = 0.014
        elif self.material_typr == 10:
            self.rfactor = 0.015
        elif self.material_typr == 11:
            self.rfactor = 0.019
        elif self.material_typr == 12:
            self.rfactor = 0.011
        elif self.material_typr == 13:
            self.rfactor = 0.023
        elif self.material_typr == 14:
            self.rfactor = 0.019
        elif self.material_typr == 15:
            self.rfactor = 0.019
        elif self.material_typr == 16:
            self.rfactor = 0.017
        elif self.material_typr == 17:
            self.rfactor = 0.24
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
            self.rfactor = 1.22
        elif self.material_typr == 28:
            self.rfactor = 0
        elif self.material_typr == 29:
            self.rfactor = 0.037
        elif self.material_typr == 30:
            self.rfactor = 0.015
        elif self.material_typr == 31:
            self.rfactor = 0.021
        elif self.material_typr == 32:
            self.rfactor = 0.025
        elif self.material_typr == 33:
            self.rfactor = 0.037
        elif self.material_typr == 34:
            self.rfactor = 0.026
        elif self.material_typr == 35:
            self.rfactor = 0.26
        elif self.material_typr == 36:
            self.rfactor = 0
        elif self.material_typr == 37:
            self.rfactor = 0.14
        elif self.material_typr == 38:
            self.rfactor = 0.14
        elif self.material_typr == 39:
            self.rfactor = 0.18
        elif self.material_typr == 40:
            self.rfactor = 0.10
        elif self.material_typr == 41:
            self.rfactor = 0.11
        elif self.material_typr == 42:
            self.rfactor = 0.32
        elif self.material_typr == 43:
            self.rfactor = 0.52
        elif self.material_typr == 44:
            self.rfactor = 0.35
        elif self.material_typr == 45:
            self.rfactor = 0.48
        else:
            self.rfactor = 0
        return self.rfactor

    def K_factor(self):
        self.material_typr = self.comboBox_2.currentIndex()
        if self.material_typr == 0:
            self.rfactor = 0.57
        elif self.material_typr == 1:
            self.rfactor = 0.25
        elif self.material_typr == 2:
            self.rfactor = 0.25
        elif self.material_typr == 3:
            self.rfactor = 0.19
        elif self.material_typr == 4:
            self.rfactor = 0.07
        elif self.material_typr == 5:
            self.rfactor = 0.06
        elif self.material_typr == 6:
            self.rfactor = 0.16
        elif self.material_typr == 7:
            self.rfactor = 0
        elif self.material_typr == 8:
            self.rfactor = 0
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
            self.rfactor = 0
        elif self.material_typr == 16:
            self.rfactor = 0
        elif self.material_typr == 17:
            self.rfactor = 0
        elif self.material_typr == 18:
            self.rfactor = 0.058
        elif self.material_typr == 19:
            self.rfactor = 0.075
        elif self.material_typr == 20:
            self.rfactor = 0.072
        elif self.material_typr == 21:
            self.rfactor = 0.105
        elif self.material_typr == 22:
            self.rfactor = 0.12
        elif self.material_typr == 23:
            self.rfactor = 0.144
        elif self.material_typr == 24:
            self.rfactor = 0.102
        elif self.material_typr == 25:
            self.rfactor = 0.135
        elif self.material_typr == 26:
            self.rfactor = 1.18
        elif self.material_typr == 27:
            self.rfactor = 0
        elif self.material_typr == 28:
            self.rfactor = 0.072
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
            self.rfactor = 0.072
        elif self.material_typr == 37:
            self.rfactor = 0
        elif self.material_typr == 38:
            self.rfactor = 0
        elif self.material_typr == 39:
            self.rfactor = 0
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
        else:
            self.rfactor = 1
        return self.rfactor

    def reset_board_material(self):
        return self.comboBox_2.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add New Building/Insulation Material"))
        self.label.setText(_translate("Dialog", "Building Board and Siding Material Type :"))
        self.pushButton_9.setText(_translate("Dialog", "Clear"))
        self.pushButton_10.setText(_translate("Dialog", "Save"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Board Asbestos/cement board (1900 kg/m3)"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Board cement board (1150 kg/m3)"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Board Fiber/cement board (1400 kg/m3)"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Board Fiber/cement board (1000 kg/m3)"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Board Fiber/cement board (400 kg/m3)"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Board Fiber/cement board (300 kg/m3)"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "Gypsum or plaster board (640 kg/m3)"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Oriented strand board (OSB) 9 to 11 mm  (650 kg/m3) "))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Oriented strand board (OSB) 12.7 mm  (650 kg/m3) "))
        self.comboBox_2.setItemText(9, _translate("Dialog", "Plywood (douglas fir) 12.7 mm  (460 kg/m3)"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "Plywood (douglas fir) 15.9 mm  (540 kg/m3)"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Plywood/wood panels 19 mm  (450 kg/m3)"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "Vegetable fiber board (650 kg/m3)"))
        self.comboBox_2.setItemText(13, _translate("Dialog", "Vegetable fiber board sheathing, regular density  12.7 mm (290 kg/m3)"))
        self.comboBox_2.setItemText(14, _translate("Dialog", "Vegetable fiber board sheathing, regular density intermediate density  12.7 mm (350 kg/m3)"))
        self.comboBox_2.setItemText(15, _translate("Dialog", "Vegetable fiber board nail-based sheathing 12.7 mm (400 kg/m3)"))
        self.comboBox_2.setItemText(16, _translate("Dialog", "Vegetable fiber board shingle backer 9.5 mm (290 kg/m3)"))
        self.comboBox_2.setItemText(17, _translate("Dialog", "Vegetable fiber board sound deadening board 12.7 mm (240 kg/m3)"))
        self.comboBox_2.setItemText(18, _translate("Dialog", "Vegetable fiber board tile and lay-in panels, plain or acoustic (290 kg/m3)"))
        self.comboBox_2.setItemText(19, _translate("Dialog", "Vegetable fiber board laminated paperboard (480 kg/m3)"))
        self.comboBox_2.setItemText(20, _translate("Dialog", "Vegetable fiber board homogeneous board from repulped paper (480 kg/m3)"))
        self.comboBox_2.setItemText(21, _translate("Dialog", "Hardboard medium density (800 kg/m3)"))
        self.comboBox_2.setItemText(22, _translate("Dialog", "Hardboard high density, service-tempered grade and service grade (880 kg/m3)"))
        self.comboBox_2.setItemText(23, _translate("Dialog", "Hardboard high density, standard-tempered grade (1010 kg/m3)"))
        self.comboBox_2.setItemText(24, _translate("Dialog", "Particleboard low density (590 kg/m3)"))
        self.comboBox_2.setItemText(25, _translate("Dialog", "Particleboard medium density (800 kg/m3)"))
        self.comboBox_2.setItemText(26, _translate("Dialog", "Particleboard high density (1000 kg/m3)"))
        self.comboBox_2.setItemText(27, _translate("Dialog", "Particleboard underlayment 15.9 mm (640 kg/m3)"))
        self.comboBox_2.setItemText(28, _translate("Dialog", "Waferboard (700 kg/m3)"))
        self.comboBox_2.setItemText(29, _translate("Dialog", "Shingles Asbestos/cement (1900 kg/m3)"))
        self.comboBox_2.setItemText(30, _translate("Dialog", "Shingles Wood, 400 mm, 190 mm exposure"))
        self.comboBox_2.setItemText(31, _translate("Dialog", "Shingles Wood, double, 400 mm, 300 mm exposure"))
        self.comboBox_2.setItemText(32, _translate("Dialog", "Shingles Wood, plus ins. backer board 8 mm"))
        self.comboBox_2.setItemText(33, _translate("Dialog", "Shingles Asbestos/cement, lapped 6.4 mm"))
        self.comboBox_2.setItemText(34, _translate("Dialog", "Shingles Asphalt roll siding"))
        self.comboBox_2.setItemText(35, _translate("Dialog", "Siding Asphalt insulating siding (12.7 mm bed)"))
        self.comboBox_2.setItemText(36, _translate("Dialog", "Siding Hardboard siding 11 mm"))
        self.comboBox_2.setItemText(37, _translate("Dialog", "Siding Wood, drop, 200 mm 25 mm"))
        self.comboBox_2.setItemText(38, _translate("Dialog", "Siding Wood, bevel 200 mm, lapped 13 mm"))
        self.comboBox_2.setItemText(39, _translate("Dialog", "Siding Wood, bevel 250 mm, lapped 19 mm"))
        self.comboBox_2.setItemText(40, _translate("Dialog", "Siding Wood, plywood, lapped 9.5 mm"))
        self.comboBox_2.setItemText(41, _translate("Dialog", "Siding Aluminum, steel, or vinyl over sheathing hollow-backed"))
        self.comboBox_2.setItemText(42, _translate("Dialog", "Siding Aluminum, steel, or vinyl over sheathing insulating-board-backed 9.5 mm"))
        self.comboBox_2.setItemText(43, _translate("Dialog", "Siding Aluminum, steel, or vinyl over sheathing foil-backed 9.5 mm"))
        self.comboBox_2.setItemText(44, _translate("Dialog", "Siding Aluminum, steel, or vinyl over sheathing insulated vinyl siding 19 mm"))
        self.comboBox_2.setItemText(45, _translate("Dialog", "Siding Aluminum, steel, or vinyl over sheathing insulated vinyl siding 32 mm"))
        self.comboBox_2.setItemText(46, _translate("Dialog", "Siding Architectural (soda-lime float) glass (2500 kg/m3)"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
