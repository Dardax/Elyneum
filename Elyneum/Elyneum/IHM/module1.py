
from tkinter import *
from FicheDePerso import FicheDePerso

def data():
    for i in range(50):
       FicheDePerso(frame).grid(row=0,column=i)
       

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)

root=Tk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=200,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="horizontal",command=canvas.xview)
canvas.configure(xscrollcommand=myscrollbar.set)

myscrollbar.pack(side="bottom",fill="x")
canvas.pack(side="bottom")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()
root.mainloop()