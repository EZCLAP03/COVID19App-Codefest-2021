from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

navigation_helper = """
Screen:
    BoxLayout: 
        orientation: 'vertical'
        MDToolbar: 
            title: 'Covid App'
            left_action_items: [{"menu",lambda_x: app.bar_draw()}]
        MDLabel:
            text: 'Cases near you'
            halign: 'center'
            
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def bar_draw(self):
        print('Navigation')


CovidApp().run()
