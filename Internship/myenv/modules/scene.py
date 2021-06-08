# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 14:26:15 2019

@author: elh
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush 
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem
import sys

app = QApplication(sys.argv)
scene = QGraphicsScene() 
rectGris = QGraphicsRectItem(0.,0.,200.,150.) 
rectGris.setBrush(QBrush(Qt.lightGray)) 
scene.addItem(rectGris) 
# definition de la vue
vue = QGraphicsView(scene) 
vue.resize(800,600) 
vue.fitInView(rectGris,Qt.KeepAspectRatio) 
vue.show() 
sys.exit(app.exec_())
