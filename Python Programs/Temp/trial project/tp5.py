from tkinter import *
from tkinter.filedialog import askopenfilename

root=Tk()
root.title("One Tap App")
root.iconbitmap(r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\favicon.ico')
root.geometry("420x700")


lbf=LabelFrame(root,text="Select the type of file you wanna open")
lbf.pack()


button1=Button(lbf,text="Music",justify = LEFT)
photo1=PhotoImage(file=r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\trial project\icons\music.png')
button1.config(image=photo1,width="170",height="120")
button1.pack(fill=X)

button2=Button(lbf,text="Images",justify = LEFT)
photo2=PhotoImage(file=r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\trial project\icons\images.png')
button2.config(image=photo2,width="170",height="120")
button2.pack(fill=X)

button3=Button(lbf,text="Videos",justify = LEFT)
photo3=PhotoImage(file=r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\trial project\icons\videos.png')
button3.config(image=photo3,width="170",height="120")
button3.pack(fill=X)

button4=Button(lbf,text="Other Files",justify = LEFT)
photo4=PhotoImage(file=r'C:\Users\Admin\Documents\GitHub\PCube-PythonProgramsPyrizard\Python Programs\Temp\trial project\icons\others.png')
button4.config(image=photo4,width="170",height="120")
button4.pack(fill=X)




root.mainloop()
