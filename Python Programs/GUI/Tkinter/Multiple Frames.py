from tkinter import *

root = Tk()     #This just creates the window
root.title("Multiple Frames")
#root.geometry('500x200')



frame = Frame(root,bg="Red")                                  #Top Frame
frame.pack()

bottomframe = Frame(root,bg="green")                           #Bottom frame
bottomframe.pack( side = BOTTOM )
#_________________________________________________________________________________________________________________________________________
redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )
#_________________________________________________________________________________________________________________________________________
blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
