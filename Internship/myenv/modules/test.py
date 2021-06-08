# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:45:47 2019

@author: elh
"""


import numpy as np
import cv2, sys, math, re
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageCrop(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setupUi(self)
        self.pushButton_1.clicked.connect(self.show_button)
        self.pushButton_2.clicked.connect(self.crop_button)

    def show_button(self):
        image = QImage("myImage.jpg")
        image = image.convertToFormat(QImage.Format_ARGB8565_Premultiplied)
        pixmap = QPixmap(image)
        w = int(self.label_1.width() - 4.0)
        h = int(self.label_1.height() - 4.0)
        smaller_pixmap = pixmap.scaled(w, h, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label_1.setPixmap(smaller_pixmap)
        self.label_1.setScaledContents(True)

    def crop_button(self):
        self.label_1.clear()
        img = cv2.imread("myImage.jpg",
                         cv2.IMREAD_GRAYSCALE)

        string_percent = self.lineEdit_1.text()
        string_percent = re.sub("\D", "", string_percent)
        percent = float(string_percent)

        image = crop_img(img, percent)
        image = np.asarray(image).copy()
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_Grayscale8)
        pixmap = QPixmap(qimage)
        w = int(self.label_1.width() - 4.0)
        h = int(self.label_1.height() - 4.0)
        smaller_pixmap = pixmap.scaled(w, h, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label_1.setPixmap(smaller_pixmap)
        self.label_1.setScaledContents(True)


def crop_img(img, percent):
    x1, y1 = 0, 0
    x2, y2 = img.shape[1], img.shape[0]
    w, h = x2 - x1, y2 - y1   
    w_curr, h_curr = int(w * math.sqrt(percent * 0.01)), int(h * math.sqrt(percent * 0.01))
    kx, ky = (w - w_curr) * 0.5, (h - h_curr) * 0.5
    x3, y3 = int(x1 + kx), int(y1 + ky)    
    img_cropped = img[int(y3):int(y3 + h_curr), int(x3):int(x3 + w_curr)]
    return img_cropped

def main():
    app = QApplication(sys.argv)
    form1 = ImageCrop()
    form1.show()
    app.exec_()    

if __name__ == '__main__': main()