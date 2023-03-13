from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from hbdo import*

app = QApplication([])    
w=loadUi("cal.ui")

w.show()
app.exec_()