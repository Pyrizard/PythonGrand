from tkinter import *


root=Tk()
root.title("Two frames left and right")
#root.geometry("700x300")                            #<---------    optional
root.state("zoomed")


frame=LabelFrame(root,height=500,width=500,bg="darkorchid2")
frame.pack(fill=X)

leftlabel=Label(frame,text="This is left lable",bg="sienna1",height=10,width=50)
leftlabel.pack(side=LEFT,expand=TRUE)
rightlabel=Label(frame,text="This is right lable",bg="red",height=10,width=50)
rightlabel.pack(side=LEFT,expand=TRUE)

#________________________________________________________________________________

frame1 = LabelFrame(root, bg="green",text="GROUP OF LABELS", padx=5, pady=5)
frame1.pack(padx=10, pady=10)

leftlabel=Label(frame1,text="LEFT BLOCK",bg="snow3",height=10,width=50)
leftlabel.pack(side=LEFT,expand=TRUE)
rightlabel=Label(frame1,text="RIGHT BLOCK",bg="khaki",height=10,width=50)
rightlabel.pack(side=LEFT,expand=TRUE)


root.mainloop()
