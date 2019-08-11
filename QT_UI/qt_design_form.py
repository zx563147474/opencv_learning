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
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setEnabled(True)
        self.Camera.setGeometry(QtCore.QRect(30, 30, 150, 150))
        self.Camera.setObjectName("Camera")
        self.Capture = QtWidgets.QLabel(self.centralwidget)
        self.Capture.setEnabled(True)
        self.Capture.setGeometry(QtCore.QRect(280, 30, 150, 150))
        self.Capture.setObjectName("Capture")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setEnabled(True)
        self.Result.setGeometry(QtCore.QRect(530, 30, 150, 150))
        self.Result.setObjectName("Result")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 440, 541, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenCamera = QtWidgets.QPushButton(self.widget)
        self.OpenCamera.setObjectName("OpenCamera")
        self.horizontalLayout.addWidget(self.OpenCamera)
        self.CaptureImage = QtWidgets.QPushButton(self.widget)
        self.CaptureImage.setObjectName("CaptureImage")
        self.horizontalLayout.addWidget(self.CaptureImage)
        self.OpenImage = QtWidgets.QPushButton(self.widget)
        self.OpenImage.setObjectName("OpenImage")
        self.horizontalLayout.addWidget(self.OpenImage)
        self.GrayScale = QtWidgets.QPushButton(self.widget)
        self.GrayScale.setObjectName("GrayScale")
        self.horizontalLayout.addWidget(self.GrayScale)
        self.Otsu = QtWidgets.QPushButton(self.widget)
        self.Otsu.setObjectName("Otsu")
        self.horizontalLayout.addWidget(self.Otsu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.OpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.CaptureImage.clicked.connect(MainWindow.btnCapture_Clicked)
        self.OpenImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.GrayScale.clicked.connect(MainWindow.btnGrayScale_Clicked)
        self.Otsu.clicked.connect(MainWindow.btnThreshold_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Camera.setText(_translate("MainWindow", "Camera"))
        self.Capture.setText(_translate("MainWindow", "Capture"))
        self.Result.setText(_translate("MainWindow", "Result"))
        self.OpenCamera.setText(_translate("MainWindow", "Open Camera"))
        self.CaptureImage.setText(_translate("MainWindow", "Capture Image"))
        self.OpenImage.setText(_translate("MainWindow", "Open Image"))
        self.GrayScale.setText(_translate("MainWindow", "Gray Scale"))
        self.Otsu.setText(_translate("MainWindow", "Otsu"))
