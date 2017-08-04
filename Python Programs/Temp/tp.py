from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox
import webbrowser               #simplest lib i found for opening files

root = Tk()
root.title("Simple Window")
root.geometry("250x200")
root.iconbitmap(r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\favicon.ico')


def openfile():
    selected_file = askopenfilename(parent=root)
    webbrowser.open(selected_file)
    '''f = open(filename)
    f.read()'''
    '''with open(filename, 'rb') as f:
        contents = f.read()
    #f = file.open("filename","rb")'''


def hello():
    print ("As Salaamu Alaikum!")
def calc():
    os.system("C:\Windows\system32\calc.exe")
def paint():
    os.system("%windir%\system32\mspaint.exe")
def mb():
    messagebox.showinfo("Credit","This simple app is created by a python lover")



calc_button = Button(root, height=2, width=10, text ="Calculator", command = calc )
calc_button.pack()
paint_button = Button(root, height=2, width=10, text ="Paint", command = paint)
paint_button.pack()
about_button = Button(root, height=2, width=10, text ="About", command = mb)
about_button.pack()
exit_button = Button(root, height=2, width=10, text ="Exit", command = root.quit)
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
