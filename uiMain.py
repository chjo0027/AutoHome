import tkinter
import asyncio
from tkinter import messagebox
import webbrowser
from planLosning import plan
from ljus import send

top = tkinter.Tk()
top.geometry("1920x1080")
top.attributes('-fullscreen', True)

#Bilder
vasttrafik1 = tkinter.PhotoImage(file="bilder//vasttrafik1.gif")
ljus = tkinter.PhotoImage(file="bilder//lampa.gif")
ljud = tkinter.PhotoImage(file="bilder//spotify.gif")
smhi = tkinter.PhotoImage(file="bilder//smhi.gif")
leaving = tkinter.PhotoImage(file="bilder//exit.gif")
calendar = tkinter.PhotoImage(file="bilder//calendar.gif")
settings = tkinter.PhotoImage(file="bilder//settings.gif")
home = tkinter.PhotoImage(file="bilder//home.gif")


#Event, fixa allt som händer
def trafficCallBack():
   webbrowser.open_new('http://sebastiannilsson.com/vasttrafik-widget/next_trips/results?from=Smaragdgatan&to=Lantmilsgatan&max_results=4&weather_image=&no_refresh=0&no_refresh=1')
   #messagebox.showinfo( "Trafik", "Västtrafik")
   #Få upp stations listan från (http://www.vasttrafik.se/nasta-tur-fullskarm/?externalid=9021014006040000&friendlyname=Smaragdgatan+G%c3%b6teborg)

#Lägg in vädertjänst
def weatherCallBack():
    messagebox.showinfo("Väder", "SMHI")

#lägg in kalender
def calendarCallBack():
    messagebox.showinfo("Schema", "Google Calendar")

#Lägg till listan med ESP
def lightCallBack():
    top.destroy()
    plan()
    #send("Computer on")
    #messagebox.showinfo("Ljus", "Ljussidan")

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


#Knapparna
B1 = tkinter.Button( image = vasttrafik1,command = trafficCallBack)
B2 = tkinter.Button( image = smhi, command = weatherCallBack)
B3 = tkinter.Button( image = calendar, command = calendarCallBack)
B4 = tkinter.Button( image = ljus, command = lightCallBack)
B5 = tkinter.Button( image = ljud, command = soundCallBack)
B6 = tkinter.Button( image = home, command = homeCallBack)
B7 = tkinter.Button( image = leaving, command = leavingCallBack)
B8 = tkinter.Button( image = settings, command = propertiesCallBack)

#Placering knappar
B1.place(x=0,y=0)
B2.place(x=480,y=0)
B3.place(x=960,y=0)
B4.place(x=1440,y=0)
B5.place(x=0,y=540)
B6.place(x=480,y=540)
B7.place(x=960,y=540)
B8.place(x=1440,y=540)

top.mainloop()
