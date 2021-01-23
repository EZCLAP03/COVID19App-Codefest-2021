from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import input
from kivy.lang import Builder

class CovidApp(MDApp):

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        screen = Screen()


        country = Builder.load_string(input.country)
        screen.add_widget(country)
        return screen


CovidApp().run()
DemoApp().run()