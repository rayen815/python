from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from hbdo import*
def check():
    f=0
    t=0
    if r1.isChecked():
        f=10
    elif r2.isChecked():
        f=2
    elif r3.isChecked():
        f=8
    elif r4.isChecked():
        f=16
    if t1.isChecked():
        t=10
    elif t2.isChecked():
        t=2
    elif t3.isChecked():
        t=8
    elif t4.isChecked():
        t=16
    res.setText(convert(ln.text(),f,t))
app = QApplication([])    
w = QWidget()    
b = QLabel(w)
ln=QLineEdit(w)

res=QLineEdit(w)
bt=QPushButton(w)

r1=QRadioButton(w)
r2=QRadioButton(w)
r3=QRadioButton(w)
r4=QRadioButton(w)

t1=QRadioButton(w)
t2=QRadioButton(w)
t3=QRadioButton(w)
t4=QRadioButton(w)

l1=QLabel(w)
l2=QLabel(w)
l3=QLabel(w)
l4=QLabel(w)

l5=QLabel(w)
l6=QLabel(w)
l7=QLabel(w)
l8=QLabel(w)

b.setText("welcome to H.B.D.O (Hexadecimal Binary Decimal Octale) converter")   
l1.setText("decimal")
l2.setText("binary")
l3.setText("octale")
l4.setText("hexadecimal")

l5.setText("decimal")
l6.setText("binary")
l7.setText("octale")
l8.setText("hexadecimal")

bt.setText("GO")

w.setGeometry(100,100,200,50)
g1=QButtonGroup(w)
g2=QButtonGroup(w)

g1.addButton(t1)
g1.addButton(t2)
g1.addButton(t3)
g1.addButton(t4)

g2.addButton(r1)
g2.addButton(r2)
g2.addButton(r3)
g2.addButton(r4)
#--------------------position--------------------
b.move(10,20)
ln.move(150,70)

r1.move(40,120)
r2.move(40,170)
r3.move(40,220)
r4.move(40,270)

t1.move(300,120)
t2.move(300,170)
t3.move(300,220)
t4.move(300,270)

l1.move(70,120)
l2.move(70,170)
l3.move(70,220)
l4.move(70,270)

l5.move(330,120)
l6.move(330,170)
l7.move(330,220)
l8.move(330,270)

bt.move(200,340)
res.move(140,400)

w.setWindowTitle("PyQt5")

w.show()
bt.clicked.connect(check)
app.exec_()
