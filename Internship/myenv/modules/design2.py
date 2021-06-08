# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 15:53:59 2019

@author: elh
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(74, 130, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(255, 19, 491, 231))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 230, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(60, 330, 113, 20))
        self.addBtn.setObjectName("addBtn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(64, 360, 111, 23))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectImageBtn.clicked.connect(self.setImage)
        self.addBtn.clicked.connect(self.addItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImageBtn.setText(_translate("MainWindow", "Select Image"))
        self.addBtn.setText(_translate("MainWindow", "Add"))

    def setImage(self,event):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a file
          
            self.image = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            #pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.image= self.image.scaled(1000,800)
            self.imageLbl.setScaledContents(True)
            self.imageLbl.setPixmap(self.image) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
            self.resize(self.image.width(), self.image.height())
            self.largest_rect = QRect(10, 10, self.image.width(), self.image.height())
            
            self.clip_rect = QRect(10, 10, self.image.width(), self.image.height())
            self.dragging = None
            self.drag_offset = QPoint()
            self.handle_offsets = (
                QPoint(8, 8), QPoint(-1, 8), QPoint(8, -1), QPoint(-1, -1)
                )
            self.show()
            self.resize(800, 600)
            
            
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.drawPixmap(QRect(10, 10, self.image.width(), self.image.height()),  self.image)
        #painter.fillRect(event.largest_rect, QBrush(Qt.white))
        #painter.setRenderHint(QPainter.Antialiasing)
       # painter.setPen(QPen(QBrush(Qt.red), 1, Qt.DashLine))
        #painter.drawRect(self.largest_rect)
        #painter.setPen(QPen(Qt.black))
        painter.drawRect(self.clip_rect)
        for i in range(4):
            painter.drawRect(self.corner(i))
        
        painter.setClipRect(self.clip_rect)
        #painter.drawPolyline(self.polygon)
        #painter.setBrush(QBrush(Qt.blue))
        #painter.drawPath(self.path)
        painter.end()
    
    def corner(self, number):
    
        if number == 0:
            return QRect(self.clip_rect.topLeft() - self.handle_offsets[0], QSize(8, 8))
        elif number == 1:
            return QRect(self.clip_rect.topRight() - self.handle_offsets[1], QSize(8, 8))
        elif number == 2:
            return QRect(self.clip_rect.bottomLeft() - self.handle_offsets[2], QSize(8, 8))
        elif number == 3:
            return QRect(self.clip_rect.bottomRight() - self.handle_offsets[3], QSize(8, 8))
    
    def mousePressEvent(self, event):
    
        for i in range(4):
            rect = self.corner(i)
            if rect.contains(event.pos()):
                self.dragging = i
                self.drag_offset = rect.topLeft() - event.pos()
                break
        else:
            self.dragging = None
    
    def mouseMoveEvent(self, event):
    
        if self.dragging is None:
            return
        
        left = self.largest_rect.left()
        right = self.largest_rect.right()
        top = self.largest_rect.top()
        bottom = self.largest_rect.bottom()
        
        point = event.pos() + self.drag_offset + self.handle_offsets[self.dragging]
        point.setX(max(left, min(point.x(), right)))
        point.setY(max(top, min(point.y(), bottom)))
        
        if self.dragging == 0:
            self.clip_rect.setTopLeft(point)
        elif self.dragging == 1:
            self.clip_rect.setTopRight(point)
        elif self.dragging == 2:
            self.clip_rect.setBottomLeft(point)
        elif self.dragging == 3:
            self.clip_rect.setBottomRight(point)
        
        self.update()
    
    def mouseReleaseEvent(self, event):
    
        self.dragging = None
        currentQRect = self.currentQRubberBand.geometry()
        cropQPixmap =  self.update().copy(currentQRect)
        cropQPixmap.save('output.png')
        
    def addItem(self):
        value = self.lineEdit.text() # Get the value of the lineEdit
        self.lineEdit.clear() # Clear the text
        self.listWidget.addItem(value) # Add the value we got to the list
    
    #def sizeHint(self):
       # return QSize(500, 500)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



