from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout


class ResolutionOption(QWidget):
    def __init__(self, parent=None):
        super(ResolutionOption, self).__init__(parent)
        
        font = QtGui.QFont()
        font.setPointSize(10)
        #Image holder
        self.imageHolder = QtWidgets.QLabel(self)
        self.imageHolder.setGeometry(QtCore.QRect(20, 50, 150, 150))
        self.imageHolder.setObjectName("imageHolder")
        pixmap = QtGui.QPixmap(".\\icon\\image.png")
        self.imageHolder.setPixmap(pixmap)
        self.imageHolder.setScaledContents(True)

        #Option Widget
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(320, 80, 421, 31))
        self.comboBox.setObjectName("comboBox")

        self.resLabel = QtWidgets.QLabel(self)
        self.resLabel.setGeometry(QtCore.QRect(320, 40, 271, 31))
        self.resLabel.setText("Chọn độ phân giải muốn tải")
        self.resLabel.setFont(font)
        self.resLabel.setObjectName("resLabel")
        self.resLabel.setMaximumHeight(20)

        self.downloadBtn = QtWidgets.QPushButton(self)
        self.downloadBtn.setGeometry(QtCore.QRect(320, 120, 111, 31))
        self.downloadBtn.setText("Download")
        self.downloadBtn.setFont(font)
        self.downloadBtn.setObjectName("pushButton")

        #Add all widget to layout
        self.option_container = QtWidgets.QWidget()
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.resLabel, 0, 0)
        gridLayout.addWidget(self.comboBox, 1, 0)
        gridLayout.addWidget(self.downloadBtn, 2, 0)
        gridLayout.addWidget(QtWidgets.QLabel(""), 3, 0)
        gridLayout.setColumnStretch(0,1)
        gridLayout.setRowStretch(0, 0)
        gridLayout.setRowStretch(1, 0)
        gridLayout.setRowStretch(2, 0)
        self.option_container.setLayout(gridLayout)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.imageHolder, 0, 0)
        mainLayout.addWidget(self.option_container, 0, 1)
        # mainLayout.addLayout(rightLayout)

        self.setLayout(mainLayout)

    def setUpComboBox(self, option_list):
        self.option_list = []

    def getResOption(self):
        return
