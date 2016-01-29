import tkinter

def plan():
    app = tkinter.Tk()
    app.geometry("1920x1080")
    app.attributes('-fullscreen', True)
    ritning = tkinter.PhotoImage(file="bilder//ritning.gif")
    background_label = tkinter.Label(app, image=ritning)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    app.mainloop()