from tkinter import * # Interface to Tk widgets
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = Button ( self, text="Quit",
            command=self.quit )
        self.quitButton.grid()
app = Application() # Instantiate the application class
app.master.title("Sample application")
app.mainloop() # Wait for events
