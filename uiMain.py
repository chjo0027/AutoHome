import tkinter
from tkinter import messagebox



top = tkinter.Tk()

def trafficCallBack():
   messagebox.showinfo( "Trafik", "Västtrafik")

def weatherCallBack():
    messagebox.showinfo("Väder", "SMHI")

def calendarCallBack():
    messagebox.showinfo("Schema", "Google Calendar")

def lightCallBack():
    messagebox.showinfo("Ljus", "Ljussidan")

def soundCallBack():
   messagebox.showinfo( "Ljud", "Spotify")

def homeCallBack():
    messagebox.showinfo("Hemma", "Tänd hemma")

def leavingCallBack():
    messagebox.showinfo("Går", "Släck hemma")

def propertiesCallBack():
    messagebox.showinfo("Inställningar", "Inställningar")




B = tkinter.Button(top, bg = "blue", text ="Västtrafik", command = trafficCallBack)
C = tkinter.Button(top, bg = "yellow", text ="Väder", command = weatherCallBack)
D = tkinter.Button(top, bg = "green", text ="Schema", command = calendarCallBack)
E = tkinter.Button(top, bg = "red", text ="Ljus", command = lightCallBack)
F = tkinter.Button(top, bg = "purple", text ="Ljud", command = soundCallBack)
G = tkinter.Button(top, bg = "orange", text ="Hemma", command = homeCallBack)
H = tkinter.Button(top, bg = "pink", text ="Går", command = leavingCallBack)
I = tkinter.Button(top, bg = "gold", text ="Inställningar", command = propertiesCallBack)

B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()
H.pack()
I.pack()
top.mainloop()