'''#!/usr/bin/env python     only for linux'''                                  #1
import tkinter as tk                                                            #2

class Application(tk.Frame):                                                    #3
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)                                         #4
        self.grid()                                                             #5
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
        command=self.quit)                                                      #6
        self.quitButton.grid()                                                  #7
app = Application()                                                             #8
app.master.title('Sample application')                                          #9
app.mainloop()                                                                  #10


'''
1 This line makes the script self-executing, assumingthatyour system has Python correctlyinstalled.
2 This line imports the Tkinter module into your program's namespace, but renames it as tk.
3 Your application class must inherit from Tkinter's Frame class.
4 Calls the constructor for the parent class, Frame.
5 Necessary to make the application actually appear on the screen.
6 Creates a button labeled “Quit”.
7 Places the button on the application.
8 The main program starts here by instantiating the Application class.
9 This method call sets the title of the window to “Sample application”.
10 Starts the application's main loop, waiting for mouse and keyboard events.
'''
