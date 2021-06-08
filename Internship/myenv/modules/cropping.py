# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 15:29:28 2019

@author: elh
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog,QApplication
import sys



class QExampleLabel (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI (self):
        self.setPixmap = QPixmap('image.png')

    def mousePressEvent (self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent (self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent (self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        cropQPixmap.save('output.png')

if __name__ == '__main__':

    myQApplication = QApplication(sys.argv)
    myQExampleLabel = QExampleLabel()
    myQExampleLabel.show()
    sys.exit(myQApplication.exec_())