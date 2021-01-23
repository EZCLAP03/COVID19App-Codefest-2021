from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

navigation_bar = """
Screen:
    BoxLayout: 
        orientation: 'vertical'
        MDToolbar: 
            title: 'Covid App'
        MDLabel:
            text: 'Cases near you'
            halign: 'center'
            
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_bar)
        return screen


CovidApp().run()
