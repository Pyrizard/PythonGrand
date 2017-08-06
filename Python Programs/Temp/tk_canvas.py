from tkinter import *

root= Tk()

lbl= Label(root,text="This is a label ")
lbl.pack()

w = Canvas (root, bg="red",cursor="dot",height=30,width=100,bd=5)
w.pack()
root.mainloop()
