from kivymd.app import MDApp
from kivy.lang import Builder

toolbar_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Covid App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
                    
        
        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                
                MDLabel:
                    text: 'Caption'
                    font_style: 'Button'
                MDLabel:
                    text: 'Caption'
                    font_style: 'Button'
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(toolbar_helper)
        return screen


CovidApp().run()
