import tkinter
from ljus import send

class plan:

    def __init__(self):
        self.computer_state = "asd"
        '''self.app = tkinter.Tk()
        self.app.geometry("1920x1080")
        self.app.attributes('-fullscreen', True)
        self.ritning = tkinter.PhotoImage(file="bilder//ritning.gif")
        self.lampan = tkinter.PhotoImage(file="bilder//lampa2.gif")'''

    def plan(self):
        app = tkinter.Tk()
        app.geometry("1920x1080")
        app.attributes('-fullscreen', True)
        ritning = tkinter.PhotoImage(file="bilder//ritning.gif")
        lampan = tkinter.PhotoImage(file="bilder//lampa2.gif")
        background_label = tkinter.Label(app, image=ritning)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def lampa1():
            if self.computer_state == "on":
                send("Computer off")
                self.computer_state = "off"
                print("on")
            elif self.computer_state == "off":
                send("Computer on")
                self.computer_state = "on"
                print("off")
            else:
                return


        B1 = tkinter.Button(image=lampan, command=lampa1)
        B1.place(x=125,y=700)
        #self.app.after(20,plan)
        app.mainloop()
