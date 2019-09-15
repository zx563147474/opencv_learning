# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setEnabled(True)
        self.labelCamera.setGeometry(QtCore.QRect(30, 30, 150, 150))
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setEnabled(True)
        self.labelCapture.setGeometry(QtCore.QRect(280, 30, 150, 150))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setEnabled(True)
        self.labelResult.setGeometry(QtCore.QRect(530, 30, 150, 150))
        self.labelResult.setObjectName("labelResult")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 440, 541, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpenCamera = QtWidgets.QPushButton(self.layoutWidget)
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.horizontalLayout.addWidget(self.btnOpenCamera)
        self.btnCapture = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCapture.setObjectName("btnCapture")
        self.horizontalLayout.addWidget(self.btnCapture)
        self.btnReadImage = QtWidgets.QPushButton(self.layoutWidget)
        self.btnReadImage.setObjectName("btnReadImage")
        self.horizontalLayout.addWidget(self.btnReadImage)
        self.btnGray = QtWidgets.QPushButton(self.layoutWidget)
        self.btnGray.setObjectName("btnGray")
        self.horizontalLayout.addWidget(self.btnGray)
        self.btnThreshold = QtWidgets.QPushButton(self.layoutWidget)
        self.btnThreshold.setObjectName("btnThreshold")
        self.horizontalLayout.addWidget(self.btnThreshold)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.btnCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.btnReadImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.btnGray.clicked.connect(MainWindow.btnGrayScale_Clicked)
        self.btnThreshold.clicked.connect(MainWindow.btnThreshold_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCamera.setText(_translate("MainWindow", "Camera"))
        self.labelCapture.setText(_translate("MainWindow", "Capture"))
        self.labelResult.setText(_translate("MainWindow", "Result"))
        self.btnOpenCamera.setText(_translate("MainWindow", "Open Camera"))
        self.btnCapture.setText(_translate("MainWindow", "Capture Image"))
        self.btnReadImage.setText(_translate("MainWindow", "Open Image"))
        self.btnGray.setText(_translate("MainWindow", "Gray Scale"))
        self.btnThreshold.setText(_translate("MainWindow", "Otsu"))
