from kivymd.app import MDApp
from kivy.lang import Builder
from helpers import toolbar_helper


class CovidApp(MDApp):
    def build(self):
        screen = Builder.load_string(toolbar_helper)
        return screen


CovidApp().run()
