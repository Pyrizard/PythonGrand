from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox

import webbrowser               #simplest lib i found for opening files

root = Tk()
root.title("Simple Window")
#root.geometry("700x500")                                       #uncomment root.geometryto apply that size to Window
root.iconbitmap(r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\favicon.ico')



def openfile():
    selected_file = askopenfilename(parent=root)
    webbrowser.open(selected_file)          #i find this method easy to open files
def hello():
    print ("As Salaamu Alaikum!")
def calc():
    os.system("C:\Windows\system32\calc.exe")
def paint():
    os.system("%windir%\system32\mspaint.exe")
def mb():
    messagebox.showinfo("Credit","This simple app is created by a python lover")
def google():
    webbrowser.open('http://google.co.in')



label1= Label(root,text="As Salaamu Alaikum \n Welcome to this simple frame packed with noob widgets.\n This yellow part is Label 1",bg="yellow")
label1.pack()
label2= Label(root,text="Okay See \n This grey part is Label 2",bg="grey")
label2.pack()


calc_button = Button(root, height=2, width=10, text ="Calculator",fg="green", command = calc )
calc_button.pack()
paint_button = Button(root, height=2, width=10, text ="Paint",fg="purple", command = paint)
paint_button.pack()
about_button = Button(root, height=2, width=10, text ="About",fg="blue", command = mb)
about_button.pack()
homepage_button = Button(root, height=2, width=10, text ="Google India",fg="green", command = google )
homepage_button.pack()
exit_button = Button(root, height=2, width=10, text ="Exit",fg="maroon", command = root.quit)
exit_button.pack()




menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
