from  tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
root.filename =  askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
root.withdraw()
