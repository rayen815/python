import turtle
import tkinter as tk



root = tk.Tk()
root.geometry("1000x500")
root.resizable()
root.title("hypdraw")
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000") 

t.penup()   
t.pendown()


def repere():
    t.pencolor("black")
    t.speed(0)
    t.penup()
    t.goto(-250,250)
    k=250
    while k>=-250:
        t.penup()
        t.goto(-250,k)
        t.pendown()
        t.goto(250,k)
        k-=10

    k=250
    while k>=-250:
        t.penup()
        t.goto(k,-250)
        t.pendown()
        t.goto(k,250)
        k-=10
    t.penup()
    t.pencolor("red")
    t.goto(0,250)
    t.pendown()
    t.goto(0,-250)
    t.penup()
    t.pencolor("red")
    t.goto(250,0)
    t.pendown()
    t.goto(-250,0)

    t.penup()
    t.pencolor("black")
    t.pensize(1)
    t.goto(2,-2)
    t.write("0")
    t.goto(2,48)
    t.write("5")
    t.goto(1,98)
    t.write("10")
    t.goto(1,148)
    t.write("15")
    t.goto(1,198)
    t.write("20")

    t.goto(2,-52)
    t.write("5")
    t.goto(1,-102)
    t.write("10")
    t.goto(1,-152)
    t.write("15")
    t.goto(1,-202)
    t.write("20")

    t.goto(43,-2)
    t.write("5")
    t.goto(90,-2)
    t.write("10")
    t.goto(140,-2)
    t.write("15")
    t.goto(190,-2)
    t.write("20")


    t.goto(-46,-2)
    t.write("5")
    t.goto(-101,-2)
    t.write("10")
    t.goto(-151,-2)
    t.write("15")
    t.goto(-201,-2)
    t.write("20")


label = tk.Label(root, text="Choose the type :")
label.place(x=15,y=60)

e = tk.Entry(root,font=('Arial', 14))
e.place(x=15,y=25,width=220,height=30)

labe2 = tk.Label(root, text="f(x) :")
labe2.place(x=15,y=5)
var = tk.IntVar() 
r1 = tk.Radiobutton(root, text='parabole',variable=var, value=1) 
r2 = tk.Radiobutton(root, text='hyperbole',variable=var, value=2) 
r1.place(x=15,y=80)
r2.place(x=15,y=100)

repere()

s=tk.Button(master = root, text = "Start",command=repere )
s.place(x=70,y=130,width=110,height=30)

root.mainloop()