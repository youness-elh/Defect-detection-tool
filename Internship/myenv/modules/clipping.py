# -*- coding: utf-8 -*-
"""
Created on Fri Jul 05 19:12:56 2019

@author: elh
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Window(QWidget):

    def __init__(self):
    
        QWidget.__init__(self)
        self.image = QPixmap("image.png")
        #self.setGeometry(10, 10, 1000, 1000)
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
        
        #self.path = QPainterPath()
        #self.path.moveTo(100, 250)
       # font = QFont()
        #font.setPixelSize(80)
       # self.path.addText(100, 300, font, "Clipping")
        
        #self.polygon = QPolygon([QPoint(250, 100), QPoint(400, 250),
                                 #QPoint(250, 400), QPoint(100, 250),
                                 #QPoint(250, 100)])
    
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
    
    #def sizeHint(self):
       # return QSize(500, 500)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
