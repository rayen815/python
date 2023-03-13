from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from hbdo import*
def check():
    f=0
    t=0
    if w.r1.isChecked():
        f=10
    elif w.r2.isChecked():
        f=2
    elif w.r3.isChecked():
        f=8
    elif w.r4.isChecked():
        f=16
    if w.t1.isChecked():
        t=10
    elif w.t2.isChecked():
        t=2
    elif w.t3.isChecked():
        t=8
    elif w.t4.isChecked():
        t=16
    w.res.setText(convert(w.ln.text(),f,t))
app = QApplication([])    
w=loadUi("conv.ui")
g1=QButtonGroup(w)
g2=QButtonGroup(w)

g1.addButton(w.t1)
g1.addButton(w.t2)
g1.addButton(w.t3)
g1.addButton(w.t4)

g2.addButton(w.r1)
g2.addButton(w.r2)
g2.addButton(w.r3)
g2.addButton(w.r4)

w.setWindowTitle("PyQt5")

w.show()
w.bt.clicked.connect(check)
app.exec_()