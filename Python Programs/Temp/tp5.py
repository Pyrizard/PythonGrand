from  tkinter import *
import webbrowser
 
from tkinter.filedialog import askopenfilename
root = Tk()
root.filename =  askopenfilename(title = "choose your file")

print (root.filename)
root.withdraw()
