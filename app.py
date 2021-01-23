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
                    text: Username
                    font_style: 'Button1'
                MDLabel:
                    text: Location
                    font_style: 'Button1'
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(toolbar_helper)
        return screen


CovidApp().run()
