import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from mainForm import Ui_MainWindow
class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camera = cv2.VideoCapture(0)
        self.is_camera_opened = False
        # capture image every 30 ms
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)
    def btnOpenCamera_Clicked(self):
        '''
        turn on/off camera
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnOpenCamera.setText("Turn off camera")
            self._timer.start()
        else:
            self.btnOpenCamera.setText("Turn on camera")
            self._timer.stop()
    def btnCapture_Clicked(self):
        '''
        capture image
        '''
        # do nothing if camera is off
        if not self.is_camera_opened:
            return
        self.captured = self.frame

        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # transform image to QImgage
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnReadImage_Clicked(self):

        # open dialog
        filename,  _ = QFileDialog.getOpenFileName(self, 'open image')
        if filename:
            self.captured = cv2.imread(str(filename))
            # transform BGR to RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)
            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnGrayScale_Clicked(self):
        '''
        灰度化
        '''
        # no action if no captured image
        if not hasattr(self, "captured"):
            return
        self.cpatured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)
        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # Format_Indexed8 for grayscale
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnThreshold_Clicked(self):
        '''
        Otsu
        '''
        if not hasattr(self, "captured"):
            return
        _, self.cpatured = cv2.threshold(
            self.cpatured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # Format_Indexed8 for otsu
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        capture image in loop
        '''
        ret, self.frame = self.camera.read()
        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())