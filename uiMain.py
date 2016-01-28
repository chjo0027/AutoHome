import tkinter
from tkinter import messagebox



top = tkinter.Tk()
top.attributes('-fullscreen', True)

#vasttrafik1 = tkinter.PhotoImage(file="vasttrafik1.gif")
photo = tkinter.PhotoImage(file="Smoke1.gif")
background_label = tkinter.Label(image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Event, fixa allt som händer

#Få upp stations listan från (http://www.vasttrafik.se/nasta-tur-fullskarm/?externalid=9021014006040000&friendlyname=Smaragdgatan+G%c3%b6teborg)
def trafficCallBack():
   messagebox.showinfo( "Trafik", "Västtrafik")

#Lägg in vädertjänst
def weatherCallBack():
    messagebox.showinfo("Väder", "SMHI")

#lägg in kalender
def calendarCallBack():
    messagebox.showinfo("Schema", "Google Calendar")

#Lägg till listan med ESP
def lightCallBack():
    messagebox.showinfo("Ljus", "Ljussidan")

#Ljud öppna spotify och koppla till högtalare
def soundCallBack():
   messagebox.showinfo( "Ljud", "Spotify")

#Kommando för ett visst ljusschema
def homeCallBack():
    messagebox.showinfo("Hemma", "Tänd hemma")

#Kommando för att släcka aktivt ljus
def leavingCallBack():
    messagebox.showinfo("Går", "Släck hemma")

#Kom på inställningar
def propertiesCallBack():
    messagebox.showinfo("Inställningar", "Inställningar")


#Knapparna, fixa storlek och placering
f1 = tkinter.Frame(top, height = 100, width = 150)
B1 = tkinter.Button(f1, bg = "blue", text = "Västtrafik",command = trafficCallBack)
B2 = tkinter.Button(bg = "yellow", text ="Väder", command = weatherCallBack)
B3 = tkinter.Button( bg = "green", text ="Schema", command = calendarCallBack)
B4 = tkinter.Button( bg = "red", text ="Ljus", command = lightCallBack)
B5 = tkinter.Button( bg = "purple", text ="Ljud", command = soundCallBack)
B6 = tkinter.Button( bg = "orange", text ="Hemma", command = homeCallBack)
B7 = tkinter.Button( bg = "pink", text ="Går", command = leavingCallBack)
B8 = tkinter.Button( bg = "gold", text ="Inställningar", command = propertiesCallBack)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()
f1.pack_propagate(0)
f1.pack()
#f2.pack_propagate(0)
#f2.pack()
#f3.pack_propagate(0)
#f3.pack()
#f4.pack_propagate(0)
#f4.pack()
#f4.pack_propagate(0)
#f4.pack()
#f5.pack_propagate(0)
#f5.pack()
#f6.pack_propagate(0)
#f6.pack()
#f7.pack_propagate(0)
#f7.pack()
#f8.pack_propagate(0)
#f8.pack()

top.mainloop()
