from tkinter import *
from tkinter.filedialog import askopenfilename
import webbrowser
import os


root=Tk()
root.title("One Tap App")
root.iconbitmap(r'C:/Users/Admin/Desktop/Simple File Opener/icons/favicon.ico')
root.geometry("420x700")


def openmusic():
    selected_m = askopenfilename(parent=root,initialdir="Libraries/Music",filetypes =(("Music Files", "*.mp3;*.wav;*.aac"),("All Files","*.*")),title = "Choose a music file to play.")
    webbrowser.open(selected_m)
def openimages():
    selected_i = askopenfilename(parent=root,initialdir="Libraries/Pictures",filetypes =(("Image Files", "*.jpg;*.png;*.webp;*.bmp"),("All Files","*.*")),title = "Choose a photo to view.")
    webbrowser.open(selected_i)
def openvideos():
    selected_v = askopenfilename(parent=root,initialdir="Libraries/Videos",filetypes =(("Video Files", "*.mp4;*.wmv;*.mkv;*.avi"),("All Files","*.*")),title = "Choose a video to watch.")
    webbrowser.open(selected_v)
def openothers():
    selected_o = askopenfilename(parent=root,initialdir="Libraries/Documents",filetypes =(("All Files", "*.*"),("All Files","*.*")),title = "Choose any file to open.")
    webbrowser.open(selected_o)

lbf=LabelFrame(root,text="Select the type of file you wanna open")
lbf.pack()




button1=Button(lbf,text="Music",justify = LEFT,command=openmusic)
photo1=PhotoImage(file=r'C:\Users\Admin\Desktop\Simple File Opener\icons\music.png')
button1.config(image=photo1,width="170",height="120")
button1.pack(fill=X)

button2=Button(lbf,text="Images",justify = LEFT,command=openimages)
photo2=PhotoImage(file=r'C:\Users\Admin\Desktop\Simple File Opener\icons\images.png')
button2.config(image=photo2,width="170",height="120")
button2.pack(fill=X)

button3=Button(lbf,text="Videos",justify = LEFT,command=openvideos)
photo3=PhotoImage(file=r'C:\Users\Admin\Desktop\Simple File Opener\icons\videos.png')
button3.config(image=photo3,width="170",height="120")
button3.pack(fill=X)

button4=Button(lbf,text="Other Files",justify = LEFT,command=openothers)
photo4=PhotoImage(file=r'C:\Users\Admin\Desktop\Simple File Opener\icons\others.png')
button4.config(image=photo4,width="170",height="120")
button4.pack(fill=X)

button5=Button(lbf,text="Exit",justify = LEFT,command=root.quit)
#photo5=PhotoImage(file=r'')
#button5.config(image=photo4,width="170",height="120")
button5.pack(fill=X)



root.mainloop()
