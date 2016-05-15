from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from getWeather import getWeather
from kivy.uix.textinput import TextInput

class startSidan(GridLayout):

    def __init__(self, **kwargs):
        super(startSidan, self).__init__(**kwargs)
        self.size=(1920,1080)
        self.cols = 4
        self.vasttrafik1 = Button(background_normal="bilder/vasttrafik1.gif")
        self.ljus = Button(background_normal="bilder/lampa.gif")
        self.ljud = Button(background_normal="bilder/spotify.gif")
        self.smhi = Button(background_normal="bilder/smhi.gif")
        self.leaving = Button(background_normal="bilder/exit.gif")
        self.calendar = Button(background_normal="bilder/calendar.gif")
        self.settings = Button(background_normal="bilder/settings.gif")
        self.home = Button(background_normal="bilder/home.gif")

        self.smhi.bind(on_release=self.weather)
        self.settings.bind(on_release=self.leaveApp)
        self.add_widget(self.vasttrafik1)
        self.add_widget(self.smhi)
        self.add_widget(self.calendar)
        self.add_widget(self.ljus)
        self.add_widget(self.ljud)
        self.add_widget(self.home)
        self.add_widget(self.leaving)
        self.add_widget(self.settings)

    def weather(self, obj):
        weather = getWeather()
        popup = Popup(title='Test popup',
                      content=Label(text=weather),
                      size_hint=(None, None),
                      size=(400, 400))
        popup.open()

    def leaveApp(self, obj):
        App.get_running_app().stop()

class MyApp(App):
    def build(self):
        return startSidan()

if __name__ == "__main__":
    main = MyApp()
    main.run()