import tkinter as tk

class Aplikacja(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.przykladowaEtykieta = tk.Label(self, text='Hello world')
        self.przykladowaEtykieta.config(bg="#00ffff")
        self.przykladowaEtykieta.grid()
        self.quitButton = tk.Button(self, text='End', command=self.quit)
        self.quitButton.grid()

app = Aplikacja()
app.master.title('Example app')
app.mainloop()