from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from arrival import arrival_helper

class CovidApp(MDApp):

    def build(self):
        screen = Screen()
                return screen


CovidApp().run()
